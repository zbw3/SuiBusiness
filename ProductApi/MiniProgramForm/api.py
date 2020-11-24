#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File   : api.py
# @Author : mocobk
# @Email  : mailmzb@qq.com
# @Time   : 2019/1/22 9:53
import mimetypes
import os
import threading

import jmespath

from ProductApi.MiniProgramForm import config
from ProductApi.base import ApiBase, Response
import urllib3

urllib3.disable_warnings()


class SingletonMetaClass(type):
    _instance_lock = threading.Lock()  # 支持多线程的单例模式
    _instance = {}

    def __call__(cls, *args, **kwargs):
        """"
        元类实现 FormApi 单例模式，避免同一个账号被实例化多次，导致多次请求登录接口
        没有用 def __new__(cls, *args, **kwargs) 方式实现单例，因为 __new__ 不返回一个已实例化的对象,
        它返回一个在其后调用__init__的单元化对象，即虽然是单例，但每次都会调用 __init__,如下：
        a = A() 实际上是 a = A.__new__(A) 和 a.__init__()
        """
        fuid = args[0] if args else kwargs.get('fuid') or config.UserFuid.user1
        if not cls._instance.get(fuid):
            with cls._instance_lock:
                if not cls._instance.get(fuid):
                    cls._instance[fuid] = super().__call__(*args, **kwargs)

        return cls._instance[fuid]


class FormResponse(Response):
    form_id = None


class FormApi(ApiBase, metaclass=SingletonMetaClass):
    USER = config.UserFuid
    Response = FormResponse

    def __init__(self, fuid=config.UserFuid.user1, print_results=False):
        """
        :param fuid: 用户群报数 id, 不传则使用配置中默认的
        """
        self.config: config.Test = getattr(config, self.env.name)
        super().__init__(self.config, print_results)
        self.fuid = fuid or self.config.DUFAULT_FUID
        self.authorized_hearders = self.get_authorized_hearders()

    def get_authorized_hearders(self) -> dict:
        """
        登录鉴权
        """
        data = {
            "appId": self.config.APP_ID,
            "fuid": self.fuid
        }
        self.set_logger_off()
        self.logger.info('正在登陆...')
        response = super().request(url=self.config.Url.v1_login_test, method=self.POST, json=data)
        self.set_logger_on()

        if response.status_code != 200:
            raise Exception('登陆失败！请检查环境和账号')
        return {'Authorization': response.data.get('data', {}).get('token', '')}

    def request(self, url, method,
                params=None, data=None, json=None, headers=None, cookies=None, files=None,
                auth=None, timeout=None, allow_redirects=True, hooks=None, stream=None, **kwargs) -> Response:
        """
        need_auth:  是否需要鉴权， 服务端这边对于不需要鉴权的但传
        :return:
        """
        headers = {**headers, **self.authorized_hearders} if headers else self.authorized_hearders
        response = super().request(url, method,
                                   params, data, json, headers, cookies, files,
                                   auth, timeout, allow_redirects, hooks, stream, **kwargs)

        if response.status_code == 401:
            self.logger.info('登录 token 过期，重新登录中...')
            self.authorized_hearders = self.get_authorized_hearders()
            if self.authorized_hearders:
                self.logger.info(f'登录中成功，重试请求：{response.request.url}')
                response = self.request(url, method,
                                        params, data, json, headers, cookies, files,
                                        auth, timeout, allow_redirects, hooks, stream, **kwargs)

        return response

    def v1_creation_forms(self, params, method='GET'):
        """
        Name: 我创建的表单列表
        """
        url = self.config.Url.v1_creation_forms
        response = self.request(url=url, method=method, params=params)
        return response

    def v1_participation_forms(self, params, method='GET'):
        """
        Name: 我参与的表单列表
        """
        url = self.config.Url.v1_participation_forms
        response = self.request(url=url, method=method, params=params)
        return response

    def v1_examples(self, method='GET'):
        """
        Name: 我创建的表单列表
        """
        url = self.config.Url.v1_examples
        response = self.request(url=url, method=method)
        return response

    def v1_image(self, image: str, method='POST'):
        """
        Name: 上传图片
        file: 可以是本地文件路径，也可以是 url
        """
        url = self.config.Url.v1_image
        if image.startswith('http'):
            try:
                res = self.request(url=image, method='GET', timeout=120)
            except Exception as e:
                self.logger.warning(f'{e} \n重试中...')
                self.v1_image(image)
                return
            fp = res.content
            name = 'image.jpg'
            content_type = res.headers.get('Content-Type', 'image/jpeg')
        else:
            fp = open(image, 'rb')
            name = os.path.basename(image)
            content_type = mimetypes.guess_type(image)[0]

        files = {'file': (name, fp, content_type)}
        response = self.request(url=url, method=method, files=files)
        return response

    def v1_form(self, data, return_form_id=False, method='POST'):
        """
        创建表单
        :param data:
        :param return_form_id: 创建表单接口不支持返回新创建的表单 id， 这里通过获取创建表单列表拿到最新创建的表单 id
        :param method: POST
        :return:
        """
        url = self.config.Url.v1_form
        response = self.request(url=url, method=method, json=data)
        if return_form_id:
            creation_forms = self.v1_creation_forms({'pageNo': 1, 'pageSize': 5})
            if creation_forms.status_code != 200:
                raise Exception('创建表单后获取表单 id 失败')
            form_ids = jmespath.search('@.data.creations.*[*].formId[]', creation_forms.data)
            response.form_id = form_ids[0]
        return response

    def v1_form_form_id(self, form_id, data=None, method='GET'):
        """
        获取表单详情、更新表单
        :param form_id:
        :param data:
        :param method: GET | PUT
        :return:
        """
        url = self.config.Url.v1_form_form_id.format(formId=form_id)
        response = self.request(url=url, method=method, json=data)
        return response

    def v1_form_id_form_data(self, form_id, data=None, form_data_id=None, method='GET'):
        """
        获取我的接龙、提交接龙、修改接龙、取消接龙
        :param form_id:
        :param data:
        :param form_data_id:
        :param method: GET | POST | PUT | DELETE
        :return:
        """
        url = self.config.Url.v1_form_id_form_data.format(formId=form_id)
        params = {'formDataId': form_data_id} if form_data_id else None
        response = self.request(url=url, method=method, params=params, json=data)
        return response

    def v1_form_id_status(self, form_id, status, method='PUT'):
        url = self.config.Url.v1_form_id_status.format(formId=form_id)
        response = self.request(url=url, method=method, params={'status': status})
        return response

    def v1_order_list_form_id(self, form_id, page_no=1, page_size=10, method='GET'):
        url = self.config.Url.v1_order_list_form_id.format(formId=form_id)
        params = {'pageNo': page_no, 'pageSize': page_size}
        response = self.request(url=url, method=method, params=params)
        return response

    def v1_order_query_form_id_fuid(self, form_id, fuid, page_no=1, page_size=10, method='GET'):
        url = self.config.Url.v1_order_query_form_id_fuid.format(formId=form_id, fuid=fuid)
        params = {'pageNo': page_no, 'pageSize': page_size}
        response = self.request(url=url, method=method, params=params)
        return response

    def v1_order_form_id_order_id(self, form_id, order_id, method='GET'):
        """
        :param form_id:
        :param order_id:
        :param method: GET | DELETE
        :return:
        """
        url = self.config.Url.v1_order_form_id_order_id.format(formId=form_id, orderId=order_id)
        response = self.request(url=url, method=method)
        return response

    def v1_order_form_id_order_id_remarks(self, form_id, order_id, remarks: str = None, method='POST'):
        """
        :param form_id:
        :param order_id:
        :param remarks:
        :param method: POST | PUT
        :return:
        """
        url = self.config.Url.v1_order_form_id_order_id_remarks.format(formId=form_id, orderId=order_id)
        headers = {'Content-Type': 'application/json'}
        response = self.request(url=url, method=method, data=remarks.encode('utf-8'), headers=headers)
        return response

    def v1_statistic_analysis_form_id(self, form_id, method='GET'):
        url = self.config.Url.v1_statistic_analysis_form_id.format(formId=form_id)
        response = self.request(url=url, method=method)
        return response

    def v1_statistic_detail_form_id(self, form_id, sort_field, sort_type, method='GET'):
        """
        :param form_id:
        :param sort_field: SEQUENCE 序号 | NICKNAME 昵称 | TIME 创建时间 | STATUS 状态 | MONEY 金额 | cid 对应填写项
        :param sort_type: ASC 升序排列 | DESC 降序排列
        :param method:
        :return:
        """
        url = self.config.Url.v1_statistic_detail_form_id.format(formId=form_id)
        params = {'sortField': sort_field, 'sortType': sort_type}
        response = self.request(url=url, method=method, params=params)
        return response

    def v1_operation_forms(self, table_id, method='GET'):
        """
        首页瀑布流表单
        :param table_id: TUTORIAL_HELP: 教程帮助CASE_TEMPLATE: 案例模板 NO_TAB:首页
        :param method:
        :return:
        """
        url = self.config.Url.v1_operation_forms
        params = {'tabId': table_id}
        response = self.request(url=url, method=method, params=params)
        return response

    def v1_form_operation_operation_operation_form_id(self, form_id, method='GET'):
        """
        获取运营表单内容
        :param form_id:
        :param method:
        :return:
        """
        url = self.config.Url.v1_form_operation_operation_operation_form_id.format(operationFormId=form_id)
        response = self.request(url=url, method=method)
        return response

    def v1_form_operation_form_operation_form_id(self, form_id, method='GET'):
        """
        获取普通表单内容
        :param form_id:
        :param method:
        :return:
        """
        url = self.config.Url.v1_form_operation_form_operation_form_id.format(operationFormId=form_id)
        response = self.request(url=url, method=method)
        return response

    def v1_templates_lit(self, tab_id, method='GET'):
        """
        获取模板表单列表
        :param tab_id: STATISTIC：报数统计INFORMATION：信息登记SHOPPING：商品接龙SIGN_UP：活动报名QUESTIONNAIRE：调查问卷
        :param method:
        :return:
        """
        url = self.config.Url.v1_templates_lit
        params = {'tabId': tab_id}
        response = self.request(url=url, method=method, params=params)
        return response

    def v1_form_operation_template_operation_form_id(self, form_id, method='GET'):
        """
        获取表单模板内容
        :param form_id:
        :param method:
        :return:
        """
        url = self.config.Url.v1_form_operation_template_operation_form_id.format(operationFormId=form_id)
        response = self.request(url=url, method=method)
        return response

    def v1_form_manager_invitation_code(self, form_id, method='GET'):
        """
        生成表单管理员邀请码
        :param form_id:
        :param method: GET
        :return:
        """
        url = self.config.Url.v1_form_manager_invitation_code
        params = {'formId': form_id}
        response = self.request(url=url, method=method, params=params)
        return response

    def v1_form_manager(self, form_id, code, method='POST'):
        """
        扫码加入管理员
        :param form_id: 表单ID短链
        :param code: 邀请码短链
        :param method: POST
        :return:
        """
        url = self.config.Url.v1_form_manager
        data = {
            "formId": form_id,
            "code": code
        }
        response = self.request(url=url, method=method, json=data)
        return response

    def v1_form_managers_form_id(self, form_id, method='GET'):
        """
        获取表单管理员列表
        :param form_id: 表单 ID
        :param method: GET
        :return:
        """
        url = self.config.Url.v1_form_managers_form_id.format(formId=form_id)
        response = self.request(url=url, method=method)
        return response

    def v1_form_manager_form_id(self, form_id, fuid=None, method='DELETE'):
        """
        删除表单管理员列表，注意与获取表单管理员列表 path 不是同一个
        :param form_id: 表单 ID
        :param fuid: 用户 ID
        :param method: DELETE
        :return:
        """
        url = self.config.Url.v1_form_manager_form_id.format(formId=form_id)
        response = self.request(url=url, method=method, params={'fuid': fuid})
        return response

    def v1_form_manager_poster(self, form_id, method='GET'):
        """
        获取管理员邀请海报信息
        :param form_id: 表单ID
        :param method: GET
        :return:
        """
        url = self.config.Url.v1_form_manager_poster
        response = self.request(url=url, params={'formId': form_id}, method=method)
        return response

    def v1_form_operation_official_account_form_id(self, form_id, method='GET'):
        """
        获取公众号文章内容
        :param form_id:
        :param method:
        :return:
        """
        url = self.config.Url.v1_form_operation_official_account_form_id.format(operationFormId=form_id)
        response = self.request(url=url, method=method)
        return response

    def v1_operation_position(self, ver, method='GET'):
        """
        获取运营位配置相关信息
        :param ver: 当前版本号，每个版本段占两位数，例如1.1.0版：10100
        :param method:
        :return:
        """
        url = self.config.Url.v1_operation_position
        params = {'ver': ver}
        response = self.request(url=url, method=method, params=params)
        return response


if __name__ == '__main__':
    os.environ['env'] = 'test'
    api = FormApi(fuid='1072705375733551112', print_results=True)

    # api.v1_operation_forms(params={'tabId': "TUTORIAL_HELP"})
    # api.v1_operation_forms("TUTORIAL_HELP")

    # api.v1_templates_lit("STATISTIC")
    # api.v1_form_operation_template_operation_form_id(1082098651125252096)

    # api.v1_form_operation_operation_operation_form_id(1070883234922893333)
    # api.v1_statistic_analysis_form_id(1076668355504508928)
    api.v1_statistic_detail_form_id(1076668355504508928, 'SEQUENCE', 'ASC')

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File   : api.py
# @Author : mocobk
# @Email  : mailmzb@qq.com
# @Time   : 2019/1/22 9:53
import mimetypes
import os
import threading
import time
from requests_toolbelt.multipart.encoder import MultipartEncoder
import random


import jmespath

from ProductApi.MiniProgramForm import config
from ProductApi.base import ApiBase, Response
import urllib3

urllib3.disable_warnings()
path = 'E:\SuiBusiness\test_cases\mp_form\images'


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

    def v1_manager_froms(self, params, method='GET'):
        """
        Name: 我管理的表单列表
        :param params:
        :param method:
        :return:
        """
        url = self.config.Url.v1_manager_forms
        response = self.request(url=url, method=method, params=params)
        return response

    # def v1_examples(self, method='GET'):
    #     """
    #     Name: 我创建的表单列表(已废弃)
    #     """
    #     url = self.config.Url.v1_examples
    #     response = self.request(url=url, method=method)
    #     return response

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

    def v2_pre_upload_image(self, file_num, method='GET'):
        url = self.config.Url.v2_image_pre_upload
        param = {"fileNum": file_num}
        r = self.request(url, params=param, verify=False,  method=method)
        result = r.json()
        new_result = {}
        new_result["host"] = result["data"]["aliSign"]["host"]
        new_result["filenames"] = result["data"]["filenames"]
        new_result["accessid"] = result["data"]["aliSign"]["accessid"]
        new_result["policy"] = result["data"]["aliSign"]["policy"]
        new_result["signature"] = result["data"]["aliSign"]["signature"]
        new_result["prefix"] = result["data"]["aliSign"]["prefix"]
        return new_result

    def oss_request(self, i, method='POST'):
        sign = self.v2_pre_upload_image(i)
        print("sign_________", sign["filenames"][0])
        oss_url = sign["host"] + "/"
        oss_url_l = []
        headers = {

            "Authorization": self.authorized_hearders,
            "content-type": "multipart/form-data; boundary=1661410466636"

        }

        multipart_encoder = MultipartEncoder(
            fields={
                "OSSAccessKeyId": sign["accessid"],
                "key": sign["prefix"] + sign["filenames"][0] + ".jpg",
                "policy": sign["policy"],
                "signature": sign["signature"],
                "file": (f"{random.randint(3, 5)}.jpg",
                         open(f"E:\SuiBusiness\ProductApi\MiniProgramForm\images\{random.randint(3, 5)}.jpg", "rb"), "image/jpg")
            })
        headers['Content-Type'] = multipart_encoder.content_type

        # 请求头必须包含Content-Type: multipart/form-data; boundary=${bound}
        # 这里也可以自定义boundary
        r = self.request(oss_url, data=multipart_encoder, headers=headers, verify=False, method=method)
        for n in sign["filenames"]:
            img_url = oss_url + sign["prefix"] + n + ".jpg"
            oss_url_l.append(img_url)

        print(oss_url_l)
        return img_url





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
            # creation_forms = self.v1_creation_forms({'pageNo': 1, 'pageSize': 5})
            # print('我发布的列表数据：',creation_forms.data)
            # if creation_forms.status_code != 200:
            #     raise Exception('创建表单后获取表单 id 失败')
            # form_ids = jmespath.search('@.data.creations.*[*].formId[]', creation_forms.data)
            # response.form_id = form_ids[0]
            # 通过headers中获取创建的formId
            response.form_id = response.headers.get('formId')
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

    def v3_form_form_id(self, form_id, data=None, method='GET'):
        """
        获取表单详情--版本兼容、更新表单
        :param form_id:
        :param data:
        :param method: GET | PUT
        :return:
        """
        url = self.config.Url.v3_form_form_id.format(formId=form_id)
        response = self.request(url=url, method=method, json=data)
        return response

    def v1_form_profile(self, form_id, data=None, method='GET'):
        """
        获取表单详情--剔除问题项
        :param form_id:
        :param data:
        :param method:
        :return:
        """
        url = self.config.Url.v1_form_profile.format(formId=form_id)
        response = self.request(url=url, method=method, json=data)
        return response

    def v1_from_catalog(self, form_id, data=None, method='GET'):
        """
        表单问题项接口
        :param from_id:
        :param data:
        :param method:
        :return:
        """
        url = self.config.Url.v1_form_catalog.format(formId=form_id)
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

    def v3_form_id_form_datas(self, form_id, method='GET'):
        """
        获取接龙统计数据
        :param form_id:
        :param method: GET
        :return:
        """
        url = self.config.Url.v3_form_id_form_datas.format(formId=form_id)
        response = self.request(url=url, method=method)
        return response

    def v1_form_data_last(self,form_id,method='GET'):
        """
        我的报名最新一条
        :param form_id:
        :param method:
        :return:
        """
        url = self.config.Url.v1_form_data_last.format(formId=form_id)
        response = self.request(url=url, method='GET')
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

    def v1_statistic_analysis_form_id(self, form_id, start, end, method='GET'):
        """
        统计分析接口
        :param form_id:
        :param start: 开始时间
        :param end: 结束时间
        :param method:
        :return:
        """
        url = self.config.Url.v1_statistic_analysis_form_id.format(formId=form_id)
        params = {'startTime': start, 'endTime': end}
        response = self.request(url=url, method=method, params=params)
        return response

    def v1_statistic_detail_form_id(self, form_id, sort_field, sort_type, start, end, method='GET'):
        """
        详细数据接口
        :param form_id:
        :param sort_field: SEQUENCE 序号 | NICKNAME 昵称 | TIME 创建时间 | STATUS 状态 | MONEY 金额 | cid 对应填写项
        :param sort_type: ASC 升序排列 | DESC 降序排列
        :param start: 开始时间
        :param end: 借宿时间
        :param method:
        :return:
        """
        url = self.config.Url.v1_statistic_detail_form_id.format(formId=form_id)
        params = {'sortField': sort_field, 'sortType': sort_type, 'startTime': start, 'endTime': end}
        response = self.request(url=url, method=method, params=params)
        return response

    def v1_form_data_owner(self, form_id, pageNo, pageSize,method='GET'):
        """
        详细数据接口
        :param form_id:
        :param sort_field: SEQUENCE 序号 | NICKNAME 昵称 | TIME 创建时间 | STATUS 状态 | MONEY 金额 | cid 对应填写项
        :param sort_type: ASC 升序排列 | DESC 降序排列
        :param start: 开始时间
        :param end: 借宿时间
        :param method:
        :return:
        """
        url = self.config.Url.v1_form_data_owener.format(formId=form_id)
        params = {'pageNo': pageNo, 'pageSize': pageSize, }
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

    def v1_templates(self,method="GET"):
        """
        获取模板列表的所有模板贴
        :return:
        """
        url = self.config.Url.v1_templates
        response = self.request(url=url,method=method)
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
        获取公众号文章内容（这个接口主要是为了统计入口流量，让前端多调用一次）
        :param form_id:
        :param method:
        :return:
        """
        url = self.config.Url.v1_form_operation_official_account_form_id.format(operationFormId=form_id)
        response = self.request(url=url, method=method)
        return response

    def v1_operation_position(self, method='GET'):
        """
        获取运营位配置相关信息
        :param method:
        :return:
        """
        url = self.config.Url.v1_operation_position
        response = self.request(url=url, method=method)
        return response

    def v1_config(self, method='GET'):
        """
        获取强制更新及当前域名等配置信息
        :param method:
        :return:
        """
        params = {
            "t": str(time.time()).split(".")[0]
        }
        url = self.config.Url.v1_config
        response = self.request(url=url, method=method,params=params, verify=False)
        return response


    def v1_form_id_cycle_form_datas(self, form_id, page_no=1, page_size=20, method='GET'):
        """
        获取今日循环表单的报名数据
        :param method:
        :return:
        """
        url = self.config.Url.v1_form_id_cycle_form_datas.format(formId=form_id)
        params = {'formId': form_id, 'pageNo': page_no, 'pageSize': page_size}
        response = self.request(url=url, method=method, params=params)
        return response

    def v2_form_id_cycle_participant(self, form_id, page_no=1, page_size=20, method='GET'):
        """
        获取参与过表单报名，但是今日未报名的用户信息
        :param method:
        :return:
        """
        url = self.config.Url.v2_form_id_cycle_participant.format(formId=form_id)
        params = {'formId': form_id, 'pageNo': page_no, 'pageSize': page_size}
        response = self.request(url=url, method=method, params=params)
        return response

    def v2_form_id_cycle_ranking(self, form_id, page_no=1, page_size=20, start_time=None, end_time=None, method='GET'):
        """
        获取循环表单用户报名的排行榜信息
        :param method:
        :return:
        """
        url = self.config.Url.v2_form_id_cycle_ranking.format(formId=form_id)  # v1变v2
        params = {'formId': form_id, 'pageNo': page_no, 'pageSize': page_size, 'startTime': start_time,
                  'endTime': end_time}
        response = self.request(url=url, method=method, params=params)
        return response

    def v1_form_id_participant_fuid(self, form_id, fuid, method='DELETE'):
        """
        从报名统计和排行榜中移除用户功能
        :param method:
        :return:
        """
        url = self.config.Url.v1_form_id_participant_fuid.format(formId=form_id, fuid=fuid)
        params = {'formId': form_id, 'fuid': fuid}
        response = self.request(url=url, method=method, params=params)
        return response

    def v1_complaint(self, form_id, reason=None, description=None, images=None, contact=None, method='POST'):
        """
        提交投诉表单
        :param form_id:
        :param reason: 投诉原因的key（必填）
        :param description: 投诉描述（必填）
        :param images: 截图证据（选填）
        :param contact: 联系方式（选填）
        :param method:
        :return:
        """
        url = self.config.Url.v1_complaint
        data = {
            'formId': form_id,
            'reason': reason,
            'description': description,
            'images': images,
            'contact': contact
        }
        response = self.request(url=url, method=method, json=data)
        return response

    def v1_comlpaint_reason(self, method='GET'):
        """
        获取投诉原因列表
        :param method:
        :return:
        """
        url = self.config.Url.v1_comlpaint_reason
        response = self.request(url=url, method=method)
        return response

    def v1_map_location_info(self, lat, lng, method='GET'):
        """
        获取附近地图位置
        :param lat:纬度
        :param lng:经度
        :param method:
        :return:
        """
        url = self.config.Url.v1_map_location_info
        params = {'lat': lat, 'lng': lng}
        response = self.request(url=url, method=method, params=params)
        return response

    """接口废弃"""
    # def v1_name_list(self, form_id=None, value=None, method='POST'):
    #     """
    #     提交预设名单
    #     :param form_id:表单id，新建表单时不传，修改表单时传
    #     :param value:名单数组
    #     :param method:请求方式：POST:创建预设名单，PUT：修改预设名单
    #     :return:
    #     """
    #     url = self.config.Url.v1_name_list
    #     data = {
    #         'formId': form_id,
    #         'value': value
    #     }
    #     response = self.request(url=url, method=method, json=data)
    #     return response

    """接口废弃"""
    # def v1_namelist(self, nlid, method='GET'):
    #     """
    #     获取预设名单
    #     :param nlid:预设名单ID
    #     :param method:
    #     :return:
    #     """
    #     url = self.config.Url.v1_namelist.format(nlid=nlid)
    #     response = self.request(url=url, method=method)
    #     return response

    def v1_export_url_name_list_nlid(self, nlid, startTime=None, endTime=None, method='GET'):
        """
        获取导出预设名单链接地址
        :param nlid:预设名单ID
        :param method:
        :param startTime:开始时间
        :param endTime:结束时间
        :return:
        """
        url = self.config.Url.v1_export_url_name_list_nlid.format(nlid=nlid)
        params = {'startTime': startTime, 'endTime': endTime}
        response = self.request(url=url, method=method, params=params)
        return response

    def v1_export_name_list_nlid_ticket(self, nlid, ticket, startTime=None, endTime=None, method='GET'):
        """
        导出预设名单接口
        :param nlid:预设名单ID
        :param ticket:导出凭证
        :param method:
        :return:
        """
        url = self.config.Url.v1_export_name_list_nlid_ticket.format(nlid=nlid)
        params = {'ticket': ticket, 'startTime': startTime, 'endTime': endTime}
        response = self.request(url=url, method=method, params=params)
        return response

    def v1_form_id_sign_up(self, form_id, method='GET'):
        """
        签到详情接口
        :param form_id: 表单ID
        :param method: GET
        :return:
        """
        url = self.config.Url.v1_form_id_sign_up.format(formId=form_id)
        response = self.request(url=url, method=method)
        return response

    def v1_form_id_sign_up_form_data_id(self, form_id, form_data_id, method='GET'):
        """
        签到接口
        :param form_id:表单ID
        :param form_data_id:签到详细接口返回list中的fid
        :param method:
        :return:
        """
        url = self.config.Url.v1_form_id_sign_up_form_data_id.format(formId=form_id, formDataId=form_data_id)
        response = self.request(url=url, method=method)
        return response

    def v1_form_inform(self, form_id, config, method='PUT'):
        """
        配置表单公众号通知，仅发布者和管理员可以配置
        :param form_id:
        :param config:
        :param method:
        :return:
        """
        url = self.config.Url.v1_from_inform.format(formId=form_id)
        # params = {'config': config}
        response = self.request(url=url, method=method, json=config)
        return response

    def v1_form_inform_get(self, form_id, method='GET'):
        """
        获取表单公众号通知配置
        :param form_id:
        :param method:
        :return:
        """
        url = self.config.Url.v1_from_inform.format(formId=form_id)
        response = self.request(url=url, method='GET')
        return response

    def v1_form_remind(self, form_id, config, method='PUT'):
        """
        配置表单公众号通知，仅发布者和管理员可以配置
        :param form_id:
        :param config:
        :param method:
        :return:
        """
        url = self.config.Url.v1_form_id_remind.format(formId=form_id)
        # params = {'config': config}
        response = self.request(url=url, method=method, json=config)
        return response

    def v1_form_remind_get(self, form_id, method='GET'):
        """
        获取表单公众号通知配置
        :param form_id:
        :param method:
        :return:
        """
        url = self.config.Url.v1_form_id_remind.format(formId=form_id)
        response = self.request(url=url, method='GET')
        return response

    def v3_form_id_patch_status(self, form_id, date=None, method='GET'):
        """
        校验用户在当前表单是否可以补卡
        :param form_id:
        :param date: 补卡日期
        :param method:
        :return:
        """
        url = self.config.Url.v3_form_id_patch_status.format(formId=form_id)
        patams = {'date': date}
        response = self.request(url=url, method='GET', params=patams)
        return response

    def v3_form_id_patched_times(self, form_id, methods='GET'):
        """
        获取用户在当前表单的已补卡次数
        :param form_id:
        :param methods:
        :return:
        """
        url = self.config.Url.v3_form_id_patched_times.format(formId=form_id)
        response = self.request(url=url, method='GET')
        return response

    def v1_finish_page_banner(self, method='GET'):
        """
        提交结束页banner配置
        :return:
        """
        url = self.config.Url.v1_finish_page_banner
        response = self.request(url=url, method='GET')
        return response

    def v1_end_forms(self, page_no=1, page_size=20):
        """
        获取已结束表单
        :param page_no:
        :param page_size:
        :return:
        """
        url = self.config.Url.v1_end_forms
        params = {'pageNo': page_no, 'pageSize': page_size}
        response = self.request(url=url, params=params, method='GET')
        return response

    def v1_end_forms_delete(self, method='DELETE'):
        """
        删除所有已结束表单
        :return:
        """
        url = self.config.Url.v1_end_forms_delete
        response = self.request(url=url, method='DELETE')
        return response

    def v1_delete_forms(self, forms, method='PUT'):
        """
        删除所有已结束表单
        :return:
        """
        url = self.config.Url.v1_delete_forms
        data = {'formIds': forms}
        response = self.request(url=url, method='PUT', json=data)
        return response

    def v1_form_id_participant_check(self, form_id, name, date=None, method='GET'):
        """
        根据预设名单名称和日期校验当前用户是够可以报名/补卡
        :param form_id:
        :param date:
        :param name:
        :param method:
        :return:
        """
        url = self.config.Url.v1_form_id_participant_check.format(formId=form_id)
        params = {'name': name, 'date': date}
        response = self.request(url=url, method=method, params=params)
        return response

    def v1_form_id_vote_cid(self, form_id, cid, method='GET'):
        """
        获取投票看板数据
        :param form_id:
        :param cid:题目id
        :param method:
        :return:
        """
        url = self.config.Url.v1_form_id_vote_cid.format(formId=form_id, cid=cid)
        response = self.request(url=url, method=method)
        return response

    def v1_form_id_page_style(self, form_id, show_record_question_title=None, show_flow_status_filter=None,  show_quick_ps_rate_rntrance=None, method='PUT'):
        """
        页面样式配置
        :param form_id:
        :param showRecordQuestionTitle:已提交列表中是否显示题目标题
        :param showFlowStatusFilter:是否显示批改状态标签筛选
        :param showQuickPsRateEntrance:是否显示批图评级按钮
        :param method:
        :return:
        """
        url = self.config.Url.v1_form_id_page_style.format(formId=form_id)
        data = {'showRecordQuestionTitle': show_record_question_title,
             'showFlowStatusFilter': show_flow_status_filter,
             'showQuickPsRateEntrance': show_quick_ps_rate_rntrance}
        response = self.request(url=url, method=method, json=data)
        return response

    def v1_form_id_sign_up_delete(self, form_id, form_data_id, method='DELETE'):
        url = self.config.Url.v1_form_id_sign_up_delete.format(formId=form_id, formDataId=form_data_id)
        response = self.request(url=url,method=method)
        return response

    def v2_export_excel_url(self, form_id, start=None, end=None, r_start=None, r_end=None, method='GET'):
        """
        获取导出excel数据链接地址
        :param form_id:
        :param start:开始时间
        :param end:结束时间
        :param r_start:预约日期筛选开始时间
        :param r_end:预约日期少选结束日期
        :param method:
        :return:
        """
        url = self.config.Url.v2_export_excel_url.format(formId=form_id)
        params = {'startTime': start, 'endTime': end, 'rStartTime': r_start, 'rEndTime': r_end}
        response = self.request(url=url, method=method, params=params)
        return response

    def v2_export_form_ticket(self, form_id, ticket, start=None, end=None, r_start=None, r_end= None, method='GET'):
        """
        导出预设名单接口
        :param form_id:
        :param ticket:导出凭证
        :param method:
        :return:
        """
        url = self.config.Url.v2_export_form_ticket.format(formId=form_id)
        params = {'ticket': ticket, 'startTime': start, 'endTime': end, 'rStartTime': r_start, 'rEndTime':r_end}
        response = self.request(url=url, method=method, params=params)
        return response

    def v1_export_attachment_url(self, form_id, start=None, end=None, r_start=None, r_end=None, method='GET'):
        """
        导出附件链接地址
        :param form_id:
        :param start: 开始日期
        :param end: 结束日期
        :param r_start: 预约开始日期
        :param r_end: 预约结束日期
        :param method:
        :return:
        """
        url = self.config.Url.v1_export_attachment_url.format(formId=form_id)
        params = {'startTime': start, 'endTime': end, 'rStartTime': r_start, 'rEndTime': r_end}
        response = self.request(url=url, method=method, params=params)
        return response

    def v1_export_attachment_ticket(self, form_id, ticket, start=None, end=None, r_start=None, r_end=None, method='GET'):
        """
        导出附件接口
        :param form_id:
        :param ticket:导出凭证
        :param start:开始日期
        :param end:结束日期
        :param r_start:预约开始日期
        :param r_end:预约结束日期
        :param method:
        :return:
        """
        url = self.config.Url.v1_export_attachment_ticket.format(formId=form_id)
        params = {'ticket': ticket, 'startTime': start, 'endTime': end, 'rStartTime': r_start, 'rEndTime': r_end}
        response = self.request(url=url, method=method, params=params)
        return response

    def user_export_times(self, form_id, user_id, export_type, method='GET'):
        """
        校验用户是否拥有导出次数
        :param form_id: 表单ID
        :param user_id: 用户ID
        :param export_type: 导出类型（带图excel:1;纯文本excel：2；附件包：3）
        :param method:
        :return:
        """
        url = self.config.Url.user_export_times
        params = {'formId': form_id, 'userId': user_id, 'exportType': export_type}
        response = self.request(url=url, method=method, params=params)
        return response

    def user_add_export_times(self, form_id, user_id, export_type, method='POST'):
        """
        每日新增额外导出次数
        :param form_id: 表单id
        :param user_id: 用户id
        :param export_type: 导出类型（(带图excel:1;纯文本excel：2；附件包：3）
        :param method:
        :return:
        """
        url = self.config.Url.user_add_export_times
        data = {'formId': form_id, 'userId': user_id, 'exportType': export_type}
        response = self.request(url=url, method=method, json=data)
        return response

    def user_get_export_times(self, form_id, method='GET'):
        """
        获取用户所有类型的导出剩余次数
        :param form_id:表单id
        :return:
        """
        url = self.config.Url.user_get_export_times
        params = {'formId': form_id}
        response = self.request(url=url, method=method, params=params)
        return response

    def v1_form_like(self, form_id, form_data_id, like, method='PUT'):
        """
        报名数据点赞/取消点赞
        :param form_id: 表单id
        :param form_data_id: 报名数据id
        :param like:1: 点赞, 0: 取消点赞
        :return:
        """
        url = self.config.Url.v1_form_like.format(formId=form_id, formDataId=form_data_id)
        params = {'like': like}
        response = self.request(url=url, method=method, params=params)
        return response

    def v1_form_comment_post(self, form_id, form_data_id, author='年', type='TEXT', value='22223333', method='POST'):
        """
        新增评论
        :param form_id:表单id
        :param form_data_id:报名数据id
        :param author:评论人
        :param type:TEXT
        :param value:评论内容
        :return:
        """
        url = self.config.Url.v1_form_comment_post.format(formId=form_id, formDataId=form_data_id)
        data = {
            "authorName": author,
            "content": [{
                "type": type,
                "value": value
            }]
        }
        response = self.request(url=url, method=method, json=data)
        return response

    def v1_form_comment_delete(self,form_id, form_data_id, fid, method='DELETE'):
        """
        删除报名评论数据
        :param form_id:
        :param form_data_id:
        :param fid 评论id
        :param method:
        :return:
        """
        url = self.config.Url.v1_form_comment_delete.format(formId=form_id, formDataId=form_data_id)
        params = {'fid': fid}
        response = self.request(url=url, method=method, params=params)
        return response

    def v1_form_last_comment(self, form_id, method='GET'):
        """
        获取用户对某个表单的最后一条评论
        :param form_id:
        :return:
        """
        url = self.config.Url.v1_form_last_comment.format(formId=form_id)
        response = self.request(url=url, method=method)
        return response

    def v1_form_comment_page_get(self, form_id, form_data_id, page_no=1, page_size=20, method='GET'):
        """
        分页获取评论数据
        :param form_id:
        :param form_data_id:
        :param page_no: 页码
        :param page_size: 每页记录数
        :return:
        """
        url = self.config.Url.v1_form_comment_page_get.format(formId=form_id, formDataId=form_data_id)
        params = {'pageNo': page_no, 'pageSize': page_size}
        response = self.request(url=url, method=method, params=params)
        return response

    def v3_like_comment_rate_remark(self, form_id, fid, comment=True, like=True, rate=True, remark=True, method='POST'):
        """
        获取点赞评论接口
        :param form_id:
        :param form_data_id:
        :param query:
        :param mrthod:
        :return:
        """
        url = self.config.Url.v3_like_comment_rate_remark.format(formId=form_id)
        data = [{'fid': fid, 'comment': comment, 'like': like, 'rate': rate, 'remark': remark}]
        response = self.request(url=url, method=method, json=data)
        return response

    def v1_form_rate_config_get(self, form_id, method='GET'):
        """
        获取评级配置
        :param form_id:
        :param method:
        :return:
        """
        url = self.config.Url.v1_form_rate_config.format(formId=form_id)
        response = self.request(url=url, method=method)
        return response

    def v1_form_rate_config_post(self, form_id, rate, method='POST'):
        """
        创建评级配置
        :param form_id:
        :param rate: 评级配置
        :param method:
        :return:
        """
        url = self.config.Url.v1_form_rate_config.format(formId=form_id)
        data = [
            {"value": rate}]
        response = self.request(url=url, method=method, json=data)
        return response

    def v1_form_rate_config_put(self, form_id, version, rid, value, method='PUT'):
        """
        修改评级配置
        :param form_id: 表单id
        :param version: 版本号
        :param rid: 配置项id，新增没有不传
        :param value: 配置值
        :param method:
        :return:
        """
        url = self.config.Url.v1_form_rate_config.format(formId=form_id)
        data = {
            "version": version,
            "items":
                [{
                    "rid": rid,
                    "value": value
                }]}
        response = self.request(url=url, method=method, json=data)
        return response

    def v1_form_rate(self, form_id, form_data_id, rid, version, method='POST'):
        """
        对报名数据进行评级
        :param form_id:
        :param form_data_id:
        :param rid:
        :param version:
        :param method:
        :return:
        """
        url = self.config.Url.v1_form_rate.format(formId=form_id, formDataId=form_data_id)
        data = {"rid": rid, "version": version}
        response = self.request(url=url, method=method, json=data)
        return response

    def v1_overt_form_list(self, page_no=1, method='GET'):
        """
        获取首页公开表单列表
        :param page_no: 分页页号
        :param method:
        :return:
        """
        url = self.config.Url.v1_overt_form_list
        params = {'pageNo': page_no}
        response = self.request(url=url, params=params, method=method)
        return response

    def v1_name_used(self, form_id, date=None, method='GET'):
        """
        获取表单预设名单中各名单的报名状态
        :param form_id: 表单id
        :param date: 日期
        :param method:
        :return:
        """
        url = self.config.Url.v1_name_used.format(formId=form_id)
        params = {'date': date}
        response = self.request(url=url, params=params, method=method)
        return response

    def v1_name_order_used(self, form_id, date=None, method='GET'):
        """
        按预设名单顺序获取表单中开启的预设名单报名状态
        :param form_id: 表单id
        :param date:周期id
        :param method:
        :return:
        """
        url = self.config.Url.v1_name_order_used.format(formId=form_id)
        params = {'date': date}
        response = self.request(url=url, params=params, method=method)
        return response

    def v1_name_form_data_list(self, form_id, name, page_no, page_size, method='GET'):
        """
        预设名单详情列表
        :param form_id:表单id
        :param name:点击的姓名
        :param page_no:
        :param page_size:
        :param method:
        :return:
        """
        url = self.config.Url.v1_name_form_data_list.format(formId=form_id)
        params = {'name': name, 'pageNo': page_no, 'pageSize': page_size}
        response = self.request(url=url, params=params, method=method)
        return response

    def v1_form_name_list_template(self, name_list, method='POST'):
        """
        保存/更新预设名单模板
        :param name_list:预设名单
        :param method:put/post
        :return:
        """
        url = self.config.Url.v1_form_name_list_template
        response = self.request(url=url, json=name_list, method=method)
        return response

    def v1_form_name_list_template_delete(self, nlid, method='DELETE'):
        """
        删除预设名单模板
        :param nlid:
        :param method:
        :return:
        """
        url = self.config.Url.v1_form_name_list_template
        params = {'nlid': nlid}
        response = self.request(url=url, params=params, method=method)
        return response

    def v1_form_name_list_template_get(self, method='GET'):
        """
        获取预设名单模板列表
        :param method:
        :return:
        """
        url = self.config.Url.v1_form_name_list_template
        response = self.request(url=url, method=method)
        return response

    def v1_name_list_form_datas(self, form_id, name, page_no=1, page_size=10, method='GET'):
        """
        根据预设名单名字查询报名数据
        :param form_id: 表单id
        :param name: 姓名
        :param page_no:
        :param page_size:
        :param method:
        :return:
        """
        url = self.config.Url.v1_name_list_form_datas.format(formId=form_id)
        params = {'name': name, 'pageNo': page_no, 'pageSize': page_size}
        response = self.request(url=url, params=params, method=method)
        return response

    def v1_name_list_not_filled(self,form_id, date=None, method='GET'):
        """
        预设名单未填写名单列表
        :param method:
        :return:
        """
        url = self.config.Url.v1_name_list_not_filled.format(formId=form_id)
        params = {'date': date}
        response = self.request(url=url, params=params, method=method)
        return response

    def v1_name_list_filled_notify(self, form_id, date=None, method='GET'):
        """
        一键通知未填人员
        :param form_id: 表单id
        :param date: 日期
        :param method:
        :return:
        """
        url = self.config.Url.v1_name_list_filled_notify.format(formId=form_id)
        params = {'date': date}
        response = self.request(url=url, params=params, method=method)
        return response

    def v1_storage_space_regular_tips_ack(self, method='PUT'):
        """
        老用户空间限制提醒弹窗确认
        :param method:
        :return:
        """
        url = self.config.Url.v1_storage_space_regular_tips_ack
        response = self.request(url=url, method=method)
        return response

    def v1_storage_space_status(self, method='GET'):
        """
        获取当前用户的存储空间使用状态
        :param method:
        :return:
        """
        url = self.config.Url.v1_storage_space_status
        response = self.request(url=url, method=method)
        return response

    def v1_form_data_delete(self, form_id, form_data_id, method='POST'):
        """
        报名数据清理
        :param form_id:表单id
        :param form_data_id: 报名数据id
        :param method:
        :return:
        """
        url = self.config.Url.v1_form_data_delete.format(formId=form_id)
        data = {"formDataIds": [form_data_id]}
        response = self.request(url=url, json=data, method=method)
        return response

    def v1_recycle_forms(self, page_no=1, page_size=20, method='GET'):
        """
        回收站列表
        :param page_no:
        :param page_size:
        :param method:
        :return:
        """
        url = self.config.Url.v1_recycle_forms
        params = {'pageNo': page_no, 'pageSize': page_size}
        response = self.request(url=url, params=params, method=method)
        return response

    def v1_recycle_form(self, form_id, method='POST'):
        """
        删除回收站/恢复回收站
        :param form_id:
        :param method:post/put
        :return:
        """
        url = self.config.Url.v1_recycle_form
        data = {"formIds": [form_id]}
        response = self.request(url=url, json=data, method=method)
        return response

    def v1_recycle_form_all(self, method='PUT'):
        """
        回收站一键恢复/回收站一键删除
        :param method:put/delete
        :return:
        """
        url = self.config.Url.v1_recycle_form_all
        response = self.request(url=url, method=method)
        return response

    def v1_delete_form_data_dete(self, form_id, start, end, method='DELETE'):
        """
        按日期批量硬删除报名数据
        :param form_id:表单id
        :param start: 开始日期
        :param end: 结束日期
        :param method:
        :return:
        """
        url = self.config.Url.v1_delete_form_data_dete.format(formId=form_id)
        params = {'startTime': start, 'endTime': end}
        response = self.request(url=url, params=params, method=method)
        return response

    def v1_date_count(self, form_id, start, end, method='GET'):
        """
        按日期查询报名数据条数
        :param form_id: 表单id
        :param start: 开始日期
        :param end: 结束日期
        :param method:
        :return:
        """
        url = self.config.Url.v1_date_count.format(formId=form_id)
        params = {'startTime': start, 'endTime': end}
        response = self.request(url=url, params=params, method=method)
        return response

    def v1_open_api_sign_up_developer(self, phone, method='POST'):
        """
        注册开发者
        :param phone: 手机号
        :param method:
        :return:
        """
        url = self.config.Url.v1_open_api_sign_up_developer
        data = {"phone": phone}
        response = self.request(url=url, json=data, method=method)
        return response

    def v1_developer(self, method='GET'):
        """
        获取开发者信息
        :return:
        """
        url = self.config.Url.v1_developer
        response = self.request(url=url, method=method)
        return response

    def wx_mp_link(self,method="GET"):
        """
        获取全部公众号链接配置
        :return:
        """
        url = self.config.Url.wx_mp_link
        response = self.request(url=url, method=method)
        return response

    # 群组相关
    def v1_group(self, name, type, method='POST'):
        """
        新增群组
        :param name: 群组名称
        :param type: 群组类型
        :param method:
        :return:
        """
        url = self.config.Url.v1_group
        data = {'groupName': name, 'groupType': type}
        response = self.request(url=url, json=data, method=method)
        return response

    def v1_get_group_member(self, group_id, page_no=1, method='GET'):
        """
        获取群组成员列表
        :param group_id: 群组id
        :param page_no: 页码
        :param method:
        :return:
        """
        url = self.config.Url.v1_group_member.format(groupId=group_id)
        params = {"pageNo": page_no}
        response = self.request(url=url, params=params, method=method)
        return response

    def v1_group_operate_put(self, id, name, type, method='PUT'):
        """
        修改群组
        :param id: 群组id
        :param name: 群组name
        :param type: 群组type
        :param method:
        :return:
        """
        url = self.config.Url.v1_group_operate.format(groupId=id)
        data = {'groupName': name, 'groupType': type}
        response = self.request(url=url, json=data, method=method)
        return response


    def v1_group_operate(self, id, method='GET'):
        """
        获取群组详细信息/删除群组
        :param id: 群组id
        :param method:GET/DELETE
        :return:
        """
        url = self.config.Url.v1_group_operate.format(groupId=id)
        response = self.request(url=url, method=method)
        return response

    def v1_delete_group_member(self, id, fuid, method='DELETE'):
        """
        移除群组成员
        :param id: 群组id
        :param fuid: 被移除成员fuid
        :param method:
        :return:
        """
        url = self.config.Url.v1_group_member.format(groupId=id)
        params = {'targetFuid': fuid}
        response = self.request(url=url, params=params, method=method)
        return response

    def v1_group_list(self, no=1, size=20, method='GET'):
        """
        个人群组列表
        :param no:
        :param size:
        :param method:
        :return:
        """
        url = self.config.Url.v1_group_list
        params = {'pageNo': no, "pageSize": size}
        response = self.request(url=url, params=params, method=method)
        return response

    def v1_group_forms(self, id, size=10, last_form_id='',method='GET'):
        """
        群组内表单列表
        :param id:群组id
        :param size:
        :param last_form_id:
        :param method:
        :return:
        """
        url = self.config.Url.v1_group_forms.format(groupId=id)
        params = {'pageSize': size, 'lastFormId': last_form_id}
        response = self.request(url=url, params=params, method=method)
        return response

    def v1_add_admin(self, id, fuid, method='POST'):
        """
        增加超级管理员
        :param id: 群组id
        :param fuid: 被加管理员fuid
        :param method:
        :return:
        """
        url = self.config.Url.v1_group_admin.format(groupId=id)
        data = {"targetFuid": fuid}
        response = self.request(url=url, json=data, method=method)
        return response

    def v1_remove_admin(self, id, fuid, method='DELETE'):
        """
        撤除超级管理员
        :param id: 群组id
        :param fuid: 被移除管理员fuid
        :param method:
        :return:
        """
        url = self.config.Url.v1_group_admin.format(groupId=id)
        params = {"targetFuid": fuid}
        response = self.request(url=url, params=params, method=method)
        return response

    def v1_group_invite(self, id, method='GET'):
        """
        生成群组邀请码
        :param id:群组id
        :param method:
        :return:
        """
        url = self.config.Url.v1_group_invite.format(groupId=id)
        response = self.request(url=url, method=method)
        return response

    def v1_join_group(self, id, pwd, method='POST'):
        """
        用户加入群组
        :param id: 群组id
        :param pwd:
        :param method:
        :return:
        """
        url = self.config.Url.v1_join_group.format(groupId=id)
        data = {'invitePassword': pwd}
        response = self.request(url=url, json=data, method=method)
        return response

    def v1_quit_group(self, id, method='POST'):
        """
        用户退出群组
        :param id: 群组id
        :param method:
        :return:
        """
        url = self.config.Url.v1_quit_group.format(groupId=id)
        response = self.request(url=url, method=method)
        return response

    def v1_wx_advertise(self,method='GET'):
        """
        流量主广告配置
        :param method:
        :return:
        """
        url = self.config.Url.v1_wx_advertise
        response = self.request(url=url,method=method)
        return response






if __name__ == '__main__':
    os.environ['env'] = 'test'
    api = FormApi(fuid='1072705609905737732', print_results=True)  # 1056011177739419657   1072705609905737732
    # api.v1_group_forms('1414696509808533505')
    # api.v1_remove_admin('1414696509808533505','1056011177739419657')
    # api.v1_group_invite('1414696509808533505')
    # api.v1_quit_group('1414696509808533505')
    api.oss_request('1')
    # api.v1_group('putong1','ORDINARY_GROUP')
    # api.v1_group_operate('1414701649106001921','DELETE')
    # api.v1_delete_group_member('1414696509808533505', '1056011177739419657')
    # api.v1_group_list()
    # api.v1_group_operate_put('1414701649106001921','bumenqun','SECTORAL_GROUP')
    # data =  {"templateName":"测试1","originData":"1\n2\n3\n4\n5","value":[{"name":"1"},{"name":"2"},{"name":"3"},{"name":"4"},{"name":"5"}]}
    # api.v1_date_count('1402424183579213824', '20230101', '20230117')
    # api.v1_templates()
    # api.v1_name_order_used('1399571737637724160')
    # api.v1_form_rate_config_get('1402424183579213824')
    # api.v1_form_comment_delete('1402424183579213824', '1402424243989774336', '1402812279739678720')
    # api.v1_form_comment_post('1402424183579213824', '1402424243989774336')
    # api.user_get_export_times('1402424183579213824')
    # api.user_add_export_times('1402424183579213824', '1072705609905737732', '3')
    # api.v1_export_attachment_url('1402424183579213824')
    # api.v1_form_id_sign_up_delete('1402424183579213824', '1402424243989774336')
    # api.v1_form_id_page_style('1402424183579213824', 'true', 'false', 'true')
    # api.v1_form_id_vote_cid('1402424183579213824', '1402424184908808193')
    # api.v1_form_data_owner('1384304617603624961','1','20')
    # api.v3_form_id_patched_times('1399845645831200769')
    # api.v3_form_id_patch_status('1392584316372353024', '20230110')
    # api.v1_finish_page_banner()
    # api.v1_end_forms()
    # api.v1_end_forms_delete()
    # data = {'formIds': ['1401769529656729600', '1401767851578613760']}
    # data = ['1401769529656729600', '1401767851578613760']
    # api.v1_delete_forms(data)
    # api.v1_form_id_participant_check('1399571737637724160', "张三", '20230110')
    # api.v1_operation_forms(params={'tabId': "TUTORIAL_HELP"})
    # api.v1_operation_forms("TUTORIAL_HELP")
    # api.v1_complaint(form_id='1111513741679136768',reason=1,description="123",images=["https://oss.feidee.cn/oss/form_eb4a07ec97d6a07d_800X698.jpg",'https://oss.feidee.cn/oss/form_6b8754320b6ea286_495X401.gif','https://oss.feidee.cn/oss/form_927aaca78713bbaa_500X500.jpg','https://oss.feidee.cn/oss/form_2d89ac01d6d5d00b_500X500.jpg'],contact='')
    # api.v1_templates_lit("STATISTIC")
    # api.v1_form_operation_template_operation_form_id(1082098651125252096)
    # api.v3_form_id_form_datas(form_id='1116127305559703552')
    # api.v1_from_catalog('1384304617603624961')
    # api.v1_manager_froms(params={"pageNo":'1', "pageSize":'20'})
#     data ={
#   "addition": "true",
#   "modify": "true",
#   "cancel": "true",
#   "comment": "true"
# }
#     config={
#   "active": "true",
#   "sunday": "1",
#   "monday": "1",
#   "tuesday": "1",
#   "wednesday": "1",
#   "thursday": "1",
#   "friday": "1",
#   "saturday": "1",
#   "timeOfDay": "1"
# }
    # api.v1_form_inform(form_id='1382804799016534017', config=data)
    # api.v1_form_inform_get(form_id='1382804799016534017')
    # v1_form_remind
    # api.v1_form_remind(form_id='1382804799016534017', config=config)
    # api.v1_form_remind_get(form_id='1382804799016534017')
    # api.v1_form_operation_operation_operation_form_id(1070883234922893333)
    # api.v1_statistic_analysis_form_id(1076668355504508928)
    # api.v1_statistic_detail_form_id(1076668355504508928, 'SEQUENCE', 'ASC')
    # api.v1_form_manager_invitation_code('1096160988106854400')
    # api.v1_form_manager("qGi0hzg61tZ", "qGR7KszGt6X")  #  qGFo6gsBAfq,qG1WtaHbCAr
    # api.v1_form_managers_form_id('1088295026292690945')
    # api.v1_form_operation_official_account_form_id('1098016190908858368')
    # api.v1_operation_position(10140)
    # data = {"fid":"","catalogs":[{"type":"IMAGE","cid":"1108938171552370688","value":["https://oss.feidee.cn/oss/form_7f6e187cc2487381_750X1334.jpg","https://oss.feidee.cn/oss/form_a1603bd4869b6699_750X1334.jpg","https://oss.feidee.cn/oss/form_86b27c686e0a7d6b_750X1334.jpg"]}],"formVersion":3}
    # api.v2_form_id_form_data(form_id='1108938171535593472', data=data, method='POST')

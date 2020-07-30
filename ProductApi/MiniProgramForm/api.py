#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File   : api.py
# @Author : mocobk
# @Email  : mailmzb@qq.com
# @Time   : 2019/1/22 9:53
import os
import mimetypes
import threading

import jmespath
import requests

from ProductApi.MiniProgramForm import config
from ProductApi.base import ApiBase, Response


class SingletonMetaClass(type):
    _instance_lock = threading.Lock()  # 支持多线程的单例模式
    _instance = {}

    def __call__(cls, *args, **kwargs):
        """"
        元类实现 FormApi 单例模式，避免同一个账号被实例化多次，导致多次请求登录接口
        没有用 def __new__(cls, *args, **kwargs) 方式实现单例，因为 __new__ 不返回一个对象,
        它返回一个在其后调用__init__的单元化对象，即虽然是单例，但每次都会调用 __init__,如下：
        a = A() 实际上是 a = A.__new__(A) 和 a.__init__()
        """
        fuid = args[0] if args else kwargs.get('fuid') or config.UserFuid.mocobk
        if not cls._instance.get(fuid):
            with cls._instance_lock:
                if not cls._instance.get(fuid):
                    cls._instance[fuid] = super().__call__(*args, **kwargs)

        return cls._instance[fuid]


class FormApi(ApiBase, metaclass=SingletonMetaClass):
    USER = config.UserFuid

    def __init__(self, fuid=config.UserFuid.mocobk, print_results=False):
        """
        :param fuid: 用户群报数 id, 不传则使用配置中默认的
        """
        super().__init__(print_results)
        self.config: config.Test = getattr(config, self.env.name)
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
        response = super().request(url=self.config.Url.v1_login_test, method='POST', json=data)
        self.set_logger_on()

        if response.status_code != 200:
            raise Exception('登陆失败！请检查环境和账号')
        return {'Authorization': response.data.get('data', {}).get('token', '')}

    def request(self, method, url,
                params=None, data=None, json=None, headers: dict = None, cookies=None, files=None,
                auth=None, timeout=None, allow_redirects=True, proxies=None,
                hooks=None, stream=None, verify=None, cert=None, need_auth=True) -> Response:
        """
        need_auth:  是否需要鉴权， 服务端这边对于不需要鉴权的但传
        :return:
        """
        headers = {**headers, **self.authorized_hearders} if headers else self.authorized_hearders
        response = super().request(method, url, params, data, json, headers, cookies, files, auth, timeout,
                                   allow_redirects, proxies, hooks, stream, verify, cert)
        if response.status_code == 401:
            self.logger.info('登录 token 过期，重新登录中...')
            self.authorized_hearders = self.get_authorized_hearders()
            if self.authorized_hearders:
                self.logger.info(f'登录中成功，重试请求：{response.request.url}')
                response = super().request(method, url, params, data, json, headers, cookies, files, auth, timeout,
                                           allow_redirects, proxies, hooks, stream, verify, cert)

        return response

    def v1_creation_forms(self, params):
        """
        Name: 我创建的表单列表
        """
        url = self.config.Url.v1_creation_forms
        response = self.request(url=url, method='GET', params=params)
        return response

    def v1_examples(self):
        """
        Name: 我创建的表单列表
        """
        url = self.config.Url.v1_examples
        response = self.request(url=url, method='GET')
        return response

    def v1_image(self, image: str):
        """
        Name: 上传图片
        file: 可以是本地文件路径，也可以是 url
        """
        url = self.config.Url.v1_image
        if image.startswith('http'):
            try:
                res = requests.get(image, timeout=120)
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
        response = self.request(url=url, method='POST', files=files)
        return response

    def v1_form(self, data, return_form_id=False):
        """创建表单接口不支持返回新创建的表单 id， 这里通过获取创建表单列表拿到最新创建的表单 id"""
        url = self.config.Url.v1_form
        response = self.request(url=url, method='POST', json=data)
        if return_form_id:
            creation_forms = self.v1_creation_forms({'pageNo': 1, 'pageSize': 5})
            if creation_forms.status_code != 200:
                raise Exception('创建表单后获取表单 id 失败')
            form_ids = jmespath.search('@.data.creations.*[*].formId[]', creation_forms.data)
            response.form_id = form_ids[0]
        return response

    def v1_form_form_id_get(self, form_id):
        url = self.config.Url.v1_form_form_id.format(formId=form_id)
        response = self.request(url=url, method='GET')
        return response


if __name__ == '__main__':
    os.environ['env'] = 'test'
    api = FormApi(fuid='1026957780256297009', print_results=True)
    api.v1_creation_forms(params={'pageNo': 1, 'pageSize': 50})
    api.v1_examples()

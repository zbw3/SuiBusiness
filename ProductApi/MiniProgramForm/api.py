#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File   : api.py
# @Author : mocobk
# @Email  : mailmzb@qq.com
# @Time   : 2019/1/22 9:53
import mimetypes

import requests

from ProductApi.MiniProgramForm import config
from ProductApi.base import ApiBase, Response


class FormApi(ApiBase):
    USER = config.UserFuid

    def __init__(self, fuid=None, print_results=False):
        """
        :param fuid: 用户群报数 id, 不传则使用配置中默认的
        """
        super().__init__(print_results)
        self.config: config.Test = getattr(config, self.env.name)
        self.fuid = fuid or self.config.DUFAULT_FUID
        self.authorized_hearders = self.get_authorized_hearders()

    def get_authorized_hearders(self) -> dict:
        """
        TODO: 待实现, 登录失败直接抛出异常
        """
        url = self.config.HOSTNAME + self.config.Url.v1_login_test
        data = {
            "appId": self.config.APP_ID,
            "fuid": self.fuid
        }
        self.set_logger_off()
        self.logger.info('正在登陆...')
        response = super().request(url=url, method='POST', json=data)
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
        if isinstance(url, str):
            url = self.config.HOSTNAME + url
        elif isinstance(url, (tuple, list)):
            url = ''.join(url)

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

        if response.elapsed.total_seconds() > 5:
            raise Exception('接口请求响应时间超过 5s 了，请及时检查')
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
            res = requests.get(image, stream=True)
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

    def v1_form(self, data):
        url = self.config.Url.v1_form
        response = self.request(url=url, method='POST', json=data)
        return response


if __name__ == '__main__':
    import os

    os.environ['env'] = 'production'
    api = FormApi(fuid='1026957780256297009', print_results=True)
    api.v1_creation_forms(params={'pageNo': 1, 'pageSize': 50})
    api.v1_examples()

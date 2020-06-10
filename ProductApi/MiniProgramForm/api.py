#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File   : api.py
# @Author : mocobk
# @Email  : mailmzb@qq.com
# @Time   : 2019/1/22 9:53
from ProductApi.MiniProgramForm import config
from ProductApi.base import ApiBase, Response


class FormApi(ApiBase):

    def __init__(self, fuid, print_results=False):
        """
        :param fuid: 用户群报数 id
        """
        self.config: config.Test = getattr(config, self.env.name)
        self.fuid = fuid
        self.authorized_hearders = self.get_authorized_hearders()
        super().__init__(print_results)

    def get_authorized_hearders(self) -> dict:
        """
        TODO: 待实现, 登录失败直接抛出异常
        """
        # self.fuid
        return {'Authorization': '330ebabccd6b19ad3738776f50a5081944e1dfcfa6698fd2caa04585a07a994b'}

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
        self.authorized_hearders = {}
        url = self.config.Url.v1_examples
        response = self.request(url=url, method='GET')
        return response


if __name__ == '__main__':
    import os
    os.environ['env'] = 'uat'
    api = FormApi(fuid='123', print_results=True)
    # api.v1_creation_forms(params={'pageNo': 1, 'pageSize': 50})
    api.v1_examples()

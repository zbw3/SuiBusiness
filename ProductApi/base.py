#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File   : base.py.py
# @Author : mocobk
# @Email  : mailmzb@qq.com
# @Time   : 2019/12/23 16:51
import json
from collections import namedtuple
from json import JSONDecodeError

import requests

from libs.CryptoUtils import Crypto
from settings.BaseConfig import AuthSchema, Logger

api_response = namedtuple('ApiResponse',
                          ['url', 'text', 'data', 'status_code', 'request', 'cookies', 'headers', 'response'])


class ApiBase(Logger):

    def __init__(self, print_results=True):
        self.print_results = print_results

    @staticmethod
    def _print(data):
        if isinstance(data, str):
            try:
                data = json.loads(data)
            except JSONDecodeError:
                print(data)
        print(json.dumps(data, ensure_ascii=False, sort_keys=True))

    def dict_to_auth(self, dict_obj):
        return AuthSchema(**dict_obj)

    def request(self, url, method, **kwargs):
        """
        :return: requests.response object but with data property
        """
        self.logger.debug('请求方法：%s', method)
        self.logger.debug('请求参数：%s', kwargs.get('params') or kwargs.get('data') or kwargs.get('json'))
        response = requests.request(method, url, **kwargs)
        self.logger.debug('请求 URL：%s', response.request.url)
        self.logger.debug('HTTP状态码：%s', response.status_code)
        self.logger.debug('请求消耗时间：%s s', response.elapsed.total_seconds())
        try:
            data = response.json()
        except JSONDecodeError:
            self.logger.warn('response is not json!')
            data = response.text
        # 因为大部分接口返回的 Json, 这里为了方便，加入了 data 属性
        return api_response(response.url, response.text, data, response.status_code, response.request,
                            response.cookies, response.headers, response)


class OperatorApiBase(ApiBase):
    crypto = Crypto()

    def gen_request_data(self, logon_encrypt, auth):
        return {'iv': auth.iv, 'cooperatorToken': auth.token, 'encryptType': 1,
                'logon': logon_encrypt}

    def api_common(self, url, api_name='', method='POST', logon_params=None,
                   auth=None, encrypt=None, decrypt=None, **kwargs):

        self.logger.info(f"{api_name}：{url}")
        self.logger.debug(f'原始参数：{logon_params}')

        if callable(encrypt):
            # 驭信接口通用请求方式
            logon_encrypt = encrypt(logon_params, auth.key, auth.iv)
            request_data = self.gen_request_data(logon_encrypt, auth)
            response = self.request(url, method=method, data=request_data, **kwargs)

            if response.status_code in [404, 500]:
                raise AssertionError(f'response_code={response.status_code}')

            if response.data.get('data') and callable(decrypt):
                response.data['data'] = decrypt(response.data['data'], auth.key, auth.iv)
            if self.print_results:
                self._print(response.data)
            return response


class EBankApiBase(OperatorApiBase):
    def gen_request_data(self, logon_encrypt, auth):
        return {'iv': auth.iv, 'token': auth.token, 'encryptType': 1,
                'logon': logon_encrypt}

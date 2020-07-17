#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File   : base.py.py
# @Author : mocobk
# @Email  : mailmzb@qq.com
# @Time   : 2019/12/23 16:51

from json import JSONDecodeError
from urllib.parse import urljoin

import requests
from requests import Response as _Response

from settings.BaseConfig import Logger, API_LOGGER_LEVEL, Env


class Response(_Response):
    data = None


class ApiBase(Logger):

    def __init__(self, config, print_results=False):
        self.config = config
        self.print_results = print_results
        super().__init__(logger_name='ApiLogger', level=API_LOGGER_LEVEL)
        self.session = requests.Session()

    @property
    def env(self):
        return Env().cur_env

    def request(self, method, url,
                params=None, data=None, json=None, headers=None, cookies=None, files=None,
                auth=None, timeout=None, allow_redirects=True, proxies=None,
                hooks=None, stream=None, verify=None, cert=None) -> Response:
        """
        :return: requests.response object but with data property
        """
        # url 如果是 path ，则加上 HOSTNAME
        if isinstance(url, str) and not url.startswith('http'):
            url = urljoin(self.config.HOSTNAME, url)

        response = self.session.request(method=method, url=url, params=params, data=data, json=json, headers=headers,
                                        cookies=cookies, files=files,
                                        auth=auth, timeout=timeout, allow_redirects=allow_redirects, proxies=proxies,
                                        hooks=hooks, stream=stream, verify=verify, cert=cert)

        self.logger.debug('%s %s', response.request.method, response.request.url)
        self.logger.debug('请求参数：%s', params or data or json)
        self.logger.debug('HTTP状态码：%s', response.status_code)
        self.logger.debug('请求消耗时间：%s s', response.elapsed.total_seconds())
        if self.print_results:
            if self.logger.level != self.DEBUG:
                self.logger.info('%s %s', response.request.method, response.request.url)
            print(response.text)

        # 因为大部分接口返回的 Json, 这里为了方便，加入了 data 属性
        try:
            data = response.json()
        except JSONDecodeError:
            self.logger.warning('响应非 json 结构!')
            data = None
        response.data = data
        return response

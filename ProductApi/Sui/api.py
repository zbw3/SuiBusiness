#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File : login_api.py
# @Author: GoGo
# @Date : 2020/3/19
# @Desc :
import hashlib
from urllib.parse import urlparse

from requests.exceptions import HTTPError

from ProductApi.Sui import config
from ProductApi.base import ApiBase
from libs.Database import Redis
from settings.BaseConfig import SuiConfig


class Sui(ApiBase):

    def __init__(self, username, password, output_log=False):
        self.username = username
        self.password = password
        self.config: config.Test = getattr(config, self.env.name)
        super().__init__()
        if not output_log:
            self.logger.setLevel(self.ERROR)

    @property
    def token(self):
        return self.get_token()

    def sha1_hex(self, text):
        """使用sha1加密，返回加密后的16进制字符串"""
        return hashlib.sha1(text.encode('utf-8')).hexdigest()

    def login_from_oauth2(self):
        """模拟从 App终端登录获取 token"""
        headers = SuiConfig.HEADERS
        headers["Host"] = urlparse(self.config.Url.v2_oauth2_authorize).hostname
        params = {
            "encode_version": "v2",
            "username": self.username,
            "scope": "MyMoney",
            "grant_type": "password",
            "password": SuiConfig.PASSWORD.get(self.password)
        }
        url = self.config.Url.v2_oauth2_authorize
        response = self.request(url=url, method='GET', params=params, headers=headers)
        return response.data

    def login_from_web(self):
        """模拟从 web 端登录获取 token"""
        params = {'opt': 'vccode'}
        response = self.request(url=self.config.Url.login_do, method='GET', params=params)
        data = response.json()
        vccode, uid = data.get('vccode'), data.get('uid')
        if not vccode:
            raise HTTPError(f'vccode 获取失败，请检查接口：{response.request.url} -> {response.text}')

        password = self.sha1_hex(self.password)
        password = self.sha1_hex(self.username + password)
        password = self.sha1_hex(password + vccode)

        params = {
            'email': self.username,
            'status': '0',
            'password': password,
            'uid': uid,
        }
        response = self.request(url=self.config.Url.login_do, method='GET', params=params)
        if response.json().get('status') != 'ok':
            raise HTTPError(f'登录 cookie 获取失败，请检查账号或密码是否正确：{response.request.url} -> {response.text}')
        response = self.request(url=self.config.Url.auth, method='GET', headers=self.config.Header.AUTH_HEADERS)
        return response.data

    def user_profile(self, token=None):
        url = self.config.Url.v1_profile
        token = token or self.token
        headers = self.config.Header.AUTH_HEADERS
        headers["Authorization"] = f"Bearer {token}"
        headers["Device"] = '{}'
        response = self.request(url=url, method='GET', headers=headers)
        return response.data

    def is_valid_token(self, token):
        data = self.user_profile(token)
        return bool(data.get('uid'))

    def get_token(self, update_token=False):
        redis = Redis()
        token = redis.get_token(self.username)
        if not token or update_token:
            self.logger.info('更新 token 中...')
            # token = self.login_from_oauth2().get('access_token')  # aouth2 接口不知道加密方法,暂取消
            token = self.login_from_web().get('object', {}).get('token')
            redis.set_token(self.username, token, expire=3000)
        return token

    def authorized_headers(self):
        """已加入鉴权信息的请求头  'token_type': 'Bearer'"""
        headers = SuiConfig.HEADERS
        headers["Authorization"] = f"Bearer {self.token}"
        return headers


if __name__ == "__main__":
    import os
    os.environ['env'] = 'test'
    sui = Sui(username="13085060818", password="123456")
    _token = sui.get_token(True)
    print('token: ', _token)
    print(sui.user_profile())



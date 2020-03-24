#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File : login_api.py
# @Author: GoGo
# @Date : 2020/3/19
# @Desc :
from urllib.parse import urlparse

from ProductApi.Sui import config
from ProductApi.base import ApiBase
from libs.Database import Redis
from settings.BaseConfig import SuiConfig


class Sui(ApiBase):

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.config: config.Test = getattr(config, self.env.name)
        super().__init__()

    @property
    def token(self):
        return self.get_token()

    def login(self):
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
        return response.json()

    def get_token(self, update_token=False):
        redis = Redis()
        token = redis.get_token(self.username)
        if not token or update_token:
            self.logger.info('更新 token 中...')
            token = self.login().get('access_token')
            redis.set_token(self.username, token, expire=36000)
            return token
        return token


if __name__ == "__main__":
    sui = Sui(username="119@kd.ssj", password="123456")
    login_res = sui.login()
    _token = sui.get_token()
    print(login_res)
    print(_token)

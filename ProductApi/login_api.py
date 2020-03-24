#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File : login_api.py
# @Author: GoGo
# @Date : 2020/3/19
# @Desc :


from settings.SuiConfig import SuiConfig
from ProductApi.base import ApiBase
from libs.Database import TokenRedis


class LoginApi(ApiBase):

    def __init__(self, *args, **kwargs):
        super(LoginApi, self).__init__(*args, **kwargs)
        self.base_url = SuiConfig.SYSTEM_ARGS[self.env.value]["login_url"]
        self.headers = SuiConfig.HEADERS
        self.headers["Host"] = self.base_url.split("//")[-1].split("/")[0]

    def login(self, username="", password="", update_token=False):
        token = None
        try:
            token = TokenRedis().get_redis_token(token_name=f"{username}_token")
            if token is None or update_token:
                url = self.base_url
                method = "GET"
                params = {
                    "encode_version": "v2",
                    "username": username,
                    "scope": "MyMoney",
                    "grant_type": "password",
                    "password": SuiConfig.PASSWORD[password]
                }
                response = self.request(url=url, method=method, params=params, headers=self.headers)
                if response is not None and response.status_code == 200:
                    token = response.data["access_token"]
                    TokenRedis().set_redis_token(f"{username}_token", new_token=token)
        except Exception as e:
            self.logger.error(e)
        return token


if __name__ == "__main__":
    token = LoginApi().login(username="119@kd.ssj", password="123456", update_token=True)
    print(token)

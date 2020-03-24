#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File : v1_store_api.py
# @Author: GoGo
# @Date : 2020/3/20
# @Desc :

from urllib.parse import urljoin
import requests

from settings.SuiConfig import SuiConfig
from ProductApi.login_api import LoginApi


class V1StoreApi(LoginApi):

    def __init__(self, trading_entity="3604098", username="", password="", *args, **kwargs):
        super(V1StoreApi, self).__init__(*args, **kwargs)
        self.base_url = SuiConfig.SYSTEM_ARGS[self.env.value]["business_base_url"]
        self.headers = SuiConfig.HEADERS
        self.headers["Host"] = self.base_url.split("//")[-1].split("/")[0]
        token = self.login(username=username, password=password)
        self.headers["Authorization"] = f"Bearer {token}"
        self.headers["Trading-Entity"] = trading_entity

    def get_v1_store_products_categorys(self):
        """查询商品分类"""
        url = "/v1/store/products/categorys"
        method = "GET"
        response = self.request(url=urljoin(self.base_url, url), method=method, params=None, headers=self.headers)
        return response

    def post_v1_store_products_categorys(self, name=""):
        """添加商品分类"""
        url = "/v1/store/products/categorys"
        method = "POST"
        json = {
            "name": name
        }
        response = self.request(url=urljoin(self.base_url, url), method=method, headers=self.headers, json=json)
        return response


if __name__ == "__main__":
    api = V1StoreApi(username="119@kd.ssj", password="123456")
    resp = api.post_v1_store_products_categorys(name="")
    print(resp.text)


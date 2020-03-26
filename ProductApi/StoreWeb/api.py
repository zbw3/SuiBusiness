#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File   : api.py
# @Author : mocobk
# @Email  : mailmzb@qq.com
# @Time   : 2019/1/22 9:53
from ProductApi.StoreWeb import config
from ProductApi.Sui.api import Sui
from ProductApi.base import ApiBase


class StoreWebApi(ApiBase):

    def __init__(self, username, password, trading_entity="3604098", print_results=False):
        """
        :param username: 用户名
        :param password: 密码
        :param trading_entity: 账本 ID
        """
        super().__init__(print_results)
        self.config: config.Test = getattr(config, self.env.name)
        self.headers = Sui(username, password).authorized_hearders()
        self.headers["Trading-Entity"] = trading_entity

    def v1_store_products_categorys_get(self):
        """
        Name: 查询商品分类
        DocUrl: None
        """
        url = self.config.Url.v1_store_products_categorys
        response = self.request(url=url, method='GET', headers=self.headers)
        return response

    def v1_store_products_categorys_post(self, params: dict):
        """
        Name: 添加商品分类
        DocUrl: None

        data::

            name            String  Y   分类名称

        """
        url = self.config.Url.v1_store_products_categorys
        response = self.request(url=url, method='POST', headers=self.headers, json=params)
        return response


if __name__ == '__main__':
    api = StoreWebApi(username="119@kd.ssj", password="123456", print_results=True)
    res1 = api.v1_store_products_categorys_get().data
    res2 = api.v1_store_products_categorys_post({'name': ''}).data

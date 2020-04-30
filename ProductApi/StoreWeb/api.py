#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File   : api.py
# @Author : mocobk
# @Email  : mailmzb@qq.com
# @Time   : 2019/1/22 9:53
import json

from ProductApi.StoreWeb import config
from ProductApi.Sui.api import Sui
from ProductApi.base import ApiBase


class StoreWebApi(ApiBase):

    def __init__(self, username, password, trading_entity, Minor_Version='1', print_results=False):
        """
        :param username: 用户名
        :param password: 密码
        :param trading_entity: 账本 ID （3604098）
        """
        super().__init__(print_results)
        self.config: config.Test = getattr(config, self.env.name)
        self.headers = Sui(username, password).authorized_headers()
        self.headers["Minor-Version"] = Minor_Version
        self.headers["Trading-Entity"] = trading_entity
        self.headers["Content-Type"] = "application/json"

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

    def v4_trade_orders_pages_get(self, params: dict):
        """
        Name: 查询订单列表
        DocUrl: None

        data::

            type             String  Y   分类名称
            page_number      String  Y   分类名称
            page_size        String  Y   分类名称

        """
        url = self.config.Url.v4_trade_orders_pages
        response = self.request(url=url, method='GET', headers=self.headers, params=params)
        return response

    def v2_report_range_get(self, params: dict):
        """
        Name: 报表
        DocUrl: None

        data::



        """
        url = self.config.Url.v2_report_range_get

        response = self.request(url=url, method='GET', headers=self.headers, params=params)
        return response

    def v2_report_month_get(self, params: dict):
        """
            Name: 月报
            DocUrl: None

            data::

            """
        url = self.config.Url.v1_report_month_get
        response = self.request(url=url, method='GET', headers=self.headers, params=params)
        return response

    def v1_store_vip_sms(self, params: dict):
        """
                  Name: 会员短信验证
                  DocUrl: None

                  data::

           """
        url = self.config.Url.v1_store_vip_sms
        response = self.request(url=url, method='POST', headers=self.headers, json=params)
        return response

    def v1_store_vip_add_member(self, params: dict):
        """
                  Name: 添加会员
                  DocUrl: None

                  data::

           """
        url = self.config.Url.v1_store_vip_add_member
        response = self.request(url=url, method='POST', headers=self.headers, json=params)
        return response

    def v1_store_vip_orders_page(self, params: dict):
        """
                  Name: 订单页面
                  DocUrl: None

                  data::

           """
        url = self.config.Url.v1_store_vip_orders_page
        response = self.request(url=url, method='GET', headers=self.headers, params=params)
        return response

    def v1_store_vip_check_phone(self, params: dict):
        """
                  Name: 订单页面
                  DocUrl: None

                  data::

           """
        url = self.config.Url.v1_store_vip_check_phone
        response = self.request(url=url, method='GET', headers=self.headers, params=params)
        return response

    def v1_store_vip_member_detail(self, params: dict):
        """
                  Name: 订单页面
                  DocUrl: None

                  data::

           """
        url = self.config.Url.v1_store_vip_member_detail
        response = self.request(url=url, method='GET', headers=self.headers, params=params)
        return response

    def v1_acquiring_open_account_cancel(self):
        """
                  Name: 开户撤回申请接口
                  DocUrl: None

                  data::

           """
        url = self.config.Url.v1_acquiring_account_cancel
        response = self.request(url=url, method='POST', headers=self.headers)
        return response

    def v1_acquiring_open_account_status(self):
        """
                  Name: 查询开户状态（增加了新状态，即Minor-Version=4）
                  DocUrl: None

                  data::

           """
        url = self.config.Url.v1_acquiring_open_account_status
        response = self.request(url=url, method='GET', headers=self.headers)
        return response

    def v3_acquiring_open_account_status(self):
        """
                  Name: 微信开户，查询状态，一样是进行兼容性测试
                  DocUrl: None

                  data::

           """
        url = self.config.Url.v3_acquiring_open_account_status
        response = self.request(url=url, method='GET', headers=self.headers)
        return response

    def v1_acquiring_open_account_info(self, params: dict):
        """
                  Name: 上传开户信息
                  DocUrl: None

                  data::

           """
        url = self.config.Url.v1_acquiring_open_account_info
        response = self.request(url=url, method='POST', headers=self.headers, json=params)
        return response


if __name__ == '__main__':
    api = StoreWebApi(username="119@kd.ssj", password="123456", trading_entity="3604098", Minor_Version="2",
                      print_results=True)
    res1 = api.v1_store_products_categorys_get().data
    res2 = api.v1_store_products_categorys_post({'name': ''}).data




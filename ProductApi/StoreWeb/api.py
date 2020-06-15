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

    def __init__(self, username, password, version='1', trading_entity="3604098", print_results=False):
        """
        :param username: 用户名
        :param password: 密码
        :param trading_entity: 账本 ID
        """
        super().__init__(print_results)
        self.config: config.Test = getattr(config, self.env.name)
        self.headers = Sui(username, password).authorized_hearders()
        self.headers["Minor-Version"] = version
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

    def v1_store_vip_vip_member_detail(self, params: dict):
        """
                  Name: 订单页面
                  DocUrl: None

                  data::

           """
        url = self.config.Url.v1_store_vip_member_detail
        response = self.request(url=url, method='GET', headers=self.headers, params=params)
        return response


    def v2_store_products_spec_name_post(self, params: dict):
        """"添加商品规格名"""
        url = self.config.Url.v2_store_products_spec_name
        response = self.request(url=url, method='POST', headers=self.headers, json=params)
        return response


    def v2_store_products_spec_get(self, **params: dict):
        """"获取店铺规格"""
        url = self.config.Url.v2_store_products_specs
        response = self.request(url=url, method='GET', headers=self.headers, json=params)
        return response

    def v2_store_products_spec_value_post(self, params: dict):
        """添加商品规格值"""
        url = self.config.Url.v2_store_products_spec_value
        response = self.request(url=url, method='POST', headers=self.headers, json=params)
        return response

    def v2_store_products_goods_get(self, params: dict):
        """"查询商品"""
        url = self.config.Url.v2_store_products_goods
        response = self.request(url=url, method='GET', headers=self.headers, params=params)
        return response

if __name__ == '__main__':
    api = StoreWebApi(username="13085060818", password="123456", version='1', trading_entity="37017996", print_results=True)
    # res1 = api.v2_store_products_spec_name_post({'spec_name': '尺寸'}).data  #添加商品规格名
    # res = api.v2_store_products_spec_get(spec_name='尺寸') #指定查询某个规格
    # res = api.v2_store_products_spec_get() #查询店铺所有规格
    #res = api.v2_store_products_spec_value_post({"spec_name_id": "5", "spec_value": "超大"}) #添加商品规格值
    # res = api.v2_store_products_goods_get({'page_number': 1, 'page_size': 30}) # 查询店铺商品

    # print(res)



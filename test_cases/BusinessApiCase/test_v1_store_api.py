#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File : test_v1_store_api.py
# @Author: GoGo
# @Date : 2020/3/20
# @Desc :

import unittest

from ddt import ddt, unpack, data
from ProductApi.BusinessApi.v1_store_api import V1StoreApi
from settings.TestData.data_v1_stroe_api import DataV1StroeApi


@ddt
class TestV1StoreApi(unittest.TestCase):

    def setUp(self) -> None:
        self.api = V1StoreApi(username=DataV1StroeApi.USERNAME, password=DataV1StroeApi.PASSWORD,
                              trading_entity=DataV1StroeApi.Trading_Entity)

    def test_get_v1_store_products_categorys(self):
        response = self.api.get_v1_store_products_categorys()
        self.assertIsNotNone(response)
        self.assertEqual(response.status_code, 200)

    @data(*DataV1StroeApi.data_post_v1_store_products_categorys())
    @unpack
    def test_post_v1_store_products_categorys(self, case_no, case_info, case_data, check_data):
        response = self.api.post_v1_store_products_categorys(**case_data)
        self.assertIsNotNone(response)
        self.assertEqual(response.status_code, check_data["status_code"])
        if response.data is not None:
            if "code" in response.data.keys():
                self.assertEqual(response.data["code"], check_data["code"])
            if "message" in response.data.keys():
                self.assertEqual(response.data["message"], check_data["message"])

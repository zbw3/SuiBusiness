# !/user/bin/env python
# _*_ coding: utf-8 _*_
# @File  : test_v1_store_vip_orders_page.py
# @Author: zy
# @Date  : 2020/4/8
import unittest
import ddt
from ProductApi.StoreWeb import api
import json


def for_resp(params: dict):
    api1 = api.StoreWebApi(username="18702612890", password="a123456", trading_entity="36756947", Minor_Version="2",
                           print_results=True)
    resp = api1.v1_store_vip_orders_page(params=params)
    resp.encoding = 'etf-8'
    return resp


# 以下条件，order_code、vip_member_no、vip_nick_name、vip_phone、begin_date、end_date这几个是前端显示的非必填条件参数
param1 = {
    "query": json.dumps({
        "order_code": "",
        "vip_member_no": "",
        "vip_nick_name": "",
        "status": "",
        "vip_phone": "",
        "begin_date": "",
        "end_date": 1586361599999,
        "page_number": 1,
        "page_size": 30
    })
}

param2 = {
    "query": json.dumps({
        "order_code": "1111",
        "vip_member_no": "",
        "vip_nick_name": "111",
        "status": "",
        "vip_phone": "",
        "begin_date": "",
        "end_date": 1586361599999,
        "page_number": 1,
        "page_size": 30
    })
}

param3 = {
    "query": json.dumps({
        "order_code": "1111",
        "vip_member_no": "",
        "vip_nick_name": "",
        "status": "",
        "vip_phone": "",
        "begin_date": "",
        "end_date": 1586361599999,
        "page_number": 1,
        "page_size": 30
    })
}

param4 = {
    "query": json.dumps({
        "order_code": "的",
        "vip_member_no": "的",
        "vip_nick_name": "",
        "status": "",
        "vip_phone": "",
        "begin_date": "",
        "end_date": 1586361599999,
        "page_number": 1,
        "page_size": 30
    })
}

param5 = {
    "query": json.dumps({
        "order_code": "",
        "vip_member_no": "的",
        "vip_nick_name": "的",
        "status": "",
        "vip_phone": "",
        "begin_date": "",
        "end_date": 1586361599999,
        "page_number": 1,
        "page_size": 30
    })
}


@ddt.ddt
class Test(unittest.TestCase):
    @ddt.data(param1)
    def test_1(self, params):
        resp = for_resp(params)
        self.assertEqual(resp.status_code, 200)

    @ddt.data(param2)
    def test_2(self, params):
        resp = for_resp(params)
        self.assertEqual(resp.status_code, 200)

    @ddt.data(param3)
    def test_3(self, params):
        resp = for_resp(params)
        self.assertEqual(resp.status_code, 200)

    @ddt.data(param4)
    def test_4(self, params):
        resp = for_resp(params)
        self.assertEqual(resp.status_code, 200)

    @ddt.data(param5)
    def test_5(self, params):
        resp = for_resp(params)
        self.assertEqual(resp.status_code, 200)


if __name__ == '__main__':
    Test(unittest.TestCase)

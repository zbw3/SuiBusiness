# !/user/bin/env python
# _*_ coding: utf-8 _*_
# @File  : test_v1_store_vip_check_phone.py
# @Author: zy
# @Date  : 2020/4/8
import unittest
import ddt
from ProductApi.StoreWeb import api


def for_resp(params: dict):
    api1 = api.StoreWebApi(username="119@kd.ssj", password="123456", print_results=True)
    resp = api1.v1_store_vip_check_phone(params=params)
    resp.encoding = 'etf-8'
    return resp


# 该号码已存在，不允许创建，所以应该返回false
param1 = {
    'phone': '18576776815',
}
# 该号码不存在，可以创建，所以返回true
param2 = {
    'phone': '18702612890',
}


@ddt.ddt
class Test(unittest.TestCase):
    @ddt.data(param1)
    def test_1(self, params):
        resp = for_resp(params)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.text, 'false')

    @ddt.data(param2)
    def test_2(self, params):
        resp = for_resp(params)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.text, 'true')


if __name__ == '__main__':
    Test(unittest.TestCase)

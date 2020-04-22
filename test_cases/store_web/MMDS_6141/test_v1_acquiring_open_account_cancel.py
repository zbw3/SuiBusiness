# !/user/bin/env python
# _*_ coding: utf-8 _*_
# @File  : test_v1_acquiring_open_account_cancel.py
# @Author: zy
# @Date  : 2020/4/13
from ProductApi.StoreWeb import api
import unittest


def for_resp(params, params1):
    api1 = api.StoreWebApi(username="119@kd.ssj", password="123456", trading_entity=params, Minor_Version=params1,
                           print_results=True)
    resp = api1.v1_acquiring_open_account_cancel()
    resp.encoding = 'etf-8'
    return resp


# 撤回申请，就是将开户状态改为未提交状态，也就是未开户，即total_status的值为-1
class Test(unittest.TestCase):
    def test_1(self):
        resp = for_resp(params="3672790", params1="4")
        self.assertEqual(resp.status_code, 200)


if __name__ == '__main__':
    Test(unittest.TestCase)

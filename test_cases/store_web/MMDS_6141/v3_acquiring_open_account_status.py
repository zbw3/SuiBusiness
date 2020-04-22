# !/user/bin/env python
# _*_ coding: utf-8 _*_
# @File  : v3_acquiring_open_account_status.py
# @Author: zy
# @Date  : 2020/4/13
import json

from ProductApi.StoreWeb import api
import unittest


def for_resp(params, params1):
    api1 = api.StoreWebApi(username="119@kd.ssj", password="123456", trading_entity=params, Minor_Version=params1,
                           print_results=True)
    resp = api1.v3_acquiring_open_account_status()
    resp.encoding = 'etf-8'
    return resp


class Test(unittest.TestCase):
    def test_1(self):
        resp = for_resp(params="3604098", params1="")
        self.assertEqual(resp.status_code, 200)
        dict_text = json.loads(resp.text)
        self.assertEqual(dict_text["total_status"], 2)

    def test_2(self):
        resp = for_resp(params="3672790", params1="")
        self.assertEqual(resp.status_code, 200)
        dict_text = json.loads(resp.text)
        self.assertEqual(dict_text["total_status"], -1)

    def test_3(self):
        resp = for_resp(params="3604098", params1="")
        self.assertEqual(resp.status_code, 200)
        dict_text = json.loads(resp.text)
        self.assertEqual(dict_text["total_status"], 2)

    def test_4(self):
        resp = for_resp(params="3672790", params1="")
        self.assertEqual(resp.status_code, 200)
        dict_text = json.loads(resp.text)
        self.assertEqual(dict_text["total_status"], -1)

    def test_5(self):
        resp = for_resp(params="3672790", params1="")
        self.assertEqual(resp.status_code, 200)
        dict_text = json.loads(resp.text)
        self.assertEqual(dict_text["total_status"], -1)

    def test_6(self):
        resp = for_resp(params="3675196", params1="")
        self.assertEqual(resp.status_code, 200)
        dict_text = json.loads(resp.text)
        self.assertEqual(dict_text["total_status"], 1)


if __name__ == '__main__':
    Test(unittest.TestCase)

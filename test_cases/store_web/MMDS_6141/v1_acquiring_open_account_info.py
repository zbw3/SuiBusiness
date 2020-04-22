# !/user/bin/env python
# _*_ coding: utf-8 _*_
# @File  : v1_acquiring_open_account_info.py
# @Author: zy
# @Date  : 2020/4/13
import json

import ddt

from ProductApi.StoreWeb import api
import unittest
from test_cases.store_web.data import account_data


def for_resp(params):
    username = account_data.data()["username"]
    password = account_data.data()["password"]
    api1 = api.StoreWebApi(username=username, password=password, trading_entity="3672790", Minor_Version="2",
                           print_results=True)
    resp = api1.v1_acquiring_open_account_info(params)
    resp.encoding = 'etf-8'
    return resp


# 申请开户（已经开户了的仍然可以申请开户）
params1 = {
    "store_id": "",
    "phone": "18702612890",
    "id_card": "",
    "name": "测试用",
    "bank_name": "",
    "bank_card": "",
    "province": "",
    "city": "",
    "district": "",
    "store_name": "",
    "store_address": "",
    "licence_code": "",
    "step_flag": "true"
}


@ddt.ddt
class Test(unittest.TestCase):
    @ddt.data(params1)
    def test_1(self, params):
        resp = for_resp(params)


if __name__ == '__main__':
    unittest.main()

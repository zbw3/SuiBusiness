# !/user/bin/env python
# _*_ coding: utf-8 _*_
# @File  : v1_acquiring_open_account_info.py
# @Author: zy
# @Date  : 2020/4/13
import pytest

from ProductApi.StoreWeb import api
from test_cases.store_web.data import account_data


def get_resp(params):
    username = account_data.data()["username"]
    password = account_data.data()["password"]
    api1 = api.StoreWebApi(username=username, password=password, trading_entity="370059118", Minor_Version="2",
                           print_results=True)
    resp = api1.v1_acquiring_open_account_info(params)
    # resp.encoding = 'utf-8'
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


def test_1():
    get_resp(params1)


if __name__ == '__main__':
    pytest.main()

# 370059118的账本名字是12345

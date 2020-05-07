# !/user/bin/env python
# _*_ coding: utf-8 _*_
# @File  : test_v1_store_vip_sms.py
# @Author: zy
# @Date  : 2020/4/8
import json

import pytest

from ProductApi.StoreWeb import api
from test_cases.store_web.data import account_data


def get_resp(params: dict):
    username = account_data.data()["username"]
    password = account_data.data()["password"]
    api1 = api.StoreWebApi(username=username, password=password, trading_entity="3604098", Minor_Version="2",
                           print_results=True)
    resp = api1.v1_store_vip_sms(params=params)
    resp.encoding = 'etf-8'
    return resp


# 验证该号码是否有短信发送（正常号码）
params_1 = {
    'phone': '18702612890'
}


def test_1():
    params = params_1
    resp = get_resp(params)
    assert resp.status_code == 200
    dict_resp = json.loads(resp.text)
    return dict_resp["vcid"]


if __name__ == '__main__':
    pytest.main()

# !/user/bin/env python
# _*_ coding: utf-8 _*_
# @File  : test_v1_store_vip_check_phone.py
# @Author: zy
# @Date  : 2020/4/8
import pytest

from ProductApi.StoreWeb import api
from test_cases.store_web.data import account_data


def get_resp(params: dict):
    username = account_data.data()["username"]
    password = account_data.data()["password"]
    api1 = api.StoreWebApi(username=username, password=password, trading_entity="3604098", Minor_Version="2",
                           print_results=True)
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


def test_1():
    params = param1
    resp = get_resp(params)
    assert resp.status_code == 200
    assert resp.text == 'false'


def test_2():
    params = param2
    resp = get_resp(params)
    assert resp.status_code == 200
    assert resp.text == 'true'


if __name__ == '__main__':
    pytest.main()

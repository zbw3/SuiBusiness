# !/user/bin/env python
# _*_ coding: utf-8 _*_
# @File  : test_v1_store_vip_orders_page.py
# @Author: zy
# @Date  : 2020/4/8
import pytest

from ProductApi.StoreWeb import api
import json
from test_cases.store_web.data import account_data


def get_resp(params: dict):
    username = account_data.data()["username"]
    password = account_data.data()["password"]
    api1 = api.StoreWebApi(username=username, password=password, trading_entity="36756947", Minor_Version="2",
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


def test_1():
    params = param1
    resp = get_resp(params)
    assert resp.status_code == 200


def test_2():
    params = param2
    resp = get_resp(params)
    assert resp.status_code == 200


def test_3():
    params = param3
    resp = get_resp(params)
    assert resp.status_code == 200


def test_4():
    params = param4
    resp = get_resp(params)
    assert resp.status_code == 200


def test_5():
    params = param5
    resp = get_resp(params)
    assert resp.status_code == 200


if __name__ == '__main__':
    pytest.main()

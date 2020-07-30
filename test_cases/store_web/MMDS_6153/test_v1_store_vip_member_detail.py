# !/user/bin/env python
# _*_ coding: utf-8 _*_
# @File  : test_v1_store_vip_member_detail.py
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
    resp = api1.v1_store_vip_member_detail(params=params)
    resp.encoding = 'etf-8'
    return resp


# 查询会员，根据条件，其中source表示第三方账号，1表示支付宝，2表示微信
# vaild表示会员状态，0表示已冻结，1表示正常
param1 = {
    "multi_conditions": json.dumps({
        "tag_id": "",
        "tag_id_flag": True,
        "nick_name": "",
        "vip_number": "1111",
        "phone": "",
        "level_id": "",
        "source": "4",
        "valid": 0
    }),
    "page_number": 1,
    "page_size": 30
}
# 会员名和会员卡号都支持模糊查询（组合条件查询）
param2 = {
    "multi_conditions": json.dumps({
        "tag_id": "",
        "tag_id_flag": True,
        "nick_name": "被",
        "vip_number": "9",
        "phone": "",
        "level_id": "",
        "source": "",
        "valid": 0
    }),
    "page_number": 1,
    "page_size": 30
}


def test_1():
    params = param1
    resp = get_resp(params)
    assert resp.status_code == 200


def test_2():
    params = param2
    resp = get_resp(params)
    assert resp.status_code == 200


if __name__ == '__main__':
    pytest.main()

# !/user/bin/env python
# _*_ coding: utf-8 _*_
# @File  : v1_store_vip_add_member.py
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
    resp = api1.v1_store_vip_add_member(params=params)
    resp.encoding = 'etf-8'
    return resp


# vcid需要使用v1_store_sms返回的vcid，需要联合接口使用，也就是先使用sms获取验证码和vcid
param1 = {
    'nick_name': '111',
    'phone': '18702612890',
    'sms_code': '',
    'vcid': ''
}


def test_1():
    params = param1
    resp = get_resp(params)
    assert resp.status_code == 200


if __name__ == '__main__':
    pytest.main()

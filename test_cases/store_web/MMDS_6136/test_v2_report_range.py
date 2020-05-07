# !/user/bin/env python
# _*_ coding: utf-8 _*_
# @File  : test_v2_report_range.py
# @Author: zy
# @Date  : 2020/3/26
import json
import ddt
import pytest

from ProductApi.StoreWeb import api
import unittest
from test_cases.store_web.MMDS_6136 import timestamp
import jmespath
from test_cases.store_web.data import account_data


def for_resp(params: dict):
    username = account_data.data()["username"]
    password = account_data.data()["password"]
    api1 = api.StoreWebApi(username=username, password=password, trading_entity="3604098", Minor_Version="2",
                           print_results=True)
    resp = api1.v2_report_range_get(params=params)
    resp.encoding = 'etf-8'
    return resp


# 正向用例1，传参单个channel_type，值为1，即门店，以及开始和结束时间
params_1 = {
    "multi_conditions": json.dumps(
        {
            "channel_type": "",
            'begin_date': timestamp.timestamp('2020-4-9 00:00:00'),
            "end_date": timestamp.timestamp('2020-4-10 00:00:00'),
        }
    ),

}
# 正向用例2，传参单个channel_type，值为2
params_2 = {
    "multi_conditions": json.dumps(
        {
            "channel_type": "2",
        }
    )
}
# 反向用例3，组合传参channel_type和handler，其中handler是传没有的值
params_3 = {
    "multi_conditions": json.dumps(
        {
            "handler": "aa",
            "channel_type": "1",
        }
    )
}
# 正向用例4，多条件选择全部传参channel_type和开始时间、结束时间、经手人，这里的begin_date和end_date对应的是biz_order表中的order_time
params_4 = {
    "multi_conditions": json.dumps(
        {
            "channel_type": '1',
            # 'begin_date': timestamp.timestamp('2020-3-25 00:00:00'),
            "end_date": timestamp.timestamp('2020-3-31 00:00:00'),
            "handler": "119@feidee"
        }
    )
}


def test_1():
    params = params_1
    resp = for_resp(params)
    assert resp.status_code, 200


def test_2():
    params = params_2
    resp = for_resp(params)
    assert resp.status_code, 200


def test_3():
    params = params_3
    resp = for_resp(params)
    assert resp.status_code, 200


def test_4():
    params = params_4
    resp = for_resp(params)
    assert resp.status_code, 200
    dict_1 = json.loads(resp.text)
    result = jmespath.search('sale_amount', dict_1)
    print(result)


if __name__ == '__main__':
    pytest.main()


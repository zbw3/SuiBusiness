# !/user/bin/env python
# _*_ coding: utf-8 _*_
# @File  : test_v4_trade_orders_page.py
# @Author: zy
# @Date  : 2020/3/26
import json
from ProductApi.StoreWeb import api
from test_cases.store_web.MMDS_6136 import timestamp
from test_cases.store_web.data import account_data


def get_resp(params: dict):
    username = account_data.data()["username"]
    password = account_data.data()["password"]
    api1 = api.StoreWebApi(username=username, password=password, trading_entity="3604098", Minor_Version="2",
                           print_results=True)
    resp = api1.v4_trade_orders_pages_get(params=params)
    # resp.encoding = 'utf-8'
    return resp


# 正向用例1，输入查询参数：type、page_number、page_size（这3个是必输项）
params_1 = {
    'type': 'sale',
    'page_number': 1,
    'page_size': 2,
    "multi_conditions": json.dumps(
        {
            "channel_type": '1',
        }
    )
}
# 正向用例2，输入查询参数：type、page_number、page_size
params_2 = {
    'type': 'sale',
    'page_number': 1,
    'page_size': 2,
}
# 正向用例3，输入查询参数：type、page_number、page_size，type = both，查询不到，目前只支持sale
params_3 = {
    'type': 'both',
    'page_number': 1,
    'page_size': 2
}
# 正向用例4，输入查询参数：type、page_number、page_size，多条件查询：multi_conditions，新增了门店渠道:channel_type
params_4 = {
    'type': 'sale',
    'page_number': 4,
    'page_size': 4,
    "multi_conditions": json.dumps(
        {
            "channel_type": '1',
            'begin_date': timestamp.timestamp('2020-1-1 00:00:00')
        }
    ),
}
# 正向用例5，输入查询参数：type、page_number、page_size，多条件查询：multi_conditions，新增了门店渠道:channel_type
params_5 = {
    'type': 'sale',
    'page_number': 1,
    'page_size': 2,
    "multi_conditions": json.dumps(
        {
            "channel_type": '1',
            'begin_date': '1583078400000',
            'status': '1',
            "calc_profit": True,
            'end_date': '1585670399999'
        }
    )
}


def test_1():
    params = params_1
    resp = get_resp(params)
    assert resp.status_code == 200


def test_2():
    params = params_2
    resp = get_resp(params)
    assert resp.status_code == 200


def test_3():
    params = params_3
    resp = get_resp(params)
    assert resp.status_code == 200


def test_4():
    params = params_4
    resp = get_resp(params)
    assert resp.status_code == 200


def test_5():
    params = params_5
    resp = get_resp(params)
    assert resp.status_code == 200


if __name__ == '__main__':
    test_1()

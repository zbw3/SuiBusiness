# !/user/bin/env python
# _*_ coding: utf-8 _*_
# @File  : v3_acquiring_open_account_status.py
# @Author: zy
# @Date  : 2020/4/13
from ProductApi.StoreWeb import api
from test_cases.store_web.data import account_data


def get_resp(params, params1):
    username = account_data.data()["username"]
    password = account_data.data()["password"]
    api1 = api.StoreWebApi(username=username, password=password, trading_entity=params, Minor_Version=params1,
                           print_results=True)
    resp = api1.v3_acquiring_open_account_status()
    # resp.encoding = 'utf-8'
    return resp


def test_1():
    resp = get_resp(params="37005934", params1="")
    assert resp.status_code == 200
    # dict_text = json.loads(resp.text)
    dict_text = resp.json()
    assert dict_text["total_status"] == 3


def test_2():
    resp = get_resp(params="36611940", params1="")
    assert resp.status_code == 200
    # dict_text = json.loads(resp.text)
    dict_text = resp.json()
    assert dict_text["total_status"] == -1


def test_3():
    resp = get_resp(params="3604098", params1="")
    assert resp.status_code == 200
    # dict_text = json.loads(resp.text)
    dict_text = resp.json()
    assert dict_text["total_status"] == 2


def test_4():
    resp = get_resp(params="37006926", params1="")  # 店铺名—店铺名称是不是同步，开户状态是—未开户
    assert resp.status_code == 200
    # dict_text = json.loads(resp.text)
    dict_text = resp.json()
    assert dict_text["total_status"] == -1


def test_5():
    resp = get_resp(params="370059118", params1="4")  # 店铺名—12345，开户状态是—审核失败
    assert resp.status_code == 200
    # dict_text = json.loads(resp.text)
    dict_text = resp.json()
    assert dict_text["total_status"] == 0


def test_6():
    resp = get_resp(params="", params1="")  # 店铺名——kk，开户状态是：待审核
    assert resp.status_code == 200
    # dict_text = json.loads(resp.text)
    dict_text = resp.json()
    assert dict_text["total_status"] == 1


if __name__ == '__main__':
    test_1()
# 该接口传账本id不起作用

# !/user/bin/env python
# _*_ coding: utf-8 _*_
# @File  : test_v1_acquiring_open_account_status.py
# @Author: zy
# @Date  : 2020/4/13
from ProductApi.StoreWeb import api
from test_cases.store_web.data import account_data


def get_resp(params, params1):
    username = account_data.data()["username"]
    password = account_data.data()["password"]
    api1 = api.StoreWebApi(username=username, password=password, trading_entity=params, Minor_Version=params1,
                           print_results=True)
    resp = api1.v1_acquiring_open_account_status()
    # resp.encoding = 'utf-8'
    return resp


# 用例1——测试账本“FF3”，提交开户资料，但是审核拒绝，即审核失败（账本id是3675196），Minor-Version有值为4则是用于Web请求
def test_1():
    resp = get_resp(params="3675196", params1="4")
    assert resp.status_code == 200
    # dict_text = json.loads(resp.text)
    dict_text = resp.json()
    assert dict_text["total_status"] == 0


# 用例2——测试账本“dd”，提及开户资料，且处于待审核，即商户还未审核。
# 即生意账本后台的商户管理没有点击编辑，没有进入审核中的状态，Minor-Version有值为“4”则是用于Web请求
def test_2():
    resp = get_resp(params="3672790", params1="4")
    assert resp.status_code == 200
    # dict_text = json.loads(resp.text)
    dict_text = resp.json()
    assert dict_text["total_status"] == 3


# 用例3——测试账本“零售勿删3604098”，该账本已经开户
def test_3():
    resp = get_resp(params="3604098", params1="4")
    assert resp.status_code == 200
    # dict_text = json.loads(resp.text)
    dict_text = resp.json()
    assert dict_text["total_status"] == 2


# 用例4——测试账本“12345”，该账本审核失败
def test_4():
    resp = get_resp(params="370059118", params1="")
    assert resp.status_code == 200
    # dict_text = json.loads(resp.text)
    dict_text = resp.json()
    assert dict_text["total_status"] == 0


# 用例5——测试账本“FF3”，该账本提交资料，审核失败
def test_5():
    resp = get_resp(params="3675196", params1="")
    assert resp.status_code == 200
    # dict_text = json.loads(resp.text)
    dict_text = resp.json()
    assert dict_text["total_status"] == 0


# 用例6——测试账本“零售勿删3604098”，该账本已经开户
def test_6():
    resp = get_resp(params="3604098", params1="")
    assert resp.status_code == 200
    # dict_text = json.loads(resp.text)
    dict_text = resp.json()
    assert dict_text["total_status"] == 2


if __name__ == '__main__':
    test_1()

# 插叙账本的开户状态，增加新版本Minor-Version=4，是测之前的旧版本是否兼容

# total_status的值分别表示：-1：未开户 ，0：审核失败，1：审核中，2：审核成功，3：待审核

# 其中3604098账本已开户，3672790账本对应的是账本名是dd，3675196对应的账本名是FF3

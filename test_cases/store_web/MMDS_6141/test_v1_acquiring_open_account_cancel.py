# !/user/bin/env python
# _*_ coding: utf-8 _*_
# @File  : test_v1_acquiring_open_account_cancel.py
# @Author: zy
# @Date  : 2020/4/13
import pytest

from ProductApi.StoreWeb import api
from test_cases.store_web.data import account_data


def get_resp(params, params1):
    username = account_data.data()["username"]
    password = account_data.data()["password"]
    api1 = api.StoreWebApi(username=username, password=password, trading_entity=params, Minor_Version=params1,
                           print_results=True)
    resp = api1.v1_acquiring_open_account_cancel()
    # resp.encoding = 'utf-8'
    return resp


# 撤回申请，就是将开户状态改为未提交状态，也就是未开户，即total_status的值为-1
# 下面的账本id需要更换
def test_1():
        resp = get_resp(params="账本id", params1="4")
        assert resp.status_code == 200


if __name__ == '__main__':
    pytest.main()
# 1、待审核中可以撤回申请，使用该接口
# 2、审核失败重新提交也是用到了该接口，撤回申请

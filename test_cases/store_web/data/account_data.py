# !/user/bin/env python
# _*_ coding: utf-8 _*_
# @File  : account_data.py
# @Author: zy
# @Date  : 2020/4/22
from settings.BaseConfig import Env


def data():
    account = {
        'username': '119@kd.ssj' if Env().is_test else '',
        'password': '123456' if Env().is_test else ''
    }
    return account


class AccountData:
    pass

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File   : Account.py
# @Author : mocobk
# @Email  : mailmzb@qq.com
# @Time   : 2020/3/26 15:14

"""随手记账号信息"""
from collections import namedtuple

_ACCOUNT = namedtuple('Account', ['username', 'password'])

user_119 = _ACCOUNT('119@kd.ssj', '123456')

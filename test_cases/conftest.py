#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File   : conftest.py.py
# @Author : mocobk
# @Email  : mailmzb@qq.com
# @Time   : 2020/3/26 20:41


def pytest_collection_modifyitems(session, config, items):
    """
    部分用例可能用到参数化，默认参数中是中文的会显示 unicode 编码
    测试用例收集完成时，将收集到的item的name和nodeid的中文显示在控制台上
    :return:
    """
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")

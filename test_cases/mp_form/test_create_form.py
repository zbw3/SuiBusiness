#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File   : test_create_form.py
# @Author : mocobk
# @Email  : mailmzb@qq.com
# @Time   : 2020/7/27 14:56
import pytest

from test_cases.mp_form import verify_create_form


def test_create_activity_form(user1, default_activity_form):
    """验证创建报名接龙接口的正确性"""
    verify_create_form(user1, default_activity_form)


def test_create_shopping_form(user1, default_shopping_form):
    """验证创建商品接龙表单接口的正确性"""
    verify_create_form(user1, default_shopping_form)


if __name__ == '__main__':
    pytest.main()

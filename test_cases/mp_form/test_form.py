#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File   : test_post_and_put_form.py
# @Author : mocobk
# @Email  : mailmzb@qq.com
# @Time   : 2020/7/27 14:56
import pytest

from test_cases.mp_form import verify_post_form, verify_put_form


def test_post_activity_form(user1, default_activity_form):
    """验证创建 [报名接龙] 表单接口的正确性"""
    verify_post_form(user1, default_activity_form)

def test_post_shopping_form(user1, default_shopping_form):
    """验证创建 [商品接龙] 表单接口的正确性"""
    verify_post_form(user1, default_shopping_form)

def test_put_activity_form(user1, default_activity_form):
    """验证修改 [报名接龙] 表单接口的正确性"""
    verify_put_form(user1, default_activity_form)

def test_put_shopping_form(user1, default_shopping_form):
    """验证修改 [商品接龙] 表单接口的正确性"""
    verify_put_form(user1, default_shopping_form)


if __name__ == '__main__':
    pytest.main()

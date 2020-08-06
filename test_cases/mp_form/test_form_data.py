#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File   : test_post_and_put_form_data.py
# @Author : mocobk
# @Email  : mailmzb@qq.com
# @Time   : 2020/7/27 14:56
from collections import namedtuple

import pytest

from test_cases.mp_form import verify_post_form_data, verify_put_form_data, verify_cancel_form_data, create_form


@pytest.fixture(scope='module')
def form_res(user1, default_activity_form, default_shopping_form):
    Form = namedtuple('Form', ['activity', 'shopping'])
    default_activity_form.set_title('参与接龙测试')
    default_shopping_form.set_title('参与接龙测试')
    return Form(
        create_form(user1, default_activity_form),
        create_form(user1, default_shopping_form)
    )


def test_post_activity_form_data(user1, user2, form_res):
    """验证 [报名接龙] 提交接龙数据"""
    verify_post_form_data(user1, user2, form_res.activity)


def test_post_shopping_form_data(user1, user2, form_res):
    """验证 [报名接龙] 提交接龙数据"""
    verify_post_form_data(user1, user2, form_res.shopping)


def test_put_activity_form_data(user2, form_res):
    """验证 [报名接龙] 修改接龙数据"""
    verify_put_form_data(user2, form_res.activity)


def test_put_shopping_form_data(user2, form_res):
    """验证 [商品接龙] 修改接龙数据"""
    verify_put_form_data(user2, form_res.shopping)


def test_cancel_activity_form_data(user2, form_res):
    """验证 [报名接龙] 取消接龙数据"""
    verify_cancel_form_data(user2, form_res.activity)


def test_cancel_shopping_form_data(user2, form_res):
    """验证 [商品接龙] 取消接龙数据"""
    verify_cancel_form_data(user2, form_res.shopping)


if __name__ == '__main__':
    pytest.main()

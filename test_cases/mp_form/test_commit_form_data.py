#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File   : test_commit_form_data.py
# @Author : mocobk
# @Email  : mailmzb@qq.com
# @Time   : 2020/7/27 14:56
from collections import namedtuple

import pytest

from test_cases.mp_form import verify_post_form_data, verify_put_form_data


@pytest.fixture(scope='module')
def form(user1, default_activity_form, default_shopping_form):
    Form = namedtuple('Form', ['activity', 'shopping'])
    return Form(
        user1.v1_form(default_activity_form.data, return_form_id=True),
        user1.v1_form(default_shopping_form.data, return_form_id=True)
    )


def test_post_activity_form_data(user1, user2, form):
    """验证[报名接龙]提交接龙数据"""
    verify_post_form_data(user1, user2, form.activity)


def test_post_shopping_form_data(user1, user2, form):
    """验证[报名接龙]提交接龙数据"""
    verify_post_form_data(user1, user2, form.shopping)


def test_put_activity_form_data(user2, form):
    """验证[报名接龙]修改接龙数据"""
    verify_put_form_data(user2, form.activity)


def test_put_shopping_form_data(user2, form):
    """验证[商品接龙]修改接龙数据"""
    verify_put_form_data(user2, form.shopping)


if __name__ == '__main__':
    pytest.main()

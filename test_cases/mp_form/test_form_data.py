#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File   : test_post_and_put_form_data.py
# @Author : mocobk
# @Email  : mailmzb@qq.com
# @Time   : 2020/7/27 14:56
from collections import namedtuple

import pytest

from ProductApi.MiniProgramForm.api import FormApi
from ProductApi.MiniProgramForm.form import PostFormData
from test_cases.mp_form import verify_post_form_data, verify_put_form_data, verify_cancel_form_data, create_form


@pytest.fixture()
def forms(user1, default_activity_form, default_shopping_form):
    default_activity_form.set_title('参与接龙测试')
    default_shopping_form.set_title('参与接龙测试')
    default_activity_form.set_limit(2)
    default_shopping_form.set_limit(2)
    default_activity_form.set_per_limit(1)
    default_shopping_form.set_per_limit(1)
    return create_form(user1, default_activity_form), create_form(user1, default_shopping_form)


def create_form_data(form_api: FormApi, form_id: str):
    """
    :param form_api:
    :param form_id:
    :return: sequence
    """
    post_form_data = PostFormData(form_api, form_id).data
    res = form_api.v1_form_id_form_data(form_id, post_form_data, method=form_api.POST)
    return res


def verify_post_form_data_limit(user1: FormApi, user2: FormApi, user3: FormApi, form_id: str):
    create_form_data(user1, form_id)
    sequence = create_form_data(user2, form_id).data.get('data', {}).get('sequence')
    assert sequence == 2
    assert create_form_data(user3, form_id).status_code == 422


def verify_post_form_data_perlimit(user1: FormApi, form_id: str):
    sequence = create_form_data(user1, form_id).data.get('data', {}).get('sequence')
    assert sequence == 1
    return create_form_data(user1, form_id).status_code == 422


def verify_limits(user1: FormApi, user2: FormApi, user3: FormApi, form_id: str):
    create_form_data(user1, form_id)
    sequence = create_form_data(user2, form_id).data.get('data', {}).get('sequence')
    assert sequence == 2
    assert create_form_data(user3, form_id).data.get('code') == 13426


def test_post_form_data(user1, user2, forms):
    """验证提交接龙数据"""
    for form in forms:
        verify_post_form_data(user1, user2, form)


def test_put_form_data(user2, forms):
    """验证修改接龙数据"""
    for form in forms:
        verify_put_form_data(user2, form)


def test_cancel_form_data(user2, forms):
    """验证取消接龙数据"""
    for form in forms:
        verify_cancel_form_data(user2, form)


def test_post_form_data_limit(user1, user2, user3, forms):
    """验证提交接龙数据接龙人数上限"""
    for form in forms:
        verify_post_form_data_limit(user1, user2, user3, form)


def test_post_form_data_perlimit(user1, forms):
    """验证提交接龙数据单个接龙人接龙次数上限"""
    for form in forms:
        verify_post_form_data_perlimit(user1, form)


def test_post_form_data_limits(user1, user2, forms):
    """验证总接龙人数未达上限，单个接龙人接龙次数达上限"""
    for form in forms:
        verify_post_form_data_limit(user1, user2, user1, form)


if __name__ == '__main__':
    pytest.main()

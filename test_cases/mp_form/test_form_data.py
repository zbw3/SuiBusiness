#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File   : test_post_and_put_form_data.py
# @Author : mocobk
# @Email  : mailmzb@qq.com
# @Time   : 2020/7/27 14:56
import pytest

from ProductApi.MiniProgramForm.api import FormApi
from ProductApi.MiniProgramForm.form import PostFormData
from test_cases.mp_form import verify_post_form_data, verify_put_form_data, verify_cancel_form_data, create_form


@pytest.fixture()
def form_ids(user1, default_activity_form, default_shopping_form):
    """
    创建活动报名和团购接龙表单，总报接龙次数限制 3， 每人接龙次数限制 2
    :return tuple[form_id]
    """
    default_activity_form.set_title('参与接龙测试')
    default_shopping_form.set_title('参与接龙测试')
    default_activity_form.set_limit(3)
    default_shopping_form.set_limit(3)
    default_activity_form.set_per_limit(2)
    default_shopping_form.set_per_limit(2)
    form_ids = create_form(user1, default_activity_form), create_form(user1, default_shopping_form)
    return form_ids


def post_form_data(form_api: FormApi, form_id: str):
    """
    :param form_api:
    :param form_id:
    :return: response
    """
    post_form_data = PostFormData(form_api, form_id).data
    res = form_api.v1_form_id_form_data(form_id, post_form_data, method=form_api.POST)
    return res


def post_form_data_twice(user: FormApi, form_id: str):
    """连续接龙2次"""
    for i in range(1, 3):
        response = post_form_data(user, form_id)
        assert response.status_code == 200, response.text
        assert response.data.get('data', {}).get('sequence') == i, response.text


def test_post_form_data(user1, user2, form_ids):
    """验证提交接龙数据"""
    for form in form_ids:
        verify_post_form_data(user1, user2, form)


def test_put_form_data(user2, form_ids):
    """验证修改接龙数据"""
    for form in form_ids:
        verify_put_form_data(user2, form)


def test_cancel_form_data(user2, form_ids):
    """验证取消接龙数据"""
    for form in form_ids:
        verify_cancel_form_data(user2, form)


def test_post_form_data_over_limit(user1, user2, form_ids):
    """验证单个接龙人数未达上限，总接龙人数达上限"""
    for form_id in form_ids:
        post_form_data_twice(user2, form_id)

        response = post_form_data(user1, form_id)
        assert response.status_code == 200, response.text

        response = post_form_data(user1, form_id)
        assert response.status_code == 422, response.text
        assert response.data.get('code') == 13356, response.text


def test_post_form_data_over_per_limit(user2, form_ids):
    """验证总接龙人数未达上限，单个接龙人接龙次数达上限"""
    for form_id in form_ids:
        post_form_data_twice(user2, form_id)

        response = post_form_data(user2, form_id)
        assert response.status_code == 422, response.text
        assert response.data.get('code') == 13426, response.text


def test_post_form_data_over_limit_and_per_limit(user1, user2, form_ids):
    """验证总接龙人数和单个接龙人次都达上限，优先提示单个接龙人接龙次数达上限"""
    for form_id in form_ids:
        post_form_data_twice(user2, form_id)

        response = post_form_data(user1, form_id)
        assert response.status_code == 200, response.text

        response = post_form_data(user2, form_id)
        assert response.status_code == 422, response.text
        assert response.data.get('code') == 13426, response.text


if __name__ == '__main__':
    pytest.main()

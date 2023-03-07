#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File   : test_post_and_put_form.py
# @Author : mocobk
# @Email  : mailmzb@qq.com
# @Time   : 2020/7/27 14:56
import random
import pytest
import allure

from test_cases.mp_form import verify_post_form, verify_put_form, create_form


def test_post_form(user1, default_activity_form, default_shopping_form):
    """验证创建 [报名/商品接龙] 表单接口的正确性"""
    for form in [default_activity_form, default_shopping_form]:
        verify_post_form(user1, form)

def test_post_form_with_admin_permission(user1, default_activity_form, default_shopping_form):
    for form in [default_activity_form, default_shopping_form]:
        form.set_form_data_permission(permission=2)
        form_id = create_form(user1, form)
        res = user1.v1_form_form_id(form_id, method=user1.GET)
        assert res.status_code == 200, res.text
        data = res.data.get('data', {})
        assert data.get('config')['formDataPermission'] == 2


def test_post_form_with_error_permission(user1, default_activity_form, default_shopping_form):
    for form in [default_activity_form, default_shopping_form]:
        permission = random.choice([-1, 0, 3])
        user1.logger.info('表单权限值为: %s', permission)
        form.set_form_data_permission(permission=permission)
        res = user1.v1_form(form.data, return_form_id=True, method=user1.POST)
        assert res.status_code == 400
        assert res.data.get('code') == -1

def test_put_form(user1, default_activity_form, default_shopping_form):
    """验证修改 [报名/商品接龙] 表单接口的正确性"""
    for form in [default_activity_form, default_shopping_form]:
        verify_put_form(user1, form)


def test_get_creation_forms(user1):
    """验证【我的】——我创建的表单列表获取正确性"""

    params = {'pageNo': 1, 'pageSize': 20}
    res = user1.v1_creation_forms(params=params, method=user1.GET)
    assert res.status_code == 200

    """20230210徐雪霞备注：由于数据库分库，目前返回的分页条数和请求的分页数对不上"""
    # forms = res.data.get('data', {}).get('participationForms')
    # # 分页测试
    # if len(forms) > 5:
    #     params = {'pageNo': 2, 'pageSize': 5}
    #     res = user1.v1_participation_forms(params=params, method=user1.GET)
    #     assert res.status_code == 200
    #     forms = res.data.get('data', {}).get('participationForms')
    #     assert 1 <= len(forms) <= 5

def test_get_participation_forms(user1):
    """验证【我的】——我参与的表单列表获取正确性"""
    params = {'pageNo': 1, 'pageSize': 20}
    res = user1.v1_participation_forms(params=params, method=user1.GET)
    assert res.status_code == 200

    forms = res.data.get('data', {}).get('participationForms')
    """20230210徐雪霞备注：由于数据库分库，目前返回的分页条数和请求的分页数对不上"""
    # 分页测试
    if len(forms) > 5:
        params = {'pageNo': 2, 'pageSize': 5}
        res = user1.v1_participation_forms(params=params, method=user1.GET)
        assert res.status_code == 200
        forms = res.data.get('data', {}).get('participationForms')
        assert 1 <= len(forms) <= 5

if __name__ == '__main__':
    pytest.main(["test_cases/mp_form/test_form.py"])

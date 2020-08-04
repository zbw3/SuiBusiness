#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File   : test_fake_form_data.py
# @Author : mocobk
# @Email  : mailmzb@qq.com
# @Time   : 2020/7/27 14:56
"""
该用例主要是为了快速构造旧版本的表单数据，以便观察是否有数据兼容问题出现
"""
import pytest

from ProductApi.MiniProgramForm.form.enum import FormStatus
from test_cases.mp_form import verify_create_form


def test_create_normal_activity_form(user1, default_activity_form):
    """创建正常进行中的 [活动接龙] 表单"""
    default_activity_form.set_title('进行中-含填写项')
    verify_create_form(user1, default_activity_form)


def test_create_normal_with_no_question_activity_form(user1, default_activity_form):
    """创建正常进行中的 [活动接龙] 表单"""
    default_activity_form.set_title('进行中-无填写项')
    default_activity_form.clear_questions()
    verify_create_form(user1, default_activity_form)


def test_create_paused_activity_form(user1, default_activity_form):
    """创建停止中的 [活动接龙] 表单"""
    default_activity_form.set_title('停止中-含填写项')
    form_id = verify_create_form(user1, default_activity_form)
    update_status_res = user1.v1_form_id_status_put(form_id, FormStatus.PAUSED.value)
    assert update_status_res.status_code == 204


def test_create_unopened_activity_form(user1, default_activity_form):
    """创建未开启的 [活动接龙] 表单"""
    default_activity_form.set_title('未开启-含填写项')
    default_activity_form.set_duration_time(start=default_activity_form.now_offset(days=1))
    verify_create_form(user1, default_activity_form)


def test_create_finished_activity_form(user1, default_activity_form):
    """创建已结束的 [活动接龙] 表单"""
    default_activity_form.set_title('已结束-含填写项')
    default_activity_form.set_duration_time(end=default_activity_form.now_offset(seconds=1))
    verify_create_form(user1, default_activity_form)


"""
=================================================================================================
"""


def test_create_normal_shopping_form(user1, default_shopping_form):
    """创建正常进行中的 [活动接龙] 表单"""
    default_shopping_form.set_title('进行中-含填写项')
    verify_create_form(user1, default_shopping_form)


def test_create_normal_with_no_question_shopping_form(user1, default_shopping_form):
    """创建正常进行中的 [活动接龙] 表单"""
    default_shopping_form.set_title('进行中-无填写项')
    default_shopping_form.clear_questions()
    verify_create_form(user1, default_shopping_form)


def test_create_paused_shopping_form(user1, default_shopping_form):
    """创建停止中的 [活动接龙] 表单"""
    default_shopping_form.set_title('停止中-含填写项')
    form_id = verify_create_form(user1, default_shopping_form)
    update_status_res = user1.v1_form_id_status_put(form_id, FormStatus.PAUSED.value)
    assert update_status_res.status_code == 204


def test_create_unopened_shopping_form(user1, default_shopping_form):
    """创建未开启的 [活动接龙] 表单"""
    default_shopping_form.set_title('未开启-含填写项')
    default_shopping_form.set_duration_time(start=default_shopping_form.now_offset(days=1))
    verify_create_form(user1, default_shopping_form)


def test_create_finished_shopping_form(user1, default_shopping_form):
    """创建已结束的 [活动接龙] 表单"""
    default_shopping_form.set_title('已结束-含填写项')
    default_shopping_form.set_duration_time(end=default_shopping_form.now_offset(seconds=1))
    verify_create_form(user1, default_shopping_form)


if __name__ == '__main__':
    pytest.main()

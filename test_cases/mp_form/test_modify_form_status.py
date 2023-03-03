#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : kse
# @Time   : 2023/3/3
import pytest
import time

from ProductApi.MiniProgramForm.api import FormApi
from ProductApi.MiniProgramForm.form import PostFormData
from test_cases.mp_form import verify_post_form_data, verify_put_form_data, verify_cancel_form_data, create_form
from ProductApi.MiniProgramForm.form.enum1 import FormStatus
from test_cases.mp_form import verify_post_form, create_form, create_form_data, create_numerous_form_data

@pytest.fixture()
def form_id(user1, default_activity_form):
    """创建正常进行中的 [活动接龙] 表单"""
    default_activity_form.set_title('修改表单状态测试')
    default_activity_form.set_cycle(127, 800, 1800)
    form_id = create_form(user1, default_activity_form)
    return form_id


def test_end_form(user1, form_id):
    """表单已结束"""
    user1.v1_form_id_status(form_id, "-1")
    res = user1.v1_form_profile(form_id)
    assert(res.data.get('data').get('status')) == -1

def test_pause_form(user1, form_id):
    """表单已暂停"""
    user1.v1_form_id_status(form_id, "-2")
    res = user1.v1_form_profile(form_id)
    assert(res.data.get('data').get('status')) == -2

def test_pause_form(user1, form_id):
    """表单已删除"""
    user1.v1_delete_forms([form_id])
    res = user1.v1_form_profile(form_id)
    assert(res.data.get('code')) == 13372

def test_open_form(user1, form_id):
    """表单已开启"""
    res = user1.v1_form_profile(form_id)
    # time.sleep(20)
    assert(res.data.get('data').get('status')) == 2

if __name__ == '__main__':
    pytest.main()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : mocobk
# @Email  : mailmzb@qq.com
# @Time   : 2020/8/5 16:18
import pytest

from ProductApi.MiniProgramForm.form.enum1 import FormStatus
from test_cases.mp_form import create_form


def test_activity_form_status(user1, default_activity_form):
    """验证首页瀑布流接龙的正确性"""
    default_activity_form.set_title('设置表单状态测试')
    form_id = create_form(user1, default_activity_form)

    res = user1.v1_form_id_status(form_id, FormStatus.PAUSED.value, method=user1.PUT)
    assert res.status_code == 204

    res = user1.v1_form_id_status(form_id, FormStatus.FINISHED.value, method=user1.PUT)
    assert res.status_code == 204

    res = user1.v1_form_id_status(form_id, FormStatus.OPENED.value, method=user1.PUT)
    assert res.status_code == 204

    res = user1.v1_form_id_status(form_id, FormStatus.DELETED.value, method=user1.PUT)
    assert res.status_code == 204


def test_shopping_form_status(user1, default_shopping_form):
    """验证首页瀑布流接龙的正确性"""
    default_shopping_form.set_title('设置表单状态测试')
    form_id = create_form(user1, default_shopping_form)

    res = user1.v1_form_id_status(form_id, FormStatus.PAUSED.value, method=user1.PUT)
    assert res.status_code == 204

    res = user1.v1_form_id_status(form_id, FormStatus.FINISHED.value, method=user1.PUT)
    assert res.status_code == 204

    res = user1.v1_form_id_status(form_id, FormStatus.OPENED.value, method=user1.PUT)
    assert res.status_code == 204

    res = user1.v1_form_id_status(form_id, FormStatus.DELETED.value, method=user1.PUT)
    assert res.status_code == 204


if __name__ == '__main__':
    pytest.main()

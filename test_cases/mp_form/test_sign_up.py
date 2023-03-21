#!/usr/bin/env python
# -*-coding: utf-8 -*-
# @File    : test_sign_up.py
# @Author  : myname
# @Email   : mailmzb@qq.com
# @Time    : 2023/3/21 9:27
import pytest


def test_sign_up(user1, default_formId_dataId_commentId):
    form_id = default_formId_dataId_commentId.form_id
    res = user1.v1_form_id_sign_up(form_id=form_id)
    assert res.status_code == 200


def test_form_id_sign_up(user1, default_formId_dataId_commentId):
    res = default_formId_dataId_commentId
    form_id = res.form_id
    form_data_id = res.form_data_id
    res = user1.v1_form_id_sign_up_form_data_id(form_id=form_id, form_data_id=form_data_id)
    assert res.status_code == 200


def test_sign_up_delete(user1, default_formId_dataId_commentId):
    res = default_formId_dataId_commentId
    form_id = res.form_id
    form_data_id = res.form_data_id
    user1.v1_form_id_sign_up_form_data_id(form_id=form_id, form_data_id=form_data_id)
    res = user1.v1_form_id_sign_up_delete(form_id, form_data_id)
    assert res.status_code == 200


if __name__ == '__main__':
    pytest.main()

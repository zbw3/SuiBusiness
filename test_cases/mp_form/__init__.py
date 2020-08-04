#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File   : __init__.py.py
# @Author : mocobk
# @Email  : mailmzb@qq.com
# @Time   : 2020/7/15 15:11
from ProductApi.MiniProgramForm.api import FormApi
from ProductApi.MiniProgramForm.form import PostFormData, PutFormData
from ProductApi.MiniProgramForm.form.form import Form
from libs.JsonUtils import json_diff


def verify_create_form(form_api: FormApi, form: Form) -> str:
    """
    :param form_api: FormApi Object
    :param form: Form Object
    :return: form_id
    """
    form_data = form.data
    res1 = form_api.v1_form(form_data, return_form_id=True)
    assert res1.status_code == 204
    res2 = form_api.v1_form_form_id_get(res1.form_id)
    assert res2.status_code == 200
    data = res2.data.get('data', {})
    assert data.get('type') == form_data['type']
    assert data.get('title') == form_data['title']
    assert data.get('contents') == form_data['contents']
    # catalog['status'] 0：正常，-1：删除，1：新增（临时），2：更新（临时）
    for catalog in form_data['catalogs']:
        for form_catalog in catalog['formCatalogs']:
            form_catalog['status'] = 0
        catalog['status'] = 0
    catalogs_diff = json_diff(form_data['catalogs'], data.get('catalogs', []))
    assert catalogs_diff == [], catalogs_diff
    return res1.form_id

def verify_post_form_data(user1, user2, form):
    assert form.status_code == 204
    form_id = form.form_id

    post_form_data = PostFormData(user1, form_id).data
    res = user1.v1_form_id_form_data_post(form_id, post_form_data)
    assert res.status_code == 200
    assert res.data['data']['sequence'] == 1

    post_form_data = PostFormData(user2, form_id).data
    res = user2.v1_form_id_form_data_post(form_id, post_form_data)
    assert res.status_code == 200
    assert res.data['data']['sequence'] == 2


def verify_put_form_data(user2, form):
    assert form.status_code == 204
    form_id = form.form_id
    has_form_data = user2.v1_form_id_form_data_get(form_id).data.get('data')

    if not has_form_data:
        post_form_data = PostFormData(user2, form_id).data
        res = user2.v1_form_id_form_data_post(form_id, post_form_data)
        assert res.status_code == 200

    put_form_data = PutFormData(user2, form_id).data
    res = user2.v1_form_id_form_data_put(form_id, put_form_data)
    assert res.status_code == 204
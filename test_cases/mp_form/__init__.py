#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File   : __init__.py.py
# @Author : mocobk
# @Email  : mailmzb@qq.com
# @Time   : 2020/7/15 15:11
import random
from collections import namedtuple
from contextlib import contextmanager

from ProductApi.MiniProgramForm.api import FormApi
from ProductApi.MiniProgramForm.form import PostFormData, PutFormData
from ProductApi.MiniProgramForm.form.enum import CatalogType, FormDataStatus
from ProductApi.MiniProgramForm.form.form import Form
from libs.JsonUtils import json_diff
from settings.BaseConfig import Env


@contextmanager
def no_authorized_hearders(user: FormApi):
    authorized_hearders = user.authorized_hearders
    user.authorized_hearders = {}
    yield
    user.authorized_hearders = authorized_hearders


def create_form(form_api: FormApi, form: Form) -> str:
    """
    :param form_api:
    :param form:
    :return: form_id
    """
    res = form_api.v1_form(form.data, return_form_id=True, method=form_api.POST)
    assert res.status_code == 204
    return res.form_id


def verify_post_form(form_api: FormApi, form: Form) -> str:
    """
    :param form_api: FormApi Object
    :param form: Form Object
    :return: form_id
    """
    form_data = form.data
    form_id = create_form(form_api, form)
    res = form_api.v1_form_form_id(form_id, method=form_api.GET)
    assert res.status_code == 200
    data = res.data.get('data', {})
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
    return form_id


def verify_put_form(form_api: FormApi, form: Form) -> str:
    """
    :param form_api: FormApi Object
    :param form: Form Object
    :return: form_id
    """
    form_id = create_form(form_api, form)
    form_detail_res = form_api.v1_form_form_id(form_id, method=form_api.GET)
    assert form_detail_res.status_code == 200
    data = form_detail_res.data.get('data', {})

    # 修改表单内容
    modify_form = Form(form.TYPE)
    modify_form.set_title('测试修改后的表单')
    modify_form.CONTENTS = data.get('contents', [])[:-1]
    modify_form.CATALOGS = [catalog for catalog in data.get('catalogs', []) if
                            CatalogType(catalog['catalogType']) not in [CatalogType.BUYER_REMARKS,
                                                                        CatalogType.SELLER_REMARKS]][:-1]
    modify_form.CONFIG = data.get('config')
    # 请求修改表单接口
    modify_form_res = form_api.v1_form_form_id(form_id, modify_form.data, method=form_api.PUT)
    assert modify_form_res.status_code == 204
    modified_form_detail_res = form_api.v1_form_form_id(form_id, method=form_api.GET)
    form_data_diff = json_diff(modify_form.data, modified_form_detail_res.data.get('data', {}))
    assert form_data_diff == [], form_data_diff
    return form_id


def create_form_data(form_api: FormApi, form_id: str) -> int:
    """
    :param form_api:
    :param form_id:
    :return: sequence
    """
    post_form_data = PostFormData(form_api, form_id).data
    res = form_api.v1_form_id_form_data(form_id, post_form_data, method=form_api.POST)
    assert res.status_code == 200
    return res.data.get('data', {}).get('sequence')


def create_numerous_form_data(*form_api: FormApi, form_id: str, number: int):
    """
    连续创建多个接龙数据
    :param form_api:
    :param form_id:
    :param number:
    :return:
    """
    for _ in range(number):
        create_form_data(random.choice(form_api), form_id)


def get_form_data(form_api: FormApi, form_id: str, index=0) -> dict:
    res = form_api.v1_form_id_form_data(form_id, method=form_api.GET)
    assert res.status_code == 200
    form_datas = res.data.get('data')
    if form_datas:
        return form_datas[index]
    else:
        return {}


def verify_post_form_data(user1: FormApi, user2: FormApi, form_id: str):
    sequence = create_form_data(user1, form_id)
    assert sequence == 1

    sequence = create_form_data(user2, form_id)
    assert sequence == 2


def verify_put_form_data(form_api, form_id: str):
    if not get_form_data(form_api, form_id):
        create_form_data(form_api, form_id)

    put_form_data = PutFormData(form_api, form_id).data
    res = form_api.v1_form_id_form_data(form_id, put_form_data, method=form_api.PUT)
    assert res.status_code == 204
    modified_form_data = get_form_data(form_api, form_id)

    put_form_data.pop('formVersion')  # 对比时排除 formVersion 字段
    form_data_diff = json_diff(put_form_data, modified_form_data)
    assert form_data_diff == [], form_data_diff


def verify_cancel_form_data(form_api: FormApi, form_id: str):
    if not get_form_data(form_api, form_id):
        create_form_data(form_api, form_id)

    form_data_id = get_form_data(form_api, form_id)['fid']

    res = form_api.v1_form_id_form_data(form_id, form_data_id=form_data_id, method=form_api.DELETE)
    assert res.status_code == 204

    deleted_form_data = get_form_data(form_api, form_id)
    assert FormDataStatus(deleted_form_data['status']) == FormDataStatus.CANCELED


def get_invitation_code(releaser: FormApi, form: Form):
    """
    :param releaser: 发布者 api
    :param form: 表单对象
    :return: namedtuple
    """
    form_id = create_form(releaser, form)
    response = releaser.v1_form_manager_invitation_code(form_id, method=releaser.GET)
    assert response.status_code == 200, response.text
    assert Env().is_test, f'仅支持在测试环境中测试，当前环境为：${Env().cur_env.value}'
    code_str: str = response.data.get('data', {}).get('codeStr')
    assert code_str
    fid, code = code_str.split(',')
    invitation = namedtuple('invitation', ['response', 'fid', 'code', 'form_id'])
    return invitation(response, fid, code, form_id)


def is_user_in_managers_list(form_id, releaser: FormApi, user: FormApi):
    """
    判断用户是否在管理员列表中
    :param form_id: 表单id
    :param releaser: 发布者 api
    :param user: 管理员
    :return: bool
    """
    reponse = releaser.v1_form_managers_form_id(form_id)
    assert reponse.status_code == 200, reponse.text
    data: list = reponse.data.get('data', [])
    is_in_managers_list = list(filter(lambda item: item['fid'] == form_id and item['fuid'] == user.fuid, data))
    return len(is_in_managers_list) == 1

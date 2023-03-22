#!/usr/bin/env python
# -*-coding: utf-8 -*-
# @File    : test_recycle_delete.py
# @Author  : myname
# @Email   : mailmzb@qq.com
# @Time    : 2023/3/21 16:34
import pytest

from ProductApi.MiniProgramForm.form.enum1 import FormStatus
from test_cases.mp_form import verify_post_form
"""数据清理相关接口"""


@pytest.fixture()
def form_id(user1, default_formId_dataId_commentId):
    """创建表单，返回表单id"""
    form_id = default_formId_dataId_commentId.form_id
    return form_id


@pytest.fixture()
def group_id(user1):
    """创建群组，返回群组id"""
    res = user1.v1_group('test_group', 'ORDINARY_GROUP', method=user1.POST)
    group_id = res.data.get('data')['groupId']
    return group_id


def test_delete_form_data(user1, default_formId_dataId_commentId):
    """验证报名数据清理"""
    res = default_formId_dataId_commentId
    form_id = res.form_id
    form_data_id = res.form_data_id
    res = user1.v1_form_data_delete(form_id=form_id, form_data_id=form_data_id)
    assert res.status_code == 200


def test_recycle_forms(user1):
    """验证回收站列表"""
    res = user1.v1_recycle_forms(group_id='', page_no=1, page_size=20)
    assert res.status_code == 200

    forms = res.data.get('data')
    # # 分页测试
    if len(forms) > 5:
        res = user1.v1_recycle_forms(group_id='', page_no=2, page_size=5, method=user1.GET)
        assert res.status_code == 200


def test_recycle_forms_group(user1, group_id):
    """验证群组内回收站列表"""
    # res = user1.v1_group('test_group', 'ORDINARY_GROUP', method=user1.POST)
    # group_id = res.data.get('data')['groupId']
    res = user1.v1_recycle_forms(group_id=group_id, page_no=1, page_size=20)
    assert res.status_code == 200

    forms = res.data.get('data')
    # # 分页测试
    if len(forms) > 5:
        res = user1.v1_recycle_forms(group_id=group_id, page_no=2, page_size=5, method=user1.GET)
        assert res.status_code == 200


def test_recycle_form_all(user1, group_id):
    """验证一键恢复"""
    # 群组外一键恢复
    res = user1.v1_recycle_form_all(group_id='', method=user1.PUT)
    assert res.status_code == 200
    # 群组内一键恢复
    res = user1.v1_recycle_form_all(group_id=group_id, method=user1.PUT)
    assert res.status_code == 200


def test_recycle_form_all_delete(user1, group_id):
    """验证一键删除"""
    # 群组外一键删除
    res = user1.v1_recycle_form_all(group_id='', method=user1.DELETE)
    assert res.status_code == 200
    # 群组内一键删除
    res = user1.v1_recycle_form_all(group_id=group_id, method=user1.DELETE)
    assert res.status_code == 200


def test_recycle_form(user1, default_formId_dataId_commentId):
    """验证删除回收站post"""
    user1.v1_recycle_form_all(method=user1.PUT)  # 避免删除掉其他表单，先一键恢复回收站
    # 新建删除个表单
    form_id = default_formId_dataId_commentId.form_id

    user1.v1_form_id_status(form_id=form_id, status=FormStatus.DELETED.value, method=user1.PUT)
    res = user1.v1_recycle_form(group_id='', form_id=form_id, method=user1.POST)
    assert res.status_code == 200


def test_recycle_form_group(user1, group_id, default_activity_form):
    """验证删除群组内的回收站 post"""
    group_id1 = group_id
    default_activity_form.set_title('群组内删除表单')  # 新建删除个表单
    default_activity_form.set_group_id(group_id1)
    form_id = verify_post_form(user1, default_activity_form)
    user1.v1_form_id_status(form_id=form_id, status=FormStatus.DELETED.value, method=user1.PUT)  # 删除表单
    res1 = user1.v1_recycle_form(group_id=group_id1, form_id=form_id, method=user1.POST)
    assert res1.status_code == 200


def test_recycle_form_delete(user1, default_formId_dataId_commentId):
    """验证恢复回收站put"""
    # 新建删除个表单
    form_id = default_formId_dataId_commentId.form_id

    user1.v1_form_id_status(form_id=form_id, status=FormStatus.DELETED.value, method=user1.PUT)
    res = user1.v1_recycle_form(group_id='', form_id=form_id, method=user1.PUT)
    assert res.status_code == 200


def test_recycle_form_group_delete(user1, group_id, default_activity_form):
    """验证恢复群组内的回收站 post"""
    group_id1 = group_id
    default_activity_form.set_title('群组内删除表单')  # 新建删除个表单
    default_activity_form.set_group_id(group_id1)
    form_id = verify_post_form(user1, default_activity_form)
    user1.v1_form_id_status(form_id=form_id, status=FormStatus.DELETED.value, method=user1.PUT)  # 删除表单
    res1 = user1.v1_recycle_form(group_id=group_id1, form_id=form_id, method=user1.PUT)
    assert res1.status_code == 200




if __name__ == '__main__':
    pytest.main()

#!/usr/bin/env python
# -*-coding: utf-8 -*-
# @File    : test_recycle_delete.py
# @Author  : myname
# @Email   : mailmzb@qq.com
# @Time    : 2023/3/21 16:34
import pytest

"""数据清理相关接口"""


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


def test_recycle_forms_group(user1):
    """验证群组内回收站列表"""
    res = user1.v1_group('test_group', 'ORDINARY_GROUP', method=user1.POST)
    group_id = res.data.get('data')['groupId']
    res = user1.v1_recycle_forms(group_id=group_id, page_no=1, page_size=20)
    assert res.status_code == 200

    forms = res.data.get('data')
    # # 分页测试
    if len(forms) > 5:
        res = user1.v1_recycle_forms(group_id=group_id, page_no=2, page_size=5, method=user1.GET)
        assert res.status_code == 200


if __name__ == '__main__':
    pytest.main()

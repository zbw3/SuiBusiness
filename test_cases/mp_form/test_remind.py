#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : ksw
# @Time   : 2023/03/21 16:00
import pytest

"""表单提醒相关测试用例"""


def test_remind(user1, default_formId_dataId_commentId):
    """验证【获取表单公众号通知配置】接口"""
    form_id = default_formId_dataId_commentId.form_id
    res = user1.v1_form_remind_get(form_id)
    assert res.status_code == 200


def test_modify_remind(user1, default_formId_dataId_commentId):
    """验证【表单公众号通知配置】接口"""
    form_id = default_formId_dataId_commentId.form_id
    user1.v1_form_remind(form_id, True, 700, 1, 1, 1, 1, 1, 0, 0)
    res = user1.v1_form_remind_get(form_id)
    assert res.status_code == 200
    assert res.data.get('data')['active'] is True
    assert res.data.get('data')['timeOfDay'] == 700
    assert res.data.get('data')['monday'] == 1
    assert res.data.get('data')['sunday'] == 0


if __name__ == '__main__':
    pytest.main()

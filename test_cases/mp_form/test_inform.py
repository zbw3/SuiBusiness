#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : ksw
# @Time   : 2023/03/21 10:00

import pytest

"""表单通知相关接口测试用例"""


def test_imform(user1, default_formId_dataId_commentId):
    """验证【获取表单公众号通知配置】接口"""
    form_id = default_formId_dataId_commentId.form_id
    res = user1.v1_form_inform_get(form_id)
    assert res.status_code == 200


def test_modify_imform(user1, default_formId_dataId_commentId):
    """验证【表单公众号通知配置】接口"""
    form_id = default_formId_dataId_commentId.form_id
    user1.v1_form_inform_input(form_id, True, True, True, False)
    res = user1.v1_form_inform_get(form_id)
    assert res.status_code == 200
    assert res.data.get('data')['addition'] is True
    assert res.data.get('data')['comment'] is False


if __name__ == '__main__':
    pytest.main()

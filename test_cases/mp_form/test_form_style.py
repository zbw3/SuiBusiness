#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2023/3/21 16:52
# @Author : ksw
# @FileName: test_form_style.py

import pytest


def test_form_style(user1, default_formId_dataId_commentId):
    """验证【页面样式配置是否显示题目标题等】接口"""
    form_id = default_formId_dataId_commentId.form_id
    res = user1.v1_form_id_page_style(form_id, True, True, False)
    res2 = user1.v3_form_form_id(form_id)
    print(res2)
    assert res.status_code == 204, res.status_code
    assert res2.data.get('data')['config']['pageStyle']['showRecordQuestionTitle'] is True
    assert res2.data.get('data')['config']['pageStyle']['showFlowStatusFilter'] is True
    assert res2.data.get('data')['config']['pageStyle']['showQuickPsRateEntrance'] is False


if __name__ == '__main__':
    pytest.main()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : mocobk
# @Email  : mailmzb@qq.com
# @Time   : 2020/8/5 16:18
import pytest


def test_get_participation_forms(user1):
    """验证【我的】——我参与的表单列表获取正确性"""
    params = {'pageNo': 1, 'pageSize': 20}
    res = user1.v1_participation_forms(params=params, method=user1.GET)
    assert res.status_code == 200

    forms = res.data.get('data', {}).get('participationForms')
    # 分页测试
    if len(forms) > 5:
        params = {'pageNo': 2, 'pageSize': 5}
        res = user1.v1_participation_forms(params=params, method=user1.GET)
        assert res.status_code == 200
        # forms = res.data.get('data', {}).get('participationForms')
        # print("forms----------------",forms)
        # print("++++++++++++++",len(forms))
        # assert 1 <= len(forms) <= 5


if __name__ == '__main__':
    pytest.main()

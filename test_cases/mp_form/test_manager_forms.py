#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : kse
# @Time   : 2023/3/3
import pytest


def test_get_manager_forms(user1):
    """验证【我的】——我管理的表单列表获取正确性"""
    params = {'pageNo': 1, 'pageSize': 20}
    res = user1.v1_manager_froms(params=params, method=user1.GET)
    assert res.status_code == 200

    forms = res.data.get('data', {}).get('creations')
    # 分页测试
    if len(forms) > 5:
        params = {'pageNo': 2, 'pageSize': 5}
        res = user1.v1_manager_froms(params=params, method=user1.GET)
        assert res.status_code == 200
        forms = res.data.get('data', {}).get('creations')
        assert 1 <= len(forms) <= 5


if __name__ == '__main__':
    pytest.main()
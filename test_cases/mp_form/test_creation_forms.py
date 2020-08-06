#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : mocobk
# @Email  : mailmzb@qq.com
# @Time   : 2020/8/5 16:18
import jmespath
import pytest


def test_get_creation_forms(user1):
    """验证【我的】——我创建的表单列表获取正确性"""
    params = {'pageNo': 1, 'pageSize': 20}
    res = user1.v1_creation_forms(params=params, method=user1.GET)
    assert res.status_code == 200

    forms = jmespath.search('@.data.creations.*[*][]', res.data)
    # 分页测试
    if len(forms) > 5:
        params = {'pageNo': 2, 'pageSize': 5}
        res = user1.v1_creation_forms(params=params, method=user1.GET)
        assert res.status_code == 200
        forms = jmespath.search('@.data.creations.*[*][]', res.data)
        assert 1 <= len(forms) <= 5


if __name__ == '__main__':
    pytest.main()

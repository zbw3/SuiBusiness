#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : mocobk
# @Email  : mailmzb@qq.com
# @Time   : 2020/8/5 16:18
import pytest

@pytest.mark.skip('原首页瀑布流接口已弃用')
def test_get_examples_form(user1):
    """验证首页瀑布流接龙的正确性"""
    res = user1.v1_examples(method=user1.GET)
    assert res.status_code == 200
    data = res.data.get('data')
    assert len(data) > 0


if __name__ == '__main__':
    pytest.main()

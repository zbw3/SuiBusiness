#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : mocobk
# @Email  : mailmzb@qq.com
# @Time   : 2020/10/26 13:39
import pytest
from test_cases.mp_form import get_invitation_code, is_user_in_managers_list

def test_get_form_managers(user1):
    """验证获取表单管理员列表"""
    pass


def test_get_form_manager_poster(user1):
    """验证获取管理员邀请海报信息"""
    pass




def test_form_manager_invitation_code(user1, user2, default_activity_form):
    """验证生成管理员邀请码"""
    data = get_invitation_code(user1, default_activity_form)
    assert data.code != "", data.code


def test_form_manager(user1, user2, default_activity_form):
    """验证扫码加入管理员"""
    data = get_invitation_code(user1, default_activity_form)
    if not is_user_in_managers_list(data.form_id, user1, user2):
        res = user2.v1_form_manager(data.fid, data.code)
        assert res.status_code == 200, res.data





if __name__ == '__main__':
    pytest.main()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : ksw
# @Time   : 2023/02/14 15:09

"""
群组相关接口的测试用例
"""

import pytest
from test_cases.mp_form import verify_post_form


def test_group(user1):
    """验证【创建群组】接口"""
    response = user1.v1_group('test_group', 'ORDINARY_GROUP', method=user1.POST)
    assert response.status_code == 200, response.text


def test_put_group(user1):
    """验证【修改群组】接口"""
    res1 = user1.v1_group('test_group', 'ORDINARY_GROUP', method=user1.POST)
    group_id = res1.data.get('data')['groupId']
    res2 = user1.v1_group_operate_put(group_id, 'group', 'SECTORAL_GROUP', method=user1.PUT)
    assert res2.status_code == 200, res2.text
    assert res2.data.get('data')['groupName'] == 'group'


def test_delete_group(user1):
    """验证【删除群组】接口"""
    res1 = user1.v1_group('test_group', 'ORDINARY_GROUP', method=user1.POST)
    group_id = res1.data.get('data')['groupId']
    res2 = user1.v1_group_operate(group_id, method=user1.DELETE)
    assert res2.status_code == 200


def test_get_group(user1):
    """验证【获取群组详细信息】接口"""
    res1 = user1.v1_group('test_group', 'ORDINARY_GROUP', method=user1.POST)
    group_id = res1.data.get('data')['groupId']
    res2 = user1.v1_group_operate(group_id, method=user1.GET)
    assert res2.status_code == 200, res2.text
    assert res2.data.get('data')['groupName'] == 'test_group'


def test_invite(user1):
    """验证【生成群组邀请码】接口"""
    res1 = user1.v1_group('test_group', 'ORDINARY_GROUP', method=user1.POST)
    group_id = res1.data.get('data')['groupId']
    res2 = user1.v1_group_invite(group_id, method=user1.GET)
    assert res2.status_code == 200
    pwd = res2.data.get('data')['invitePassword']
    assert len(pwd) > 0


def test_join_group(user1, user2):
    """验证【加入群组】接口"""
    res1 = user1.v1_group('test_group', 'ORDINARY_GROUP', method=user1.POST)
    group_id = res1.data.get('data')['groupId']
    res2 = user1.v1_group_invite(group_id, method=user1.GET)
    pwd = res2.data.get('data')['invitePassword']
    res3 = user2.v1_join_group(group_id, pwd, method=user2.POST)
    assert res3.status_code == 200
    assert len(res3.data.get('data')) > 0


def test_group_member(user1, user2):
    """验证【群组成员列表】接口"""
    res1 = user1.v1_group('test_group', 'ORDINARY_GROUP', method=user1.POST)
    group_id = res1.data.get('data')['groupId']
    res2 = user1.v1_group_invite(group_id, method=user1.GET)
    pwd = res2.data.get('data')['invitePassword']
    res3 = user2.v1_join_group(group_id, pwd, method=user2.POST)
    res4 = user1.v1_get_group_member(group_id)
    assert len(res4.data.get('data')['members']) == 2


def test_modify_group_member_info(user1, user2):
    """验证【修改群成员信息】接口"""
    res1 = user1.v1_group('test_group', 'ORDINARY_GROUP', method=user1.POST)
    group_id = res1.data.get('data')['groupId']
    res2 = user1.v1_group_invite(group_id, method=user1.GET)
    pwd = res2.data.get('data')['invitePassword']
    fuid = user2.v1_join_group(group_id, pwd, method=user2.POST).data.get('data')['fuid']
    res = user1.v1_put_group_member(group_id, fuid, '自动修改的群昵称')
    assert res.data.get('data')['groupNickname'] == '自动修改的群昵称'


def test_unsubscribe_list(user1, user2):
    """验证【未关注公众号群成员列表】"""
    res1 = user1.v1_group('test_group', 'ORDINARY_GROUP', method=user1.POST)
    group_id = res1.data.get('data')['groupId']
    res2 = user1.v1_group_invite(group_id, method=user1.GET)
    pwd = res2.data.get('data')['invitePassword']
    user2.v1_join_group(group_id, pwd, method=user2.POST)
    res = user1.v1_group_unsubscribe_list(group_id)
    assert res.status_code == 200
    assert res.data.get('data')['unsubNum'] == 1


def test_member_info(user1):
    """验证【获取群成员基本信息】接口"""
    res1 = user1.v1_group('test_group', 'ORDINARY_GROUP', method=user1.POST)
    group_id = res1.data.get('data')['groupId']
    res = user1.v1_group_member_info(group_id)
    assert res.status_code == 200


def test_quit_group(user1, user2):
    """验证【退出群组】接口"""
    res1 = user1.v1_group('test_group', 'ORDINARY_GROUP', method=user1.POST)
    group_id = res1.data.get('data')['groupId']
    res2 = user1.v1_group_invite(group_id, method=user1.GET)
    pwd = res2.data.get('data')['invitePassword']
    user2.v1_join_group(group_id, pwd, method=user2.POST)
    res3 = user2.v1_quit_group(group_id, method=user2.POST)
    assert res3.status_code == 200


def test_remove_group_member(user1, user2):
    """验证【移除群组成员】接口"""
    res1 = user1.v1_group('test_group', 'ORDINARY_GROUP', method=user1.POST)
    group_id = res1.data.get('data')['groupId']
    res2 = user1.v1_group_invite(group_id, method=user1.GET)
    pwd = res2.data.get('data')['invitePassword']
    fuid = user2.v1_join_group(group_id, pwd, method=user2.POST).data.get('data')['fuid']
    res3 = user1.v1_delete_group_member(group_id, fuid, method=user1.DELETE)
    assert res3.status_code == 200


def test_group_forms(user1, default_activity_form):
    """验证【群组内表单列表】接口"""
    res1 = user1.v1_group('test_group', 'ORDINARY_GROUP', method=user1.POST)
    group_id = res1.data.get('data')['groupId']
    default_activity_form.set_title('群组内表单')
    default_activity_form.set_group_id(group_id)
    verify_post_form(user1, default_activity_form)
    assert len(user1.v1_group_forms(group_id).data.get('data')['formList']) == 1


def test_group_list(user1):
    """验证【（个人）群组列表】接口"""
    user1.v1_group('test_group', 'ORDINARY_GROUP', method=user1.POST)
    res = user1.v1_group_list()
    assert res.status_code == 200, res.text


def test_add_group_admin(user1, user2):
    """验证【添加管理员】接口"""
    res1 = user1.v1_group('test_group', 'ORDINARY_GROUP', method=user1.POST)
    group_id = res1.data.get('data')['groupId']
    res2 = user1.v1_group_invite(group_id, method=user1.GET)
    pwd = res2.data.get('data')['invitePassword']
    fuid = user2.v1_join_group(group_id, pwd, method=user2.POST).data.get('data')['fuid']
    res = user1.v1_add_admin(group_id, fuid)
    assert res.status_code == 200


def test_remove_group_admin(user1, user2):
    """验证【移除管理员】接口"""
    res1 = user1.v1_group('test_group', 'ORDINARY_GROUP', method=user1.POST)
    group_id = res1.data.get('data')['groupId']
    res2 = user1.v1_group_invite(group_id, method=user1.GET)
    pwd = res2.data.get('data')['invitePassword']
    fuid = user2.v1_join_group(group_id, pwd, method=user2.POST).data.get('data')['fuid']
    user1.v1_add_admin(group_id, fuid)
    res = user1.v1_remove_admin(group_id, fuid)
    assert res.status_code == 200


if __name__ == '__main__':
    pytest.main()

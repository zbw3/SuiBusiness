#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : ksw
# @Time   : 2023/02/14 15:09

import pytest

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
    res2 = user1.v1_group_invite(group_id,method=user1.GET)
    assert res2.status_code == 200
    pwd = res2.data.get('data')['invitePassword']
    assert len(pwd) > 0


if __name__ == '__main__':
    pytest.main()


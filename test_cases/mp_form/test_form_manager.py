#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : mocobk
# @Email  : mailmzb@qq.com
# @Time   : 2020/10/26 13:39
import pytest

from test_cases.mp_form import get_invitation_code, no_authorized_hearders, is_user_in_managers_list


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


def test_get_form_managers(user1, user2, user3, default_shopping_form, default_activity_form):
    """验证获取表单管理员列表"""
    default_shopping_form.set_title('测试获取表单管理员列表')
    default_activity_form.set_title('测试获取表单管理员列表')
    for form in [default_shopping_form, default_activity_form]:
        invitation = get_invitation_code(user1, form)
        reponse1 = user1.v1_form_managers_form_id(invitation.form_id, user1.GET)
        data: list = reponse1.data.get('data')
        assert len(data) == 0, reponse1.text

        response2 = user2.v1_form_manager(invitation.fid, invitation.code, user2.POST)
        response3 = user3.v1_form_manager(invitation.fid, invitation.code, user3.POST)
        assert response2.status_code == 200 and response3.status_code == 200

        reponse1 = user1.v1_form_managers_form_id(invitation.form_id, user1.GET)
        data: list = reponse1.data.get('data')
        assert len(data) == 2, reponse1.text


def test_get_form_managers_by_other(user1, user2, user3, default_shopping_form, default_activity_form):
    """验证非发布者（管理员/参与者）请求正确的表单管理员列表数据，响应约定的错误码"""
    default_shopping_form.set_title('测试非发布者获取表单管理员列表')
    default_activity_form.set_title('测试非发布者获取表单管理员列表')
    for form in [default_shopping_form, default_activity_form]:
        invitation = get_invitation_code(user1, form)
        # 管理员请求管理员列表数据
        response = user2.v1_form_manager(invitation.fid, invitation.code, user2.POST)
        assert response.status_code == 200, response.text
        response = user2.v1_form_managers_form_id(invitation.form_id, user2.GET)
        assert response.status_code == 422, response.text
        assert response.data.get('code') == 13381, response.text

        # 普通用户请求管理员列表数据
        response = user3.v1_form_managers_form_id(invitation.form_id, user3.GET)
        assert response.status_code == 422, response.text
        assert response.data.get('code') == 13381, response.text

        # 未登录用户将头请求管理员列表数据
        with no_authorized_hearders(user3):
            response = user3.v1_form_managers_form_id(invitation.form_id, user3.GET)
            assert response.status_code == 400, response.text


def test_get_form_manager_poster(user1, user2, user3, default_shopping_form, default_activity_form):
    """"验证获取管理员邀请海报信息"""
    default_shopping_form.set_title('测试获取管理员邀请海报信息')
    default_activity_form.set_title('测试获取管理员邀请海报信息')
    for form in [default_shopping_form, default_activity_form]:
        invitation = get_invitation_code(user1, form)

        # 发布人请求邀请海报信息
        response = user1.v1_form_manager(invitation.fid, invitation.code, user1.POST)
        assert response.status_code == 422, response.text
        assert response.data.get('code') == 13419, response.text

        # 管理员请求邀请海报信息
        response = user2.v1_form_manager(invitation.fid, invitation.code, user2.POST)
        assert response.status_code == 200, response.text
        response = user2.v1_form_manager_poster(invitation.fid, user2.GET)
        assert response.status_code == 200, response.text

        # 普通用户请求邀请海报信息
        response = user3.v1_form_manager_poster(invitation.fid, user3.GET)
        assert response.status_code == 200, response.text
        data = response.data.get('data')
        assert data
        assert data['formId'] == invitation.form_id
        assert data['title'] == form.TITLE

        # 未登录用户将头请求管理员列表数据
        with no_authorized_hearders(user3):
            response = user3.v1_form_managers_form_id(invitation.form_id, user3.GET)
            assert response.status_code == 400, response.text


if __name__ == '__main__':
    pytest.main()

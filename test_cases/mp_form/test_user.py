#!/usr/bin/env python
# -*-coding: utf-8 -*-
# @File    : test_user.py
# @Author  : myname
# @Email   : mailmzb@qq.com
# @Time    : 2023/3/14 18:13
"""
用户相关接口
"""
import pytest


def test_v1_test_info(user1):
    """
    用户信息接口
    :param user1:
    :return:
    """
    res = user1.v1_user_info()
    assert res.status_code == 200


def test_v1_userinfo(user1):
    """
    更新用户信息
    :param user1:
    :return:
    """
    res = user1.v1_userinfo(nickname='百威', avatar_url='https://thirdwx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTKYvA15PvbH51SWh6BLgNm7swSGYtMxxicHVjm4PagjYtbGno3ljamv7jOTgicpKJDYS5mjyrAFb0wQ/132')
    assert res.status_code == 204


if __name__ == '__main__':
    pytest.main()
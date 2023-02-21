# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time: 2023/2/21 10:59

"""
开放api 相关接口的测试用例
"""

import pytest


def test_signup_developer(user1,phone="13265484102"):
    """
    注册成为开发者接口的测试用例

    :param user1:
    :param phone: 注册开发者的手机号
    :return:
    """
    response = user1.v1_open_api_sign_up_developer(phone=phone)
    assert response.status_code == 200 or 422




def test_v1_developer(user1):
    """
    获取开发者信息
    :param user1:
    :return:
    """
    response = user1.v1_developer()
    assert response.status_code == 200
    assert response.data.get("data")["appId"],response
    assert response.data.get("data")["secret"],response




if __name__ == '__main__':
    pytest.main()
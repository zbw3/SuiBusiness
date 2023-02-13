#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : mocobk
# @Email  : mailmzb@qq.com
# @Time   : 2020/11/25 15:09

import pytest


def test_v1_config(user1):
    response = user1.v1_config(method=user1.GET)
    assert response.status_code == 200,response.text
    # assert response.data.get('data'), response.text
    assert response.data.get('appConfig'), response.text


def test_wx_mp_link(user1):
    response = user1.wx_mp_link(method=user1.GET)
    assert response.status_code == 200,response.text
    assert response.data.get("data")

def test_operation_position(user1):
    response = user1.v1_operation_position(method=user1.GET)
    assert response.status_code == 200, response.text
    data = response.data.get('data')
    if data and data.get('status') != -1:
        assert data.get('image')
        if data.get('linkType') == 'WX_MEDIA_PLATFORM':
            assert data.get('linkUrl')
        else:
            assert not data.get('linkUrl')


if __name__ == '__main__':
    pytest.main()

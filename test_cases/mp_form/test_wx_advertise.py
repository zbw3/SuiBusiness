# -*- coding utf-8 -*-
# @Time    : 2023/2/28 15:19
# @Author  : muzi
# @File    : test_wx_advertise.py
# Software : PyCharm
# Explain  : 流量主广告配置

import pytest

def test_wx_advertise(user1):

    response = user1.v1_wx_advertise(method=user1.GET)
    assert response.status_code == 200, response.text


if __name__ == '__main__':
    pytest.main(["test_wx_advertise.py::test_wx_advertise"])
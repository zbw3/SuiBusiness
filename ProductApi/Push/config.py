#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File   : __init__.py.py
# @Author : mocobk
# @Email  : mailmzb@qq.com
# @Time   : 2020/3/23 14:56
"""
http://swagger.sui.work/pass/apidoc/share/show.htm?shareKey=8884a371f0d097c2c0b8540492c243c5#!/%E6%96%B0%E5%9C%B0%E6%8E%A8%E4%B8%9A%E5%8A%A1/get_v1_push_staff_info
"""
from settings.HostName import BizBook


class Test:
    HOSTNAME = BizBook.TEST

    class Url:
        v1_push_staff_info = '/v1/push/staff_info'
        v1_push_staffs = '/v1/push/staffs'
        v1_push_agent_enter = '/v1/push/agent_enter'
        v1_push_agents_agent_detail = '/v1/push/agents/agent_detail'
        v1_push_staff_profit = '/v1/push/staff/profit'
        v1_push_staff_openInfo = '/v1/push/staff/openInfo'
        v1_push_staff_image = '/v1/push/staff/image'


class Production:
    HOSTNAME = BizBook.PROD

    class Url(Test.Url):
        pass
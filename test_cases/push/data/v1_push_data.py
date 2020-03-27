#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File   : v1_push.py
# @Author : mocobk
# @Email  : mailmzb@qq.com
# @Time   : 2020/3/26 18:43
from settings import Account
from settings.BaseConfig import PROJECT_PATH
import requests


class StaffInfoData:
    class Data1:
        account = Account.user_119  # 资质未通过审核的用户
        trading_entity = '3604098'
        keys = ['name', 'enter_type', 'staff_id', 'agent_name', 'agent_id', 'can_login', 'status', 'role_type']


class StaffsData:
    class Data1:
        account = Account.user_119  # 资质未通过审核的用户
        trading_entity = '3604098'
        params = {
            "name": "motest",
            "id_card": "430528199608306197",
            "id_card_front_img": "string,地推人员身份证正面照片",
            "id_card_bak_img": "string,地推人员身份证背面照片",
            "phone": "18566772480",
            "agent_code": ""
        }


class AgentEnterData:
    class Data1:
        account = Account.user_119  # 资质未通过审核的用户
        trading_entity = '3604098'
        params = {
            "name": "motest",
            "business_card_img": "string,供应商管理人员名片照片",
            "agent_name": "string,供应商名称",
            "remark": "string，备注",
            "phone": "18566772480",
            "wechat_id": "no_id"
        }


class AgentsAgentDetailData:
    class Data1:
        account = Account.user_119  # 资质未通过审核的用户
        trading_entity = '3604098'


class StaffProfitData:
    class Data1:
        account = Account.user_119  # 资质未通过审核的用户
        trading_entity = '3604098'
        keys = ['transaction', 'open_commit', 'open_success']


class StaffOpenInfoData:
    class Data1:
        account = Account.user_119  # 资质未通过审核的用户
        trading_entity = '3604098'
        keys = ['transaction', 'open_commit', 'open_success']


class StaffImageData:

    class Data1:
        image = requests.get('http://mocobk.test.upcdn.net/image/20200327154152047.jpg', stream=True)

        account = Account.user_119  # 资质未通过审核的用户
        trading_entity = '3604098'
        keys = ['transaction', 'open_commit', 'open_success']
        params = {
            'image_file': ('img.jpg', image.content, 'image/jpeg'),
            'image_type': 1
        }

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File   : BaseConfig.py
# @Author : mocobk
# @Email  : mailmzb@qq.com
# @Time   : 2019/12/23 14:21
import os
from libs.logger import Logger


class SuiConfig:
    PASSWORD = {
        "123456": "7bca5282a041ca8bbd12ec2d98c83f30"
    }

    HEADERS = {
        "Client-Key": "C18191004B04494491C24EA8551C9D42",
        "Nonce-Str": "b37fb0c0eaad439aa352b894a3da2f38",
        "Sign": "cef6748001244411ccedc059d6785f1f",
        "Minor-Version": "1",
        "User-Agent": "MyMoney/10.6.1.5 (samsung/SM-N9005; Android/4.4.2; feidee)",
        "Device": "{'platform': 'Android', 'device_id': 'deviceId-358022020240216', 'model': 'SM-N9005', "
                  "'product_version': '10.6.1.5', 'locale': 'zh_CN', 'product_name': 'MyMoney For Feidee', "
                  "'os_version': '4.4.2'}",
    }


class Project:
    # 项目根目录
    path = os.path.abspath(os.path.dirname(__file__) + '/..')


# Api 默认日志级别
API_LOGGER_LEVEL = Logger.INFO

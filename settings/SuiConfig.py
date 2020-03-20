#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File : SuiConfig.py
# @Author: GoGo
# @Date : 2020/3/19
# @Desc :


class SuiConfig:
    HEADERS = {
        "Client-Key": "C18191004B04494491C24EA8551C9D42",
        "Nonce-Str": "b37fb0c0eaad439aa352b894a3da2f38",
        "Sign": "cef6748001244411ccedc059d6785f1f",
        "Device": "{'platform': 'Android', 'device_id': 'deviceId-358022020240216', 'model': 'SM-N9005', 'product_version': '10.6.1.5', 'locale': 'zh_CN', 'product_name': 'MyMoney For Feidee', 'os_version': '4.4.2'}",
        "Minor-Version": "1",
        "User-Agent": "MyMoney/10.6.1.5 (samsung/SM-N9005; Android/4.4.2; feidee)",
        "Cache-Control": "no-cache, max-age=43200",
        "Host": "bizbook.feidee.cn",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip",
        "Authorization": "Bearer ee5977fe-e856-4a75-ada0-35f3dbd078b4"
    }

    PASSWORD = {
        "123456": "7bca5282a041ca8bbd12ec2d98c83f30"
    }

    SYSTEM_ARGS = {
        "test": {
            "business_base_url": "https://bizbook.feidee.cn",
            "login_url": "http://auth.feidee.cn/v2/oauth2/authorize",
        },
        "prod": {
            "login_url": "https://auth.feidee.net/v2/oauth2/authorize",
            "business_base_url": "https://bizbook.feidee.net",
        }
    }

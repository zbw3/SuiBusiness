#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File   : config.py
# @Author : mocobk
# @Email  : mailmzb@qq.com
# @Time   : 2020/3/23 19:38
from settings.HostName import SuiAuth, SuiLogin, SuiUserApi


class Test:
    class Url:
        v2_oauth2_authorize = SuiAuth.TEST + '/v2/oauth2/authorize'
        login_do = SuiLogin.TEST + '/login.do'
        auth = SuiLogin.TEST + '/auth'
        v1_profile = SuiUserApi.TEST + '/v1/profile'

    class Header:
        # web 登录获取 token 时需要
        AUTH_HEADERS = {
            'Client-Key': 'E1B9F17DF5D24B9D88C462C8855BB0F0',  # 不能少
            "Minor-Version": "1",
            'DNT': '1',
            'Origin': 'https://sy.feidee.cn',  # 不能少
            'Accept': 'application/json, text/plain, */*',  # 不能少
        }


class Production:
    class Url:
        v2_oauth2_authorize = SuiAuth.PROD + '/v2/oauth2/authorize'
        login_do = SuiLogin.PROD + '/login.do'
        auth = SuiLogin.PROD + '/auth'
        v1_profile = SuiUserApi.PROD + '/v1/profile'

    class Header:
        # web 登录获取 token 时需要
        AUTH_HEADERS = {**Test.Header.AUTH_HEADERS,
                        'Client-Key': 'C17A51FBE2B241858CCA8AA4F2A25B95',  # 不能少
                        'Origin': 'https://sy.sui.com',  # 不能少
                        }

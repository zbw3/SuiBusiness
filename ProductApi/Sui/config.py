#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File   : config.py
# @Author : mocobk
# @Email  : mailmzb@qq.com
# @Time   : 2020/3/23 19:38
from settings.HostName import SuiAuth


class Test:
    class Url:
        v2_oauth2_authorize = SuiAuth.TEST + '/v2/oauth2/authorize'


class Production:
    class Url:
        v2_oauth2_authorize = SuiAuth.PROD + '/v2/oauth2/authorize'

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File   : __init__.py.py
# @Author : mocobk
# @Email  : mailmzb@qq.com
# @Time   : 2020/3/23 14:56
"""
http://swagger.sui.work/pass/apidoc/share/show.htm?shareKey=8895efc612db2b171b1b78234060c562
"""
from settings.BaseConfig import Env

from settings.HostName import MiniProgramForm

class _Fuid:
    def __init__(self, test, uat, prodution=None):
        self._test = test
        self._uat = uat
        self._prodution = prodution or uat

    @property
    def fuid(self):
        env = Env()
        if env.is_test:
            return self._test
        elif env.is_uat:
            return self._uat
        else:
            return self._prodution

class UserFuid:
    mocobk = _Fuid(test='1026957780256297009', uat='1025186602202501154').fuid
    moco = _Fuid(test='1027047761280765954', uat='').fuid


class Test:
    APP_ID = 'wx1e766c9a00355017'
    HOSTNAME = MiniProgramForm.TEST
    DUFAULT_FUID = '1026957780256297009'

    class Url:
        """
        如果不是默认的域名 HOSTNAME， 可以传一个元组或列表，如:
        v1_login2 = ('https://hostname', '/v1/login2')
        """
        v1_login_test = '/v1/login_test'
        v1_creation_forms = '/v1/creation_forms'
        v1_examples = '/v1/examples'
        v1_image = '/v1/image'
        v1_form = '/v1/form'


class Uat:
    APP_ID = 'wx3f32186d2340171c'
    HOSTNAME = MiniProgramForm.UAT
    DUFAULT_FUID = '1025186602202501154'

    class Url(Test.Url):
        pass


class Production(Uat):
    HOSTNAME = MiniProgramForm.PROD


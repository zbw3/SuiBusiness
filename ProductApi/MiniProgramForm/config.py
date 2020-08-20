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
    user1 = _Fuid(test='1026957780256297009', uat='1025186602202501154').fuid  # mocobk
    user2 = _Fuid(test='1027047761280765954', uat='').fuid  # moco
    zhou_ying1 = _Fuid(test='1027314905029545986', uat='').fuid
    # user1 = _Fuid(test='1053828831317590037', uat='').fuid  # 已废弃的 UAT 用户
    # user2 = _Fuid(test='1059901948376911929', uat='').fuid  # 已废弃的 UAT 用户


class Test:
    HOSTNAME = MiniProgramForm.TEST
    APP_ID = 'wx1e766c9a00355017'
    DUFAULT_FUID = '1026957780256297009'
    # APP_ID = 'wxc67f6d90678e1fe4'  # 已废弃的 UAT
    # DUFAULT_FUID = '1053828831317590037'  # 已废弃的 UAT 用户

    class Url:
        """
        如果不是默认的域名 HOSTNAME， 可以传一个元组或列表，如:
        v1_login2 = ('https://hostname', '/v1/login2')
        """
        v1_login_test = '/v1/login_test'
        v1_creation_forms = '/v1/creation_forms'
        v1_participation_forms = '/v1/participation_forms'
        v1_examples = '/v1/examples'
        v1_image = '/v1/image'
        v1_form = '/v1/form'
        v1_form_form_id = '/v1/form/{formId}'
        v1_form_id_form_data = '/v1/{formId}/form_data'
        v1_form_id_status = '/v1/form/{formId}/status'
        v1_order_list_form_id = '/v1/order/list/{formId}'
        v1_order_form_id_order_id = '/v1/order/{formId}/{orderId}'
        v1_order_query_form_id_fuid = '/v1/order/query/{formId}/{fuid}'
        v1_order_form_id_order_id_remarks = '/v1/order/{formId}/{orderId}/remarks'
        v1_statistic_analysis_form_id = '/v1/statistic/analysis/{formId}'
        v1_statistic_table_form_id = '/v1/statistic/table/{formId}'


class Uat:
    APP_ID = 'wx3f32186d2340171c'
    HOSTNAME = MiniProgramForm.UAT
    DUFAULT_FUID = '1025186602202501154'

    class Url(Test.Url):
        pass


class Production(Uat):
    HOSTNAME = MiniProgramForm.PROD

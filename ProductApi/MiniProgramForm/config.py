#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File   : __init__.py.py
# @Author : mocobk
# @Email  : mailmzb@qq.com
# @Time   : 2020/3/23 14:56
from settings.HostName import MiniProgramForm
"""
http://swagger.sui.work/pass/apidoc/share/show.htm?shareKey=8895efc612db2b171b1b78234060c562
"""

class Test:
    class Url:
        v1_creation_forms = MiniProgramForm.TEST + '/v1/creation_forms'
        v1_examples = MiniProgramForm.TEST + '/v1/examples'


class Uat:
    class Url:
        v1_creation_forms = MiniProgramForm.UAT + '/v1/creation_forms'
        v1_examples = MiniProgramForm.UAT + '/v1/examples'

class Production:
    class Url:
        v1_creation_forms = MiniProgramForm.PROD + '/v1/creation_forms'
        v1_examples = MiniProgramForm.PROD + '/v1/examples'

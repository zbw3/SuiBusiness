#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File   : manage.py
# @Author : mocobk
# @Email  : mailmzb@qq.com
# @Time   : 2019/12/24 15:03
import os
import time

import pytest

from settings.BaseConfig import EnvType


def set_run_env(env: EnvType):
    os.environ['env'] = env.value


def run_test_cases(path, report_dir='./reports'):
    os.makedirs(report_dir, exist_ok=True)
    report_path = os.path.join(report_dir, os.path.basename(path) + time.strftime('-%Y%m%d%H%M%S.html'))
    pytest.main([
        path,
        f'--html={report_path}'
    ])


if __name__ == '__main__':
    # 设置当前运行环境
    set_run_env(EnvType.Test)
    run_test_cases('./mp_form')

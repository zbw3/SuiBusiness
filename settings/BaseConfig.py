#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File   : api.py
# @Author : mocobk
# @Email  : mailmzb@qq.com
# @Time   : 2019/12/23 14:21
import os

from ilogger import logger


class AuthSchema:
    def __init__(self, token=None, key=None, iv=None, **kwargs):
        self.iv = iv
        self.key = key
        self.token = token
        self.args = kwargs


class Logger:
    NOTSET = logger.NOTSET
    DEBUG = logger.DEBUG
    INFO = logger.INFO
    WARNING = logger.WARNING
    WARN = logger.WARN
    ERROR = logger.ERROR
    CRITICAL = logger.CRITICAL
    logger = logger


class Project:
    # 项目根目录
    path = os.path.abspath(os.path.dirname(__file__) + '/..')

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File   : manage.py
# @Author : mocobk
# @Email  : mailmzb@qq.com
# @Time   : 2019/12/24 15:03

import os
import unittest

from BeautifulReport import BeautifulReport
from ilogger import logger


# 打印当前查找到的所有用例
def print_discover_cases(suits):
    import re
    for each_suit in suits:
        cases = re.findall('<test.+?>', str(each_suit))
        for test_case in cases:
            logger.debug(test_case)
    logger.info('共加载%s个用例' % suits.countTestCases())


def discover(start_dir='./', pattern='test*.py'):
    start_dir = os.path.join('./', start_dir)
    t = unittest.defaultTestLoader.discover(start_dir, pattern)
    return unittest.defaultTestLoader.discover(start_dir, pattern)


def store_web_suites():
    suites = unittest.TestSuite()
    suites.addTests(discover('store_web'))
    return suites


if __name__ == '__main__':
    # 设置当前运行环境 test or productionff
    os.environ['env'] = 'test'
    test_suites = store_web_suites()
    print_discover_cases(test_suites)
    result = BeautifulReport(test_suites)
    result.report(filename='驭信接口测试报告', description='驭信接口', report_dir='report')

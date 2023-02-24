#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File   : run_all.py
# @Email  : xuexia_xu@feidee.com
# @Time   :2023/2/14 14:11:00
import pytest
import os
"""生成allure报告的运行方式"""
#方式一：默认运行的是当前目录及子目录的所有文件夹的测试用例
# pytest.main(['-s', '-q','--clean-alluredir','--alluredir=../reports/result'])
# os.system("allure serve ../reports/result -o ../report/html")

#方式二：运行某一个.py文件下的用例
pytest.main(['-s', '-q','test_operation_form.py','--clean-alluredir','--alluredir=../reports/result'])
os.system("allure serve ../reports/result -o ../report/html")

#方式三：运行指定的 test_form.py 下的某一个用例 test_post_form
# pytest.main(['-s', '-q','test_form.py::test_post_form','--clean-alluredir','--alluredir=../reports/result'])
# os.system("allure serve ../reports/result -o ../report/html")

"""不生成allure报告运行"""
# 方式一：默认运行的是当前目录及子目录的所有文件夹的测试用例
# pytest.main()

# 方式二：运行某一个.py文件下的用例
# pytest.main(["test_creation_forms.py"])

# 方式三：运行指定的 test_form.py 下的某一个用例 test_post_form
# pytest.main(["test_form.py::test_post_form"])

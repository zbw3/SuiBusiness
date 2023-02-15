#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File   : run_all.py
# @Email  : xuexia_xu@feidee.com
# @Time   :2023/2/14 14:11:00
import pytest

# 默认运行的是当前目录及子目录的所有文件夹的测试用例
# pytest.main()
#运行某一个.py文件下的用例
pytest.main(["test_creation_forms.py"])
# 运行指定的 test_form.py 下的某一个用例 test_post_form
# pytest.main(["test_form.py::test_post_form"])

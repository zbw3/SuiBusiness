# @File   : test_get_oper_original_data_entire.py
# @Time   : 2019/12/24 10:51
"""
author: zaibin_mo
description: 运营商原始数据全部字段获取接口
api_path: 
api_doc: 
"""
import os
import unittest

from parameterized import parameterized, param
from testfilter import runIf, Filter

from ProductApi.NetworkOperator.api import Operator

# 设置执行环境 test uat prod/production 不区分大小写
Filter.env = os.getenv("env", "test")
Filter.level = os.getenv("level", "P4")  # smoke/p1 p2 p3 p4 不区分大小写


class TestData:
    normal = {'name': '黄伟杰', 'idCardNo': '440182199410253311', 'phone': '17362952439'}

    @staticmethod
    def phone_param_data():
        base_params = {'name': '黄伟杰', 'idCardNo': '440182199410253311'}
        return [
            # phone 参数不传
            param(base_params, expected_code='500'),
            # phone 参数不合法
            param({**base_params, 'phone': None}, expected_code='500'),
            param({**base_params, 'phone': ''}, expected_code='500'),
            param({**base_params, 'phone': 18566772480}, expected_code='200'),
            param({**base_params, 'phone': '1856677'}, expected_code='500'),
            param({**base_params, 'phone': '18566772480000'}, expected_code='500'),
            param({**base_params, 'phone': 'abcdefg'}, expected_code='500'),
        ]


class GetOperOriginalDataEntire(unittest.TestCase, metaclass=Filter.Meta):
    @classmethod
    def setUpClass(cls) -> None:
        cls.oper = Operator(env=Filter.env)
        cls.oper.logger.setLevel(cls.oper.DEBUG)

    @runIf.level_in.SMOKE
    def test_smoke(self):
        """基本冒烟测试"""
        params = TestData.normal
        response = self.oper.get_oper_original_data_entire(params)
        self.assertEqual(200, response.status_code)
        self.assertEqual('200', response.data.get('code'))
        self.assertIsNotNone(response.data.get('data'), response)

    @runIf.level_in.P1
    def test_params_null(self):
        """logon 参数为空"""
        params = {}
        response = self.oper.get_oper_original_data_entire(params)
        self.assertEqual('500', response.data.get('code'))
        self.assertIsNone(response.data.get('data'), response)

    @parameterized.expand(TestData.phone_param_data())
    @runIf.level_in.P2  # 需要在参数化之前
    def test_param_phone(self, params, expected_code):
        """phone参数验证"""
        response = self.oper.get_oper_original_data_entire(params)
        self.assertEqual(expected_code, response.data.get('code'), response.data)


if __name__ == '__main__':
    unittest.main()

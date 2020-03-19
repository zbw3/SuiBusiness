#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File   : network_operator.py
# @Author : mocobk
# @Email  : mailmzb@qq.com
# @Time   : 2019/1/22 9:53
from ProductApi.base import OperatorApiBase
from ProductApi.NetworkOperator import config


class Operator(OperatorApiBase):
    def __init__(self, env, auth: dict = None, print_results=True):
        """
        """
        self.config = config
        self.url = self.config.get(env).Url
        self.auth = self.dict_to_auth(auth) if auth else self.config.get(env).Auth
        self.print_results = print_results
        super().__init__(print_results)

    def get_oper_original_data_entire(self, logon_params, **kwargs):
        """
        Name: 运营商原始数据全部字段获取接口(在用)
        DocUrl: https://confluence.sui.work/pages/viewpage.action?pageId=10973264

        params::

            name            String  Y   用户姓名
            idCardNo        String  Y   用户姓名身份证号
            phone           String  Y   用户手机号
        """
        api_name = '运营商原始数据全部字段获取接口'
        url = self.url.oper_original_data_entire
        return self.api_common(
            url, api_name,
            logon_params=logon_params,
            auth=self.auth,
            encrypt=self.crypto.AES_Base64_encrypt,
            decrypt=self.crypto.AES_Base64_decrypt,
            **kwargs
        )

    def get_oper_var(self, logon_params, **kwargs):
        """
        Name: 运营商变量数据获取接口（旧接口）
        DocUrl: http://172.22.23.233:8888/openapi-doc/network-operator/network-operator.html#%E6%8E%A5%E5%8F%A3_3

        params::

            name            String  Y   用户姓名
            idCardNo        String  Y   用户姓名身份证号
            phone           String  Y   用户手机号
            phoneOne        String  N   联系人1
            phoneTwo        String  N   联系人2
            phoneThree      String  N   联系人3
        """
        api_name = '运营商变量计算字段获取接口'
        url = self.url.get_oper_var
        return self.api_common(
            url, api_name,
            logon_params=logon_params,
            auth=self.auth,
            encrypt=self.crypto.AES_Base64_encrypt,
            decrypt=None,
            **kwargs
        )


if __name__ == '__main__':
    oper = Operator(env='test')
    oper.logger.setLevel(oper.DEBUG)
    # oper.get_oper_original_data_entire({"phone": "18566772480"})
    oper.get_oper_var({"phone": "18566772480"})

# !/user/bin/env python
# _*_ coding: utf-8 _*_
# @File  : v1_store_vip_add_member.py
# @Author: zy
# @Date  : 2020/4/8
import unittest
import ddt
from ProductApi.StoreWeb import api


def for_resp(params: dict):
    api1 = api.StoreWebApi(username="119@kd.ssj", password="123456", trading_entity="3604098", Minor_Version="2",
                           print_results=True)
    resp = api1.v1_store_vip_add_member(params=params)
    resp.encoding = 'etf-8'
    return resp


# vcid需要使用v1_store_sms返回的vcid，需要联合接口使用，也就是先使用sms获取验证码和vcid
param1 = {
    'nick_name': '111',
    'phone': '18702612890',
    'sms_code': '',
    'vcid': ''
}


@ddt.ddt
class Test(unittest.TestCase):
    @ddt.data(param1)
    def test_1(self, params):
        resp = for_resp(params)
        self.assertEqual(resp.status_code, 200)


if __name__ == '__main__':
    unittest.main()

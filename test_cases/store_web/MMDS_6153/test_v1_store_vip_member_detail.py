# !/user/bin/env python
# _*_ coding: utf-8 _*_
# @File  : test_v1_store_vip_member_detail.py
# @Author: zy
# @Date  : 2020/4/8
import json
import unittest
import ddt
from ProductApi.StoreWeb import api


def for_resp(params: dict):
    api1 = api.StoreWebApi(username="119@kd.ssj", password="123456", print_results=True)
    resp = api1.v1_store_vip_vip_member_detail(params=params)
    resp.encoding = 'etf-8'
    return resp


# 查询会员，根据条件，其中source表示第三方账号，1表示支付宝，2表示微信
# vaild表示会员状态，0表示已冻结，1表示正常
param1 = {
    "multi_conditions": json.dumps({
        "tag_id": "",
        "tag_id_flag": True,
        "nick_name": "",
        "vip_number": "1111",
        "phone": "",
        "level_id": "",
        "source": "",
        "valid": 0
    }),
    "page_number": 1,
    "page_size": 30
}
# 会员名和会员卡号都支持模糊查询（组合条件查询）
param2 = {
    "multi_conditions": json.dumps({
        "tag_id": "",
        "tag_id_flag": True,
        "nick_name": "被",
        "vip_number": "9",
        "phone": "",
        "level_id": "",
        "source": "",
        "valid": 0
    }),
    "page_number": 1,
    "page_size": 30
}


@ddt.ddt
class Test(unittest.TestCase):
    @ddt.data(param1)
    def test_1(self, params):
        resp = for_resp(params)
        self.assertEqual(resp.status_code, 200)

    @ddt.data(param2)
    def test_2(self, params):
        resp = for_resp(params)
        self.assertEqual(resp.status_code, 200)


if __name__ == '__main__':
    Test(unittest.TestCase)

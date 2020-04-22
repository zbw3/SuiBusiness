# !/user/bin/env python
# _*_ coding: utf-8 _*_
# @File  : test_v2_report_month.py
# @Author: zy
# @Date  : 2020/3/26
import decimal
import json
import ddt

from ProductApi.StoreWeb import api
import unittest
from test_cases.store_web.MMDS_6136 import timestamp
from test_cases.store_web.MMDS_6136.mysql_month import do_mysql


def for_resp(params: dict):
    api1 = api.StoreWebApi(username="119@kd.ssj", password="123456", trading_entity="3604098", Minor_Version="2",
                           print_results=True)
    resp = api1.v2_report_month_get(params=params)
    resp.encoding = 'etf-8'
    return resp


'''
" 5 "表示进货单，后面type的值表示——purchase
" 61 "表示销售单，后面type的值表示——sale
" 62 "表示会员充值，后面type的值表示——recharge
该接口查询字符串传参一共4个：
            begin_date、end_date、order_types、channel_type（非必填）
'''
# 正向用例1，传单个order_types——》5
params_1 = {
    'begin_date': timestamp.timestamp('2020-3-1 00:00:00'),
    'end_date': timestamp.timestamp('2020-3-26 00:00:00'),
    'order_types': '5'
}
# 正向用例2，传多个order_types——》5,
params_2 = {
    'begin_date': timestamp.timestamp('2020-1-1 00:00:00'),
    'end_date': timestamp.timestamp('2020-3-26 00:00:00'),
    'order_types': '5',
    'channel_type': '1'
}
# 正向用例3，传多个order_types——》5，62，以及channel_type传参为1
params_3 = {
    'begin_date': timestamp.timestamp('2020-1-1 00:00:00'),
    'end_date': timestamp.timestamp('2020-3-26 00:00:00'),
    'order_types': '5,62',
    'channel_type': '1'
}
# 正向用例4，传单个order_types——》61，以及channel_type传参为1
params_4 = {
    'begin_date': timestamp.timestamp('2020-3-10 00:00:00'),
    'end_date': timestamp.timestamp('2020-4-7 00:00:00'),
    'order_types': '61,63',
    'channel_type': '1'
}
# 正向用例5，传多个order_types——》61，以及channel_type传参为2
params_5 = {
    'begin_date': timestamp.timestamp('2020-1-1 00:00:00'),
    'end_date': timestamp.timestamp('2020-3-26 00:00:00'),
    'order_types': '61,63',
    'channel_type': '2'
}


@ddt.ddt
class Test(unittest.TestCase):

    @ddt.data(params_1)
    def test_1(self, params):
        resp = for_resp(params)
        self.assertEqual(resp.status_code, 200)
        do = do_mysql(params)
        result = do.channel_have
        do.conn_close()
        if result[0][0] is None:
            self.assertEqual(
                str(decimal.Decimal("0.00").quantize(decimal.Decimal("0.00"))), json.loads(resp.text)['trade_amount'])
        else:
            self.assertEqual(str(result[0][0]), json.loads(resp.text)['trade_amount'])

    @ddt.data(params_2)
    def test_2(self, params):
        resp = for_resp(params)
        self.assertEqual(resp.status_code, 200)
        do = do_mysql(params)
        result = do.channel_have
        do.conn_close()
        if result[0][0] is None:
            self.assertEqual(
                str(decimal.Decimal("0.00").quantize(decimal.Decimal("0.00"))), json.loads(resp.text)['trade_amount'])
        else:
            self.assertEqual(str(result[0][0]), json.loads(resp.text)['trade_amount'])

    @ddt.data(params_3)
    def test_3(self, params):
        resp = for_resp(params)
        self.assertEqual(resp.status_code, 200)
        do = do_mysql(params)
        result = do.channel_have
        do.conn_close()
        if result[0][0] is None:
            self.assertEqual(
                str(decimal.Decimal("0.00").quantize(decimal.Decimal("0.00"))), json.loads(resp.text)['trade_amount'])
        else:
            self.assertEqual(str(result[0][0]), json.loads(resp.text)['trade_amount'])

    @ddt.data(params_4)
    def test_4(self, params):
        resp = for_resp(params)
        self.assertEqual(resp.status_code, 200)
        do = do_mysql(params)
        result = do.channel_have
        do.conn_close()
        if result[0][0] is None:
            self.assertEqual(
                str(decimal.Decimal("0.00").quantize(decimal.Decimal("0.00"))), json.loads(resp.text)['trade_amount'])
        else:
            self.assertEqual(str(result[0][0]), json.loads(resp.text)['trade_amount'])

    @ddt.data(params_5)
    def test_5(self, params):
        resp = for_resp(params)
        self.assertEqual(resp.status_code, 200)
        do = do_mysql(params)
        result = do.channel_have
        do.conn_close()
        if result[0][0] is None:
            self.assertEqual(
                str(decimal.Decimal("0.00").quantize(decimal.Decimal("0.00"))), json.loads(resp.text)['trade_amount'])
        else:
            self.assertEqual(str(result[0][0]), json.loads(resp.text)['trade_amount'])


if __name__ == '__main__':
    Test(unittest.TestCase)
# 账本是3604098

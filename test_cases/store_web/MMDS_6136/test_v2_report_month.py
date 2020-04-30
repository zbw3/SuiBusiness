# !/user/bin/env python
# _*_ coding: utf-8 _*_
# @File  : test_v2_report_month.py
# @Author: zy
# @Date  : 2020/3/26
import warnings
from ProductApi.StoreWeb import api
from test_cases.store_web.MMDS_6136 import timestamp
from test_cases.store_web.MMDS_6136.mysql_month import V2ReportMonthMysql
from test_cases.store_web.data import account_data


def get_resp(params: dict):
    username = account_data.data()["username"]
    password = account_data.data()["password"]
    api1 = api.StoreWebApi(username=username, password=password, trading_entity="3604098", Minor_Version="2",
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


# 忽略ResourceWarning的警告
def setUpClass():
    warnings.simplefilter('ignore', ResourceWarning)


def test_1():
    params = params_1
    resp = get_resp(params)
    assert resp.status_code == 200
    mysql_object = V2ReportMonthMysql(params)
    result = mysql_object.channel_have
    pre = result.get("trade_amount").to_eng_string() if result.get("trade_amount") else '0.00'
    assert pre == resp.json()['trade_amount']
    mysql_object.conn_close()
    import decimal
    decimal.Decimal('0.00').to_eng_string()


def test_2():
    params = params_2
    resp = get_resp(params)
    assert resp.status_code == 200
    mysql_object = V2ReportMonthMysql(params)
    result = mysql_object.channel_have
    pre = result.get("trade_amount").to_eng_string() if result.get("trade_amount") else '0.00'
    assert pre == resp.json()['trade_amount']
    mysql_object.conn_close()


def test_3():
    params = params_3
    resp = get_resp(params)
    assert resp.status_code == 200
    mysql_object = V2ReportMonthMysql(params)
    result = mysql_object.channel_have
    pre = result.get("trade_amount").to_eng_string() if result.get("trade_amount") else '0.00'
    assert pre == resp.json()['trade_amount']
    mysql_object.conn_close()


def test_4():
    params = params_4
    resp = get_resp(params)
    assert resp.status_code == 200
    mysql_object = V2ReportMonthMysql(params)
    result = mysql_object.channel_have
    pre = result.get("trade_amount").to_eng_string() if result.get("trade_amount") else '0.00'
    assert pre == resp.json()['trade_amount']
    mysql_object.conn_close()


def test_5():
    params = params_5
    resp = get_resp(params)
    assert resp.status_code == 200
    mysql_object = V2ReportMonthMysql(params)
    result = mysql_object.channel_have
    pre = result.get("trade_amount").to_eng_string() if result.get("trade_amount") else '0.00'
    assert pre == resp.json()['trade_amount']
    mysql_object.conn_close()


if __name__ == '__main__':
    test_1()


'''
if result[0][0] is None:
    self.assertEqual(
        str(decimal.Decimal("0.00").quantize(decimal.Decimal("0.00"))), json.loads(resp.text)['trade_amount'])
else:
    self.assertEqual(str(result[0][0]), json.loads(resp.text)['trade_amount'])
'''


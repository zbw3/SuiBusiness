# !/user/bin/env python
# _*_ coding: utf-8 _*_
# @File  : test_v2_report_range.py
# @Author: zy
# @Date  : 2020/3/26
import json
import ddt
from ProductApi.StoreWeb import api
import unittest
from test_cases.store_web.MMDS_6136 import timestamp
import jmespath


def for_resp(params: dict):
    api1 = api.StoreWebApi(username="119@kd.ssj", password="123456", trading_entity="3604098", Minor_Version="2",
                           print_results=True)
    resp = api1.v2_report_range_get(params=params)
    resp.encoding = 'etf-8'
    return resp


# 正向用例1，传参单个channel_type，值为1，即门店，以及开始和结束时间
params_1 = {
    "multi_conditions": json.dumps(
        {
            "channel_type": "",
            'begin_date': timestamp.timestamp('2020-4-9 00:00:00'),
            "end_date": timestamp.timestamp('2020-4-10 00:00:00'),
        }
    ),

}
# 正向用例2，传参单个channel_type，值为2
params_2 = {
    "multi_conditions": json.dumps(
        {
            "channel_type": "2",
        }
    )
}
# 反向用例3，组合传参channel_type和handler，其中handler是传没有的值
params_3 = {
    "multi_conditions": json.dumps(
        {
            "handler": "aa",
            "channel_type": "1",
        }
    )
}
# 正向用例4，多条件选择全部传参channel_type和开始时间、结束时间、经手人，这里的begin_date和end_date对应的是biz_order表中的order_time
params_4 = {
    "multi_conditions": json.dumps(
        {
            "channel_type": '1',
            # 'begin_date': timestamp.timestamp('2020-3-25 00:00:00'),
            "end_date": timestamp.timestamp('2020-3-31 00:00:00'),
            "handler": "119@feidee"
        }
    )
}


@ddt.ddt
class Test(unittest.TestCase):
    @ddt.data(params_1)
    def test_1(self, params):
        resp = for_resp(params)
        self.assertEqual(resp.status_code, 200)

    @ddt.data(params_2)
    def test_2(self, params):
        resp = for_resp(params)
        self.assertEqual(resp.status_code, 200)

    @ddt.data(params_3)
    def test_3(self, params):
        resp = for_resp(params)
        self.assertEqual(resp.status_code, 200)

    @ddt.data(params_4)
    def test_4(self, params):
        resp = for_resp(params)
        self.assertEqual(resp.status_code, 200)
        dict_1 = json.loads(resp.text)
        result = jmespath.search('sale_amount', dict_1)
        print(result)


if __name__ == '__main__':
    unittest.main()

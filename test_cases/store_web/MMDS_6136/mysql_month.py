# !/user/bin/env python
# _*_ coding: utf-8 _*_
# @File  : mysql_month.py
# @Author: zy
# @Date  : 2020/4/3
import pymysql
from test_cases.store_web.MMDS_6136 import timestamp


class V2ReportMonthMysql:
    def __init__(self, params):
        self.params = params
        self.connect = pymysql.connect(
            host='ssj0.testfeideedba.com',
            db='test_money_3_business',
            port=3232,
            user='SSJ_feidee',
             passwd='Hf#df_6c#b7,d8d#2ee6_fe85H3d',
             charset='utf8',
         )
        self.cursor = self.connect.cursor(pymysql.cursors.DictCursor)
        # self.cursor = test_money_3_business()

    @property
    def channel_have(self):
        params = self.params
        if 'channel_type' in params:
            if params['channel_type'] == '1':
                sql = "SELECT SUM(real_amount) as trade_amount FROM biz_order " \
                      "WHERE trading_entity = '3604098' and type in (%s) and refund_status!=2 " \
                      "and order_source in (0,1,2) and status = 50 and order_time BETWEEN \'%s\' and \'%s\'"
                self.cursor.execute(sql % (
                    params['order_types'], timestamp.time1(params['begin_date']), timestamp.time1(params['end_date'])))
                return self.cursor.fetchone()
            elif params['channel_type'] == '2':
                sql = "SELECT SUM(real_amount) as trade_amount  FROM biz_order " \
                      "WHERE trading_entity = '3604098' and type in (%s) and refund_status!=2 " \
                      "and order_source in (3) and status = 50 and order_time BETWEEN \'%s\' and \'%s\'"
                self.cursor.execute(sql % (
                    params['order_types'], timestamp.time1(params['begin_date']), timestamp.time1(params['end_date'])))
                return self.cursor.fetchone()
            else:
                return 'wrong'
        else:
            sql = "SELECT SUM(real_amount) as trade_amount  FROM biz_order " \
                  "WHERE trading_entity = '3604098' and type in (%s) and refund_status!=2 " \
                  "and status = 50 and order_time BETWEEN \'%s\' and \'%s\'"
            self.cursor.execute(sql % (
                params['order_types'], timestamp.time1(params['begin_date']), timestamp.time1(params['end_date'])))
            return self.cursor.fetchone()

    def conn_close(self):
        self.cursor.close()
        self.connect.close()


'''
上面的sql语句是求总金额，即v2_report_month接口的返回的trade_amount的数
'''

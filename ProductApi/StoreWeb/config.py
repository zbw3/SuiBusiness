#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File   : __init__.py.py
# @Author : mocobk
# @Email  : mailmzb@qq.com
# @Time   : 2020/3/23 14:56
from settings.HostName import BizBook


class Test:
    class Url:
        v1_store_products_categorys = BizBook.TEST + '/v1/store/products/categorys'
        v4_trade_orders_pages = 'https://bizbook.feidee.cn/v4/trade/orders_page'
        v2_report_range_get = 'https://bizbook.feidee.cn/v2/report/range'
        v1_report_month_get = 'https://bizbook.feidee.cn/v2/report/month'
        v1_store_vip_sms = 'https://bizbook.feidee.cn/v1/store/vip/sms'
        v1_store_vip_add_member = 'https://bizbook.feidee.cn/v1/store/vip/add/member'
        v1_store_vip_orders_page = 'https://bizbook.feidee.cn/v1/store/vip/orders_page'
        v1_store_vip_check_phone = 'https://bizbook.feidee.cn/v1/store/vip/check_phone'
        v1_store_vip_member_detail = 'https://bizbook.feidee.cn/v1/store/vip/members'
        v1_acquiring_account_cancel = 'https://bizbook.feidee.cn/v1/acquiring/open_acount/cancel'
        v1_acquiring_open_account_status = 'https://bizbook.feidee.cn/v1/acquiring/open_account/status'
        v1_acquiring_open_account_info = 'https://bizbook.feidee.cn/v1/acquiring/open_account/info'
        v3_acquiring_open_account_status = 'https://bizbook.feidee.cn/v3/acquiring/open_account/status'


class Production:
    class Url:
        v1_store_products_categorys = BizBook.PROD + '/v1/store/products/categorys'
        v4_trade_orders_pages = 'https://bizbook.feidee.net/v4/trade/orders_page'
        v2_report_range_get = 'https://bizbook.feidee.net/v2/report/range'
        v1_report_month_get = 'https://bizbook.feidee.net/v2/report/month'



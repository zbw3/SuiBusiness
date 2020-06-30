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
        v4_trade_orders_pages = BizBook.TEST + '/v4/trade/orders_page'
        v2_report_range_get = BizBook.TEST + '/v2/report/range'
        v1_report_month_get = BizBook.TEST + '/v2/report/month'
        v1_store_vip_sms = BizBook.TEST + '/v1/store/vip/sms'
        v1_store_vip_add_member = BizBook.TEST + '/v1/store/vip/add/member'
        v1_store_vip_orders_page = BizBook.TEST + '/v1/store/vip/orders_page'
        v1_store_vip_check_phone = BizBook.TEST + '/v1/store/vip/check_phone'
        v1_store_vip_member_detail = BizBook.TEST + '/v1/store/vip/members'
        v2_store_products_spec_name = BizBook.TEST + '/v2/store/products/spec_name'
        v2_store_products_specs = BizBook.TEST + '/v2/store/products/specs'
        v2_store_products_spec_value = BizBook.TEST +'/v2/store/products/spec_value'
        v2_store_products_goods = BizBook.TEST + '/v2/store/products/goods'
        v2_store_products_batch = BizBook.TEST + '/v2/store/products/batch'
        v2_store_products_goods_item = BizBook.TEST + '/v2/store/products/goods_item'
        v1_store_storehouse = BizBook.TEST + '/v1/store/storehouse'
        v1_store_storehouse_statistics = BizBook.TEST + '/v1/store/storehouse/statistics'
        v1_store_suppliers = BizBook.TEST + '/v1/store/suppliers'
        v1_store_vip_levels = BizBook.TEST + '/v1/store/vip/levels'


class Production:
    class Url:
        v1_store_products_categorys = BizBook.PROD + '/v1/store/products/categorys'
        v4_trade_orders_pages = BizBook.PROD + '/v4/trade/orders_page'
        v2_report_range_get = BizBook.PROD + '/v2/report/range'
        v1_report_month_get = BizBook.PROD + '/v2/report/month'

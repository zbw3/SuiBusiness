#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File   : __init__.py.py
# @Author : mocobk
# @Email  : mailmzb@qq.com
# @Time   : 2020/3/23 14:56
from settings.HostName import BizBook


class Test:
    HOSTNAME = BizBook.TEST

    class Url:
        v1_store_products_categorys = '/v1/store/products/categorys'
        v4_trade_orders_pages = '/v4/trade/orders_page'
        v2_report_range_get = '/v2/report/range'
        v1_report_month_get = '/v2/report/month'
        v1_store_vip_sms = '/v1/store/vip/sms'
        v1_store_vip_add_member = '/v1/store/vip/add/member'
        v1_store_vip_orders_page = '/v1/store/vip/orders_page'
        v1_store_vip_check_phone = '/v1/store/vip/check_phone'
        v1_store_vip_member_detail = '/v1/store/vip/members'
        v2_store_products_spec_name = '/v2/store/products/spec_name'
        v2_store_products_specs = '/v2/store/products/specs'
        v2_store_products_spec_value = '/v2/store/products/spec_value'
        v2_store_products_goods = '/v2/store/products/goods'
        v2_store_products_batch = '/v2/store/products/batch'
        v2_store_products_goods_item = '/v2/store/products/goods_item'
        v1_store_storehouse = '/v1/store/storehouse'
        v1_store_storehouse_statistics = '/v1/store/storehouse/statistics'
        v1_store_suppliers = '/v1/store/suppliers'
        v1_store_vip_levels = '/v1/store/vip/levels'
        v1_logistic_orders = '/v1/logistic_orders'
        v1_trading_entity_logistics_balance = '/v1/trading_entity/logistics/balance'
        v1_trading_entity_logistics_thd_deliveries = '/v1/trading_entity/logistics/thd_deliveries'
        v1_trading_entity_logistics_thd_ss_delivery = '/v1/trading_entity/logistics/thd_ss_delivery'
        v1_logistic_orders_re = '/v1/logistic_orders'
        v1_logistic_orders_cancel = '/v1/logistic_orders'
        v1_logistic_orders_back = '/v1/logistic_orders'
        v1_trading_entity_logistics_thd_ss_delivery_remove = '/v1/trading_entity/logistics/thd_ss_delivery'
        v1_trading_entity_logistics_bound_supported = '/v1/trading_entity/logistics/bound_supported'
        v1_trading_entity_logistics_type = '/v1/trading_entity/logistics'
        online_logistic_book_store = 'online/logistic/book_store'
        v1_trading_entity_logistics = '/v1/trading_entity/logistics'
        v1_store_coupon_batches = '/v1/store/coupon_batches'
        v1_store_coupon_batches_coupons = '/v1/store/coupon_batches/coupons'
        v1_store_coupon_batches_info = '/v1/store/coupon_batches/info'
        """会员标签"""
        v1_store_vip_tags = '/v1/store/vip/tags'
        v1_store_vip_tag_only = '/v1/store/vip/tag_only'
        """会员充值"""
        v1_store_vip_recharges = '/v1/store/vip/recharges'
        v1_store_vip_recharges_save = '/v1/store/vip/recharges/save'

        "网店商品分组"
        """
        新增接口：
1、GET /v1/store/products/tags 查询店铺商品分组
2、POST /v1/store/products/tags 添加商品分组
3、PUT /v1/store/products/tags 修改商品分组
4、DELETE /v1/store/products/tags/batch 批量删除商品分组
5、POST /v1/store/products/tags/add_product_channels 分组添加渠道商品
6、DELETE /v1/store/products/tags/delete_product_channels 分组移除渠道商品
7、PUT /v1/store/products/tags/reweight_product_channels 修改分组里渠道商品的权重
        """
        v1_store_products_tags = '/v1/store/products/tags'
        v1_store_products_tags_batch = "/v1/store/products/tags/batch"
        v1_store_products_tags_add_product_channels = '/v1/store/products/tags/add_product_channels'
        v1_store_products_tags_delete_product_channels = '/v1/store/products/tags/delete_product_channels'
        v1_store_products_tags_reweight_product_channels = '/v1/store/products/tags/reweight_product_channels'



class Production:
    HOSTNAME = BizBook.PROD

    class Url(Test.Url):
        pass

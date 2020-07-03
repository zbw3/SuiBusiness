#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File   : api.py
# @Author : mocobk
# @Email  : mailmzb@qq.com
# @Time   : 2019/1/22 9:53
from ProductApi.StoreWeb import config
from ProductApi.Sui.api import Sui
from ProductApi.base import ApiBase
import time

class StoreWebApi(ApiBase):

    def __init__(self, username, password, version='1', trading_entity="3604098", print_results=False):
        """
        :param username: 用户名
        :param password: 密码
        :param trading_entity: 账本 ID
        """
        super().__init__(print_results)
        self.config: config.Test = getattr(config, self.env.name)
        self.headers = Sui(username, password).authorized_hearders()
        self.headers["Minor-Version"] = version
        self.headers["Trading-Entity"] = trading_entity

    def v1_store_products_categorys_get(self):
        """
        Name: 查询商品分类
        DocUrl: None
        """
        url = self.config.Url.v1_store_products_categorys
        response = self.request(url=url, method='GET', headers=self.headers)
        return response

    def v1_store_products_categorys_post(self, params: dict):
        """
        Name: 添加商品分类
        DocUrl: None

        data::

            name            String  Y   分类名称

        """
        url = self.config.Url.v1_store_products_categorys
        response = self.request(url=url, method='POST', headers=self.headers, json=params)
        return response

    def v4_trade_orders_pages_get(self, params: dict):
        """
        Name: 查询订单列表
        DocUrl: None

        data::

            type             String  Y   分类名称
            page_number      String  Y   分类名称
            page_size        String  Y   分类名称

        """
        url = self.config.Url.v4_trade_orders_pages
        response = self.request(url=url, method='GET', headers=self.headers, params=params)
        return response

    def v2_report_range_get(self, params: dict):
        """
        Name: 报表
        DocUrl: None

        data::



        """
        url = self.config.Url.v2_report_range_get

        response = self.request(url=url, method='GET', headers=self.headers, params=params)
        return response

    def v2_report_month_get(self, params: dict):
        """
            Name: 月报
            DocUrl: None

            data::

            """
        url = self.config.Url.v1_report_month_get
        response = self.request(url=url, method='GET', headers=self.headers, params=params)
        return response

    def v1_store_vip_sms(self, params: dict):
        """
                  Name: 会员短信验证
                  DocUrl: None

                  data::

           """
        url = self.config.Url.v1_store_vip_sms
        response = self.request(url=url, method='POST', headers=self.headers, json=params)
        return response

    def v1_store_vip_add_member(self, params: dict):
        """
                  Name: 添加会员
                  DocUrl: None

                  data::

           """
        url = self.config.Url.v1_store_vip_add_member
        response = self.request(url=url, method='POST', headers=self.headers, json=params)
        return response

    def v1_store_vip_orders_page(self, params: dict):
        """
                  Name: 订单页面
                  DocUrl: None

                  data::

           """
        url = self.config.Url.v1_store_vip_orders_page
        response = self.request(url=url, method='GET', headers=self.headers, params=params)
        return response

    def v1_store_vip_check_phone(self, params: dict):
        """
                  Name: 订单页面
                  DocUrl: None

                  data::

           """
        url = self.config.Url.v1_store_vip_check_phone
        response = self.request(url=url, method='GET', headers=self.headers, params=params)
        return response

    def v1_store_vip_vip_member_detail(self, params: dict):
        """
                  Name: 订单页面
                  DocUrl: None

                  data::

           """
        url = self.config.Url.v1_store_vip_member_detail
        response = self.request(url=url, method='GET', headers=self.headers, params=params)
        return response


    def v2_store_products_spec_name_post(self, params: dict):
        """"添加商品规格名"""
        url = self.config.Url.v2_store_products_spec_name
        response = self.request(url=url, method='POST', headers=self.headers, json=params)
        return response


    def v2_store_products_spec_get(self, **params: dict):
        """"获取店铺规格"""
        url = self.config.Url.v2_store_products_specs
        response = self.request(url=url, method='GET', headers=self.headers, json=params)
        return response

    def v2_store_products_spec_value_post(self, params: dict):
        """添加商品规格值"""
        url = self.config.Url.v2_store_products_spec_value
        response = self.request(url=url, method='POST', headers=self.headers, json=params)
        return response

    def v2_store_products_goods_get(self, params: dict):
        """"查询商品"""
        url = self.config.Url.v2_store_products_goods
        response = self.request(url=url, method='GET', headers=self.headers, params=params)
        return response

    def v2_store_products_batch_delete(self, params: dict):
        """删除商品"""
        url = self.config.Url.v2_store_products_batch
        response = self.request(url=url, method='DELETE', headers=self.headers, json=params)
        return response

    def v2_store_products_goods_item_get(self, params: dict):
        """查询单品"""
        url = self.config.Url.v2_store_products_goods_item
        response = self.request(url=url, method='GET', headers=self.headers, params=params)
        return response

    def v1_store_storehouse_post(self, params: dict):
        """管店-仓库进货"""
        url = self.config.Url.v1_store_storehouse
        response = self.request(url=url, method='POST', headers=self.headers, json=params)
        return response

    def v1_store_storehouse_statistics_get(self, params: dict):
        """管店-仓库统计"""
        url = self.config.Url.v1_store_storehouse_statistics
        response = self.request(url=url, method='GET', headers=self.headers, params=params)
        return response


    def v1_store_suppliers_get(self):
        """供应商-查询供应商列表"""
        url = self.config.Url.v1_store_suppliers
        response = self.request(url=url, method='GET', headers=self.headers)
        return response

    def v1_store_suppliers_post(self, params: dict):
        """供应商-新增供应商"""
        url = self.config.Url.v1_store_suppliers
        response = self.request(url=url, method='POST', headers=self.headers, json=params)
        return response

    def v1_store_suppliers_put(self, params: dict):
        """供应商-修改供应商"""
        url = self.config.Url.v1_store_suppliers
        response = self.request(url=url, method='PUT', headers=self.headers, json=params)
        return response

    def v1_store_suppliers_delete(self, supplier_id='393'):
        """供应商-删除供应商"""
        url = self.config.Url.v1_store_suppliers + '/' + supplier_id
        response = self.request(url=url, method='DELETE', headers=self.headers)
        return response


    def v1_store_vip_levels_post(self, params: dict):
        """添加会员等级"""
        url = self.config.Url.v1_store_vip_levels
        response = self.request(url=url, method='POST', headers=self.headers, json=params)
        return response

    def v1_store_vip_levels_delete(self, level_id='2656'):
        """删除会员等级"""
        url = self.config.Url.v1_store_vip_levels + "/" + level_id
        response = self.request(url=url, method='DELETE', headers=self.headers)
        return response

    def v1_store_vip_levels_put(self, params: dict):
        """编辑会员等级"""
        url = self.config.Url.v1_store_vip_levels
        response = self.request(url=url, method='PUT', headers=self.headers, json=params)
        return response

    def v1_store_vip_levels_get(self):
        """查询等级"""
        url = self.config.Url.v1_store_vip_levels
        response = self.request(url=url, method='GET', headers=self.headers)
        return response

    def v1_store_vip_menmbers_level_get(self, number='13085060818'):
        """查询会员等级信息"""
        url = self.config.Url.v1_store_vip_member_detail + '/' + number + '/level'
        response = self.request(url=url, method='GET', headers=self.headers)
        return response

    def v1_store_coupon_batches_post(self, params: dict):
        """添加卡券批次"""
        url = self.config.Url.v1_store_coupon_batches
        response = self.request(url=url, method='POST', headers=self.headers, json=params)
        return response

    def v1_store_coupon_batches_coupon_batch_id_get(self, params: dict, coupon_batch_id='1428'):
        """获取卡券批次"""
        url = self.config.Url.v1_store_coupon_batches + '/' + coupon_batch_id +'/coupons'
        response = self.request(url=url, method='GET', headers=self.headers, params=params)
        return response

    def v1_store_coupon_batches_get(self, params: dict):
        """获取卡券批次列表"""
        url = self.config.Url.v1_store_coupon_batches
        response = self.request(url=url, method='GET', headers=self.headers,params=params)
        return response

    def v1_store_coupon_batches_coupon_batch_id_coupons_get(self, params: dict, coupon_batch_id='1418'):
        """获取卡券批次下的卡券列表"""
        url = self.config.Url.v1_store_coupon_batches + '/' + coupon_batch_id + '/coupons'
        response = self.request(url=url, method='GET', headers=self.headers, params=params)
        return response

    def v1_store_coupon_batches_coupon_batch_id_vip_coupons_post(self, params: dict, coupon_batch_id='467467734634'):
        """批量发券"""
        url = self.config.Url.v1_store_coupon_batches + '/' + coupon_batch_id + '/vip_coupons'
        response = self.request(url=url, method='POST', headers=self.headers, json=params)
        return response

    def v1_store_coupon_batches_coupon_batch_id_status_put(self, coupon_batch_id='1429'):
        """停用卡券批次"""
        url = self.config.Url.v1_store_coupon_batches + '/' + coupon_batch_id + '/status'
        response = self.request(url=url, method='PUT', headers=self.headers)
        return response

    def v1_store_coupon_batches_coupon_batch_id_export_get(self, coupon_batch_id='467467734634'):
        """导出卡券"""
        url = self.config.Url.v1_store_coupon_batches + '/' + coupon_batch_id + '/export'
        response = self.request(url=url, method='GET', headers=self.headers)
        print(type(response))
        return response

    def v1_store_coupon_batches_coupons_code_get(self, code='20750246990848'):
        """卡券编号查询卡券信息(具体的卡券码)"""
        url = self.config.Url.v1_store_coupon_batches_coupons + '/' + code
        response = self.request(url=url, method='GET', headers=self.headers)
        return response

    def v1_store_coupon_batches_info_get(self, trading_entity='37017996', coupon_batch_id='1429'):
        """获取优惠券详细信息"""
        url = self.config.Url.v1_store_coupon_batches_info + '/' + trading_entity + '/' + coupon_batch_id
        response = self.request(url=url, method='GET', headers=self.headers)
        return response





if __name__ == '__main__':
    api = StoreWebApi(username="13085060818", password="123456", version='1', trading_entity="37017996", print_results=True)
    # res1 = api.v2_store_products_spec_name_post({'spec_name': '尺寸'}).data  #添加商品规格名
    # res = api.v2_store_products_spec_get(spec_name='尺寸') #指定查询某个规格
    # res = api.v2_store_products_spec_get() #查询店铺所有规格
    #res = api.v2_store_products_spec_value_post({"spec_name_id": "5", "spec_value": "超大"}) #添加商品规格值
    # res = api.v2_store_products_goods_get({'page_number': 1, 'page_size': 30}) # 查询店铺商品
    # res = api.v2_store_products_batch_delete({"product_id_list": [43357]}) #删除商品
    # res = api.v2_store_products_goods_get({'page_number': 1, 'page_size': 30}) # 查询单品
    # res = api.v1_store_storehouse_post({'date':1592214039914,"supplier_id": 352,"remark": "","goods_list":[{"item_id": 59844,"price": "4.00","quantity": "5"}]})  # 仓库进货
    # print(time.time())
    # res = api.v1_store_storehouse_statistics_get({'begin_date': 1590940800000, 'end_date': 1593532799999})  # 仓库统计
    # res = api.v1_store_suppliers_get()             # 查询供应商列表
    # res = api.v1_store_suppliers_post({"phone": "13098760098", "remark": "一个咖啡店", "supplier_id": 305204312207360, "supplier_name": "lost cafe", "contact_person": "kun", "create_time": 1593482857377})  # 新增供应商
    # res = api.v1_store_suppliers_put({"phone": "19905421365", "remark": "接口测试", "supplier_id": 355, "supplier_name": "9894", "contact_person": "小王", "create_time": 1592552035000})   #修改供应商
    # res = api.v1_store_suppliers_delete('355')   # 删除供应商
    # res = api.v1_store_vip_levels_post({"level_name": "黄金", "upgrade_condition": "1", "upgrade_exponent": "150"})   #添加会员等级
    # res = api.v1_store_vip_levels_delete('388266689622016')  #删除会员等级
    # res = api.v1_store_vip_levels_put({"level_id": 802, "level_name": "a卡nh", "upgrade_condition": 1, "upgrade_exponent": 100}) #编辑会员等级
    # res = api.v1_store_vip_levels_get()  # 查询等级
    # res = api.v1_store_vip_menmbers_level_get()   # 查询会员等级信息
    # res = api.v1_store_coupon_batches_get({'page_number': 1, 'page_size': 30})   # 获取卡券批次列表
    # res = api.v1_store_coupon_batches_coupon_batch_id_get({'page_number': 1, 'page_size': 30}, '1428')    # 获取卡券批次
    # res = api.v1_store_coupon_batches_post({"amount": 0.0, "amount_limit": 50.0, "begin_time": 1593705600000, "discount": 80, "end_time": 1596470399999,
    #  "coupon_batch_id": "", "name": "测试卡", "quantity": 5, "use_remark": "不退换、不折现", "status": 1, "surplus_quantity": 0,
    #  "type": 1})
    # res = api.v1_store_coupon_batches_info_get()   # 获取优惠券详细信息
    # res = api.v1_store_coupon_batches_coupons_code_get('20750246990848')   # 卡券编号查询卡券信息
    # res = api.v1_store_coupon_batches_coupon_batch_id_status_put()  # 停用卡券批次
    # res = api.v1_store_coupon_batches_coupon_batch_id_vip_coupons_post({"tag_ids": [], "vip_ids": [8667, 8663]}, '1452')   # 批量发券
    # res = api.v1_store_coupon_batches_coupon_batch_id_coupons_get({'page_number': 1, 'page_size': 30}, '1418')    # 获取卡券批次下的卡券列表
    res = api.v1_store_coupon_batches_coupon_batch_id_export_get('1418')  # 导出卡券
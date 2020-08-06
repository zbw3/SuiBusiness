#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : mocobk
# @Email  : mailmzb@qq.com
# @Time   : 2020/8/5 16:18
import random

import pytest

from ProductApi.MiniProgramForm.form.enum import CatalogType, RoleType, FormDataStatus
from test_cases.mp_form import create_form, create_form_data, get_form_data


def get_goods_price(form_catalogs):
    for item in form_catalogs:
        if RoleType(item['role']) == RoleType.PRICE:
            return float(item['content'])


def get_form_data_amount(form_data):
    goods_catalogs = filter(lambda item: CatalogType(item['catalogType']) == CatalogType.GOODS, form_data['catalogs'])
    amount = []
    for goods_catalog in goods_catalogs:
        amount.append(int(goods_catalog['value']) * get_goods_price(goods_catalog['formCatalogs']))
    return sum(amount)


class UserData:
    def __init__(self):
        self.sequence = None
        self.form_data = None
        self.amount = None
        self.fuid = None
        self.order_id = None


@pytest.fixture(scope='module')
def create_order(user1, user2, default_shopping_form):
    """
    创建 3 个订单，分别 user1 2 个， user2 1 个
    """
    default_shopping_form.set_title('测试订单列表')
    form_id = create_form(user1, default_shopping_form)
    user1_data1 = UserData()
    user1_data2 = UserData()
    user2_data1 = UserData()

    user1_data1.sequence = create_form_data(user1, form_id)
    user1_data2.sequence = create_form_data(user1, form_id)
    user2_data1.sequence = create_form_data(user2, form_id)

    user1_data1.form_data = get_form_data(user1, form_id, index=1)
    user1_data2.form_data = get_form_data(user1, form_id, index=0)
    user2_data1.form_data = get_form_data(user2, form_id, index=0)

    user1_data1.amount = get_form_data_amount(user1_data1.form_data)
    user1_data2.amount = get_form_data_amount(user1_data2.form_data)
    user2_data1.amount = get_form_data_amount(user2_data1.form_data)
    return form_id, user1_data1, user1_data2, user2_data1


def test_get_order_list(user1, create_order):
    """验证订单列表获取正确"""
    form_id, user1_data1, user1_data2, user2_data1 = create_order

    res = user1.v1_order_list_form_id(form_id, method=user1.GET)
    assert res.status_code == 200

    data = res.data.get('data')
    predict_amount = user1_data1.amount + user1_data2.amount + user2_data1.amount
    assert data['amount'] == predict_amount

    order_details_list = data['orderDetails']
    assert len(order_details_list) == 3

    assert order_details_list[0]['sequence'] == user2_data1.sequence
    assert order_details_list[1]['sequence'] == user1_data2.sequence
    assert order_details_list[2]['sequence'] == user1_data1.sequence

    assert order_details_list[0]['queryFlag'] is False
    assert order_details_list[1]['queryFlag'] is True
    assert order_details_list[2]['queryFlag'] is True


def test_order_query(user1, create_order):
    """验证订单搜索获取列表正确"""
    form_id, user1_data1, _, _ = create_order
    res = user1.v1_order_query_form_id_fuid(form_id, fuid=user1_data1.form_data['fuid'], method=user1.GET)
    assert res.status_code == 200
    assert len(res.data.get('data', {}).get('orderDetails', [])) == 2


def test_get_order_detail(user1, create_order):
    """验证获取订单详情正确"""
    form_id, _, user2_data1, _ = create_order
    res = user1.v1_order_form_id_order_id(form_id, user2_data1.form_data['fid'], method=user1.GET)
    assert res.status_code == 200
    assert res.data.get('data')


def test_cancel_order(user1, create_order):
    """验证管理员取消订单正确"""
    form_id, _, user2_data1, _ = create_order
    res = user1.v1_order_form_id_order_id(form_id, user2_data1.form_data['fid'], method=user1.DELETE)
    assert res.status_code == 204

    res = user1.v1_order_form_id_order_id(form_id, user2_data1.form_data['fid'], method=user1.GET)
    assert FormDataStatus(res.data.get('data', {}).get('status')) == FormDataStatus.CANCELED


def test_post_seller_remarks(user1, create_order):
    """验证添加管理员备注正确"""
    form_id, _, user1_data2, _ = create_order
    remarks = f'这是卖家备注{random.randint(1000, 9999)}'
    res = user1.v1_order_form_id_order_id_remarks(form_id, user1_data2.form_data['fid'], remarks, method=user1.POST)
    assert res.status_code == 204
    res = user1.v1_order_form_id_order_id(form_id, user1_data2.form_data['fid'], method=user1.GET)
    for catalog in res.data.get('data', {}).get('catalogs'):
        if CatalogType(catalog['catalogType']) == CatalogType.SELLER_REMARKS:
            assert catalog['value'] == remarks
            break


def test_put_seller_remarks(user1, create_order):
    """验证修改管理员备注正确"""
    form_id, _, _, user2_data1 = create_order
    remarks1 = f'这是卖家备注{random.randint(1000, 9999)}'
    res = user1.v1_order_form_id_order_id_remarks(form_id, user2_data1.form_data['fid'], remarks1, method=user1.POST)
    assert res.status_code == 204

    remarks2 = f'这是更新后的卖家备注{random.randint(1000, 9999)}'
    res = user1.v1_order_form_id_order_id_remarks(form_id, user2_data1.form_data['fid'], remarks2, method=user1.PUT)
    assert res.status_code == 204

    res = user1.v1_order_form_id_order_id(form_id, user2_data1.form_data['fid'], method=user1.GET)
    for catalog in res.data.get('data', {}).get('catalogs'):
        if CatalogType(catalog['catalogType']) == CatalogType.SELLER_REMARKS:
            assert catalog['value'] == remarks2
            break


if __name__ == '__main__':
    pytest.main()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : mocobk
# @Email  : mailmzb@qq.com
# @Time   : 2020/8/18 10:33

import pytest
from test_cases.mp_form import verify_post_form, create_numerous_form_data


def create_many_order_shopping_form(user1, user2, default_shopping_form, number=10):
    """创建有多个接龙的 [商品接龙] 表单"""
    default_shopping_form.set_title(f'测试多个接龙/订单（{number}）')
    form_id = verify_post_form(user1, default_shopping_form)
    create_numerous_form_data(user1, user2, form_id=form_id, number=number)
    return form_id


def test_statistic_detail_no_end_time(user1, user2, default_shopping_form, number=10):
    """订单详情-没有结束时间"""
    form_id = create_many_order_shopping_form(user1, user2, default_shopping_form, number)
    res = user1.v1_statistic_detail_form_id(form_id, 'SEQUENCE', 'ASC', '2020-12-31 00:00:00', '')
    assert res.status_code == 200, res.text

def test_statistic_detail_no_start_time(user1, user2, default_shopping_form, number=10):
    """订单详情-没有开始时间"""
    form_id = create_many_order_shopping_form(user1, user2, default_shopping_form, number)
    res = user1.v1_statistic_detail_form_id(form_id, 'SEQUENCE', 'ASC', '',  '2020-12-31 00:00:00')
    assert res.status_code == 200, res.text

def test_statistic_detail(user1, user2, default_shopping_form, number=10):
    """订单详情-开始时间和结束时间满足条件"""
    form_id = create_many_order_shopping_form(user1, user2, default_shopping_form, number)
    res = user1.v1_statistic_detail_form_id(form_id, 'SEQUENCE', 'ASC', '2020-12-31 00:00:00', '2020-12-31 23:59:59')
    assert res.status_code == 200, res.text

def test_statistic_detail_error_time(user1, user2, default_shopping_form, number=10):
    """订单详情-开始时间晚于结束时间"""
    form_id = create_many_order_shopping_form(user1, user2, default_shopping_form, number)
    res = user1.v1_statistic_detail_form_id(form_id, 'SEQUENCE', 'ASC', '2020-12-31 00:00:00', '2020-12-30 00:00:00')
    assert res.status_code == 200, res.text

def test_statistic_analysis(user1, user2, default_shopping_form, number=10):
    """订单分析-时间满足条件"""
    form_id = create_many_order_shopping_form(user1, user2, default_shopping_form, number)
    res = user1.v1_statistic_analysis_form_id(form_id, '2020-12-30 00:00:00', '2020-12-31 00:00:00')
    assert res.status_code == 200, res.text

def test_statistic_analysis_no_start(user1, user2, default_shopping_form, number=10):
    """订单分析-没有开始时间"""
    form_id = create_many_order_shopping_form(user1, user2, default_shopping_form, number)
    res = user1.v1_statistic_analysis_form_id(form_id, '', '2020-12-31 00:00:00')
    assert res.status_code == 200, res.text

def test_statistic_analysis_no_end(user1, user2, default_shopping_form, number=10):
    """订单分析-没有结束时间"""
    form_id = create_many_order_shopping_form(user1, user2, default_shopping_form, number)
    res = user1.v1_statistic_analysis_form_id(form_id, '2020-12-30 00:00:00', '')
    assert res.status_code == 200, res.text

def test_statistic_analysis_error_time(user1, user2, default_shopping_form, number=10):
    """订单分析-开始时间晚于结束时间"""
    form_id = create_many_order_shopping_form(user1, user2, default_shopping_form, number)
    res = user1.v1_statistic_analysis_form_id(form_id, '2020-12-31 23:59:59', '2020-12-31 00:00:00')
    assert res.status_code == 200, res.text




if __name__ == '__main__':
    pytest.main()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : mocobk
# @Email  : mailmzb@qq.com
# @Time   : 2020/8/18 10:33

# def create_many_order_shopping_form(user1, user2, default_shopping_form, number=10):
#     """创建有多个接龙的 [商品接龙] 表单"""
#     default_shopping_form.set_title(f'测试多个接龙/订单（{number}）')
#     form_id = verify_post_form(user1, default_shopping_form)
#     create_numerous_form_data(user1, user2, form_id=form_id, number=number)

def test_statistic_analysis(user1):
    res = user1.v1_statistic_analysis_form_id('1061367683649376279')
    print(res.text)
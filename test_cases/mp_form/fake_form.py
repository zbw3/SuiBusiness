#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File   : test_fake_form.py
# @Author : mocobk
# @Email  : mailmzb@qq.com
# @Time   : 2020/7/27 14:56
"""
该用例主要是为了快速构造旧版本的表单数据，以便观察是否有数据兼容问题出现
"""
import random
import time
import pytest


from ProductApi.MiniProgramForm.form.enum import FormStatus
from test_cases.mp_form import verify_post_form, create_form, create_form_data, create_numerous_form_data


def test_create_normal_activity_form(user1, default_activity_form):
    """创建正常进行中的 [活动接龙] 表单"""
    default_activity_form.set_title('进行中-含填写项11')
    # default_activity_form.set_duration_time("2020-11-21 14:39:00", "2020-12-21 14:39:00")
    #
    # default_activity_form.set_limit("90")
    # default_activity_form.set_per_limit("10")
    default_activity_form.set_cycle(127, 800, 1800)
    verify_post_form(user1, default_activity_form)


def test_create_normal_with_no_question_activity_form(user1, default_activity_form):
    """创建正常进行中的 [活动接龙] 表单"""
    default_activity_form.set_title('进行中-无填写项')
    default_activity_form.clear_questions()
    verify_post_form(user1, default_activity_form)


def test_create_paused_activity_form(user1, default_activity_form):
    """创建停止中的 [活动接龙] 表单"""
    default_activity_form.set_title('停止中-含填写项')
    form_id = verify_post_form(user1, default_activity_form)
    update_status_res = user1.v1_form_id_status(form_id, FormStatus.PAUSED.value)
    assert update_status_res.status_code == 204


def test_create_unopened_activity_form(user1, default_activity_form):
    """创建未开启的 [活动接龙] 表单"""
    default_activity_form.set_title('未开启-含填写项')
    default_activity_form.set_duration_time(start=default_activity_form.now_offset(days=1))
    verify_post_form(user1, default_activity_form)


def test_create_finished_activity_form(user1, default_activity_form):
    """创建已结束的 [活动接龙] 表单"""
    default_activity_form.set_title('已结束-含填写项')
    default_activity_form.set_duration_time(end=default_activity_form.now_offset(seconds=1))
    verify_post_form(user1, default_activity_form)


"""
=================================================================================================
"""


def test_create_normal_shopping_form(user1, default_shopping_form):
    """创建正常进行中的 [商品接龙] 表单"""
    default_shopping_form.set_title('进行中-含填写项')
    verify_post_form(user1, default_shopping_form)


def test_create_normal_with_no_question_shopping_form(user1, default_shopping_form):
    """创建正常进行中的 [商品接龙] 表单"""
    default_shopping_form.set_title('进行中-无填写项')
    default_shopping_form.clear_questions()
    verify_post_form(user1, default_shopping_form)


def test_create_paused_shopping_form(user1, default_shopping_form):
    """创建停止中的 [商品接龙] 表单"""
    default_shopping_form.set_title('停止中-含填写项')
    form_id = verify_post_form(user1, default_shopping_form)
    update_status_res = user1.v1_form_id_status(form_id, FormStatus.PAUSED.value)
    assert update_status_res.status_code == 204


def test_create_unopened_shopping_form(user1, default_shopping_form):
    """创建未开启的 [商品接龙] 表单"""
    default_shopping_form.set_title('未开启-含填写项')
    default_shopping_form.set_duration_time(start=default_shopping_form.now_offset(days=1))
    verify_post_form(user1, default_shopping_form)


def test_create_finished_shopping_form(user1, default_shopping_form):
    """创建已结束的 [商品接龙] 表单"""
    default_shopping_form.set_title('已结束-含填写项')
    default_shopping_form.set_duration_time(end=default_shopping_form.now_offset(seconds=1))
    verify_post_form(user1, default_shopping_form)


"""
=================================================================================================
"""

def test_create_many_order_shopping_form(user1, user2,user3,default_activity_form , number=200):
    """
    创建有多个接龙的 [商品接龙] 表单,
    number： 为接龙数
    user: 可以添加多个，会随机选择接龙
    """
    default_activity_form .set_title(f'测试多个接龙/订单统计分析2（{number}）')
    default_activity_form .set_cycle(127, 800, 2300)
    time.sleep(200)
    form_id = verify_post_form(user1, default_activity_form )    #  default_activity_form    default_shopping_form
    create_numerous_form_data(user1, user2, user3, form_id=form_id, number=number)
    print(form_id)


def test_add_form_data(user1, user2,user3,user4,user5,user6,user7,default_activity_form , number=200,form_id = 1283253971457634305):
    """
    对指定表单添加多条接龙，
    form_id:为需要增加接龙的表单
    :param number: 为接龙数目
    :return:
    """
    create_numerous_form_data(user1,user2, user3,user4,user5,user6,user7, form_id=form_id, number=number)




if __name__ == '__main__':
    pytest.main()

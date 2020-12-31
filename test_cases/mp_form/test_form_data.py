#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File   : test_post_and_put_form_data.py
# @Author : mocobk
# @Email  : mailmzb@qq.com
# @Time   : 2020/7/27 14:56
import pytest

from ProductApi.MiniProgramForm.api import FormApi
from ProductApi.MiniProgramForm.form import PostFormData
from test_cases.mp_form import verify_post_form_data, verify_put_form_data, verify_cancel_form_data, create_form


@pytest.fixture()
def form_ids(user1, default_activity_form, default_shopping_form):
    """
    创建活动报名和团购接龙表单，总报接龙次数限制 3， 每人接龙次数限制 2
    :return tuple[form_id]
    """
    default_activity_form.set_title('普通表单不循环-验证转化用')
    default_shopping_form.set_title('普通表单不循环-验证转化用')
    default_activity_form.set_limit(3)
    # default_activity_form.set_cycle(127, 800, 1030)
    default_activity_form.set_per_limit(2)
    default_shopping_form.set_limit(3)
    default_shopping_form.set_per_limit(2)
    # default_shopping_form.set_cycle(127, 800, 1030)
    form_ids = create_form(user1, default_activity_form), create_form(user1, default_shopping_form)
    return form_ids


def post_form_data(form_api: FormApi, form_id: str):
    """
    :param form_api:
    :param form_id:
    :return: response
    """
    post_form_data = PostFormData(form_api, form_id).data
    res = form_api.v1_form_id_form_data(form_id, post_form_data, method=form_api.POST)
    return res


def post_form_data_twice(user: FormApi, form_id: str):
    """连续接龙2次"""
    for i in range(1, 3):
        response = post_form_data(user, form_id)
        assert response.status_code == 200, response.text
        assert response.data.get('data', {}).get('sequence') == i, response.text




def test_post_form_data(user1, user2, form_ids):
    """验证提交接龙数据"""
    for form in form_ids:
        verify_post_form_data(user1, user2, form)


def test_put_form_data(user2, form_ids):
    """验证修改接龙数据"""
    for form in form_ids:
        verify_put_form_data(user2, form)


def test_cancel_form_data(user2, form_ids):
    """验证取消接龙数据"""
    for form in form_ids:
        verify_cancel_form_data(user2, form)


def test_post_form_data_over_limit(user1, user2, form_ids):
    """验证单个接龙人数未达上限，总接龙人数达上限"""
    for form_id in form_ids:
        post_form_data_twice(user2, form_id)

        response = post_form_data(user1, form_id)
        assert response.status_code == 200, response.text

        response = post_form_data(user1, form_id)
        assert response.status_code == 422, response.text
        assert response.data.get('code') == 13356, response.text


def test_post_form_data_over_per_limit(user2, form_ids):
    """验证总接龙人数未达上限，单个接龙人接龙次数达上限"""
    for form_id in form_ids:
        post_form_data_twice(user2, form_id)

        response = post_form_data(user2, form_id)
        assert response.status_code == 422, response.text
        assert response.data.get('code') == 13426, response.text


def test_post_form_data_over_limit_and_per_limit(user1, user2, form_ids):
    """验证总接龙人数和单个接龙人次都达上限，优先提示单个接龙人接龙次数达上限"""
    for form_id in form_ids:
        post_form_data_twice(user2, form_id)

        response = post_form_data(user1, form_id)
        assert response.status_code == 200, response.text

        response = post_form_data(user2, form_id)
        assert response.status_code == 422, response.text
        assert response.data.get('code') == 13426, response.text


def test_query_form_id_cycle_form_datas(user1, user2, form_ids):
    """验证获取今日循环表单的报名数据"""
    for form_id in form_ids:
        verify_post_form_data(user1, user2, form_id)

        response = user1.v1_form_id_cycle_form_datas(form_id)
        assert response.status_code == 200, response.text
        assert len(response.data.get('data')) == 2

        for i in range(0, len(response.data.get('data'))):
            assert response.data.get('data')[i].get('status') == 0
            assert response.data.get('data')[i].get('sequence') == 2-i


def test_cancel_form_id_cycle_form_datas(user2, form_ids):
    """获取取消报名数据"""
    for form_id in form_ids:
        verify_post_form_data(user1, user2, form_id)
        verify_cancel_form_data(user2, form_id)

        response = user2.v1_form_id_cycle_form_datas(form_id)
        assert response.status_code == 200, response.text
        assert response.data.get('data')[0].get('status') == -1


def test_form_id_cycle_ranking(user1, user2, form_ids):
    """"循环表单排行榜获取"""
    for form_id in form_ids:
        verify_post_form_data(user1,user2,form_id)
        verify_cancel_form_data(user2, form_id)
        response = user1.v1_form_id_cycle_ranking(form_id)
        assert response.status_code == 200,response.text
        assert response.data.get("data")[0].get('fuid') == FormApi.USER.user1 and response.data.get("data")[0].get('days') == 1
        assert response.data.get("data")[1].get('fuid') == FormApi.USER.user2 and response.data.get("data")[1].get('days') == 0


def test_query_form_id_cycle_form_datas(user1, user2, form_ids):
    """验证获取今日循环表单的报名数据"""
    for form_id in form_ids:
        verify_post_form_data(user1, user2, form_id)

        response = user1.v1_form_id_cycle_form_datas(form_id)
        assert response.status_code == 200, response.text
        assert len(response.data.get('data')) == 2

        for i in range(0, len(response.data.get('data'))):
            assert response.data.get('data')[i].get('status') == 0
            assert response.data.get('data')[i].get('sequence') == 2-i


def test_cancel_form_id_cycle_form_datas(user2, form_ids):
    """获取取消报名数据"""
    for form_id in form_ids:
        verify_cancel_form_data(user2, form_id)

        response = user2.v1_form_id_cycle_form_datas(form_id)
        assert response.status_code == 200, response.text
        assert response.data.get('data')[0].get('status') == -1


def test_complaint(user1,form_ids):
    "举报你三次"
    for i in range (0,3):
        reason = i
        for form_id in form_ids:
            pictures=['https://oss.feidee.cn/oss/form_6b8754320b6ea286_495X401.gif','https://oss.feidee.cn/oss/form_927aaca78713bbaa_500X500.jpg','https://oss.feidee.cn/oss/form_2d89ac01d6d5d00b_500X500.jpg','https://oss.feidee.cn/oss/form_7cbae0658c918533_224X224.jpg']
            response = user1.v1_complaint(form_id,reason,description="投诉",images=pictures,contact="abc123")
            assert response.status_code == 200
            assert response.data.get("code")== 0

    "验证获取投诉原因枚举"
    reason_reponse = user1.v1_comlpaint_reason()
    reason_value = ["其他","新冠肺炎疫情相关","色情","诱导","骚扰","欺诈","恶意营销","与服务类目不符","违法犯罪","侵权（冒名、诽谤、抄袭）","不实信息","隐私信息收集"]
    for id in range (0,len(reason_value)):
        if id == 0:
            assert reason_reponse.status_code == 200
            assert reason_reponse.data.get("data")[11].get("key")=="0"
            assert reason_reponse.data.get("data")[11].get("value")==reason_value[0]
            pass
        else:
            assert reason_reponse.status_code == 200
            assert reason_reponse.data.get("data")[id-1].get("key") == str(id)
            assert reason_reponse.data.get("data")[id-1].get("value") == reason_value[id]






if __name__ == '__main__':
    pytest.main()

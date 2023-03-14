#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File   : test_name_list.py
# @Email  : xuexia_xu@feidee.com
# @Time   :2023/3/9 11:06:00
"""
预设名单相关接口
"""
import pytest
import time

@pytest.mark.xfail(reason='已废弃')
def test_name_list_nlid(user1):
    """
    获取预设名单
    :param user1:
    :return:
    """
    pass

@pytest.mark.xfail(reason='已废弃')
def test_name_list(user1):
    """
    创建预设名单
    :param user1:
    :return:
    """
    pass

@pytest.mark.xfail(reason='已废弃')
def test_name_list_nlid_put(user1):
    """
    修改预设名单
    :param user1:
    :return:
    """
    pass

@pytest.mark.xfail(reason='已废弃')
def test_name_list_copy(user1):
    """
    复制预设名单
    :param user1:
    :return:
    """
    pass

def test_name_list_used(user1,default_formId_dataId_commentId):
    """
    获取表单预设名单中各名单的报名状态
    :param user1:
    :return:
    """
    form_id = default_formId_dataId_commentId.form_id
    response = user1.v1_name_list_used(form_id)
    assert response.status_code == 200,response.text

def test_name_list_orderd_used(user1,default_formId_dataId_commentId):
    """
    按预设名单顺序获取表单中开启的预设名单报名状态
    :param user1:
    :return:
    """
    form_id = default_formId_dataId_commentId.form_id
    response = user1.v1_name_order_used(form_id)
    assert response.status_code == 200, response.text

@pytest.mark.xfail(reason='404')
def test_name_list_form_data_list(user1,default_formId_dataId_commentId):
    """
    预设名单详情列表
    :param user1:
    :return:
    """
    form_id = default_formId_dataId_commentId.form_id
    response = user1.v1_name_form_data_list(form_id,name='徐雪霞',page_no=1,page_size=5)
    assert response.status_code == 200, response.text

def test_name_list_template_post(user1):
    """
    获取预设名单模板列表
    :param user1:
    :return:
    """
    data = {"templateName":"三年三班","originData":"徐雪霞、秦卓珈、韩一芳","value":[{"name":"徐雪霞"},{"name":"秦卓珈"},{"name":"韩一芳"}]}
    name_list_template_response = user1.v1_form_name_list_template(name_list=data, method=user1.POST)
    assert name_list_template_response.status_code == 200, name_list_template_response.text


def test_name_list_template_get(user1):
    """
    获取预设名单模板列表
    :param user1:
    :return:
    """
    name_list_template_response = user1.v1_form_name_list_template(name_list={},method=user1.GET)
    assert name_list_template_response.status_code == 200,name_list_template_response.text



def test_name_list_template_put(user1):
    """
    获取预设名单模板列表
    :param user1:
    :return:
    """
    name_list_template_response = user1.v1_form_name_list_template(name_list={}, method=user1.GET)
    assert name_list_template_response.status_code == 200, name_list_template_response.text
    nlid = name_list_template_response.json()['data'][0]['nlid']
    template_name = f'{"三年三班2"}-{time.strftime("%T")}'
    data = {"nlid":nlid,"templateName":template_name,"originData":"徐雪霞、秦卓珈、韩一芳","value":[{"name":"徐雪霞"},{"name":"秦卓珈"},{"name":"韩一芳"}]}
    name_list_template_response = user1.v1_form_name_list_template(name_list=data, method=user1.PUT)
    assert name_list_template_response.status_code == 204, name_list_template_response.text



def test_name_list_template_delete(user1,default_formId_dataId_commentId):
    """
    删除预设名单模板
    :param user1:
    :return:
    """
    name_list_template_response = user1.v1_form_name_list_template(name_list={}, method=user1.GET)
    assert name_list_template_response.status_code == 200, name_list_template_response.text
    template = name_list_template_response.data.get('data', {})
    nlid = name_list_template_response.json()['data'][len(template)-1]['nlid']
    name_list_template_response = user1.v1_form_name_list_template_delete(nlid=nlid)
    assert name_list_template_response.status_code == 204, name_list_template_response.text

def test_name_list_form_datas(user1,default_formId_dataId_commentId):
    """
    根据预设名单名字查询报名数据
    :param user1:
    :return:
    """
    form_id = default_formId_dataId_commentId.form_id
    response = user1.v1_name_list_form_datas(form_id, name='徐雪霞', page_no=1, page_size=5)
    assert response.status_code == 200, response.text

def test_name_list_not_filled(user1,default_formId_dataId_commentId):
    """
    预设名单未填写名单列表
    :param user1:
    :return:
    """
    form_id = default_formId_dataId_commentId.form_id
    response = user1.v1_name_list_not_filled(form_id)
    assert response.status_code == 200, response.text


def test_name_list_filled_notify(user1,default_formId_dataId_commentId):
    """
    一键通知未填人员
    :param user1:
    :return:
    """
    form_id = default_formId_dataId_commentId.form_id
    date = time.strftime("%Y%m%d",time.localtime())
    response = user1.v1_name_list_filled_notify(form_id,date)
    assert response.status_code == 200, response.text


if __name__ == '__main__':
    pytest.main(['-vs', 'test_name_list.py'])

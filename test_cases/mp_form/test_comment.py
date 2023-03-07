#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File   : test_comment.py
# @Email  : xuexia_xu@feidee.com
# @Time   :2023/2/28 15:45:00
"""
点赞 评论 评级 相关
"""
import pytest
import pickle
from test_cases.mp_form import verify_post_form, verify_put_form, create_form
from test_cases.mp_form.test_form_data import post_form_data

def get_txt_data():
    """
    获取txt文件中的form_id,form_data_id,fid,rid
    :return:
    """
    with open('./test.txt', 'rb') as f:
        data = pickle.load(f)
        form_id = data['form_id']
        form_data_id = data['form_data_id']
        fid =  data['fid']
    return form_id,form_data_id,fid

def test_form_comment(user1,default_activity_form):
    """
    报名数据新增评论
    :param user1:
    :param default_activity_form:
    :return:
    """
    form_id = verify_post_form(user1, default_activity_form)
    response = post_form_data(user1, form_id)
    assert response.status_code == 200, response.text
    form_data_id = response.json()['data']['fid']
    comment_response = user1.v1_form_comment_post(form_id,form_data_id)
    assert comment_response.status_code == 200
    fid = comment_response.json()['data']['fid']

    # 将form_id、form_data_id保存起来，供后续使用
    with open('./test.txt', 'wb') as f:
        data = {'form_id':form_id,'form_data_id':form_data_id,'fid':fid}
        pickle.dump(data,f)

def test_form_comment_delete(user1):
    """
    报名数据删除评论
    :param user1:
    :param default_activity_form:
    :return:
    """
    form_id,form_data_id,fid = get_txt_data()
    comment_response = user1.v1_form_comment_delete(form_id, form_data_id, fid)
    assert comment_response.status_code == 204

# @pytest.mark.run(order=3)
def test_form_like(user1):
    """
    报名数据点赞/取消点赞
    :param user1:
    :param default_activity_form:
    :return:
    """
    form_id,form_data_id,fid= get_txt_data()
    # 点赞
    like_response = user1.v1_form_like(form_id,form_data_id,1)
    assert like_response.status_code == 200
    # 取消点赞
    like_response = user1.v1_form_like(form_id, form_data_id, 0)
    assert like_response.status_code == 200

# @pytest.mark.run(order=2)
def test_form_like_get(user1):
    """
     分页获取表单数据点赞记录
    :param user1:
    :param default_activity_form:
    :return:
    """
    form_id,form_data_id,fid= get_txt_data()
    like_response = user1.v1_form_like_get(form_id,form_data_id)
    assert like_response.status_code == 200

def test_form_last_comment(user1):
    """
    获取用户对某个表单的最后一次评论
    :param user1:
    :param default_activity_form:
    :return:
    """
    form_id,form_data_id,fid = get_txt_data()
    last_comment = user1.v1_form_last_comment(form_id)
    assert last_comment.status_code == 200

def test_form_comment_get(user1):
    """
    分页获取表单数据评论记录
    :param user1:
    :param default_activity_form:
    :return:
    """
    form_id,form_data_id,fid = get_txt_data()
    page_comment = user1.v1_form_comment_page_get(form_id,form_data_id)
    assert page_comment.status_code == 200


def test_form_like_comment_rate_remark(user1):
    """
    根据报名数据id获取点赞评论评级备注相关数据
    :param user1:
    :param default_activity_form:
    :return:
    """
    form_id, form_data_id, fid= get_txt_data()
    page_comment = user1.v3_like_comment_rate_remark(form_id, form_data_id)
    assert page_comment.status_code == 200

def test_form_rate_config_post(user1):
    """
    创建评级配置，一个表单只能post一次
    :param user1:
    :param default_activity_form:
    :return:
    """
    form_id, form_data_id, fid= get_txt_data()
    rate = "优秀"
    rate_config = user1.v1_form_rate_config_post(form_id,rate)
    assert rate_config.status_code == 200
    rid = rate_config.json()['data']['items'][0]['rid']
    # 将form_id、form_data_id保存起来，供后续使用
    with open('./test.txt', 'wb') as f:
        data = {'form_id': form_id, 'form_data_id': form_data_id, 'fid': fid, 'rid': rid}
        pickle.dump(data, f)

def test_form_rate_config_get(user1):
    """
    创建评级配置
    :param user1:
    :param default_activity_form:
    :return:
    """
    form_id, form_data_id, fid= get_txt_data()
    page_comment = user1.v1_form_rate_config_get(form_id)
    assert page_comment.status_code == 200

@pytest.mark.xfail(reason='实际未使用')
def test_form_rate_config_delete(user1):
    """
    创建评级配置
    :param user1:
    :param default_activity_form:
    :return:
    """
    form_id, form_data_id, fid= get_txt_data()
    page_comment = user1.v1_form_rate_config_delete(form_id)
    assert page_comment.status_code == 200


def test_form_rate_config_put(user1):
    """
    修改评级配置
    :param user1:
    :param default_activity_form:
    :return:
    """
    form_id, form_data_id, fid= get_txt_data()
    rate = "优秀"
    rate_revise_config = user1.v1_form_rate_revise(form_id)
    assert rate_revise_config.status_code == 200
    rid = rate_revise_config.json()['data']['formDataRateConfig']['items'][0]['rid']
    version = rate_revise_config.json()['data']['formDataRateConfig']['version']
    page_comment = user1.v1_form_rate_config_put(form_id,version,rid,rate)
    assert page_comment.status_code == 200


def test_form_rate_post(user1):
    """
    对报名数据评级
    :param user1:
    :param default_activity_form:
    :return:
    """
    form_id, form_data_id, fid= get_txt_data()
    rate_revise_config = user1.v1_form_rate_revise(form_id)
    assert rate_revise_config.status_code == 200
    rid = rate_revise_config.json()['data']['formDataRateConfig']['items'][0]['rid']
    version = rate_revise_config.json()['data']['formDataRateConfig']['version']
    page_comment = user1.v1_form_rate(form_id,form_data_id,rid,version)
    assert page_comment.status_code == 200


def test_form_rate_revise(user1):
    """
     获取评级配置和订正功能开关
    :param user1:
    :param default_activity_form:
    :return:
    """
    form_id, form_data_id, fid= get_txt_data()
    page_comment = user1.v1_form_rate_revise(form_id)
    assert page_comment.status_code == 200


def test_formdata_attach(user1):
    """
     评论、评级、标签整合接口
    :param user1:
    :param default_activity_form:
    :return:
    """
    form_id, form_data_id, fid= get_txt_data()
    rate_revise_config = user1.v1_form_rate_revise(form_id)
    assert rate_revise_config.status_code == 200
    rid = rate_revise_config.json()['data']['formDataRateConfig']['items'][0]['rid']
    version = rate_revise_config.json()['data']['formDataRateConfig']['version']
    page_comment = user1.v1_formdata_attach(form_id,form_data_id,rid,version)
    assert page_comment.status_code == 200

if __name__ == '__main__':
    pytest.main(['-vs', 'test_comment.py'])



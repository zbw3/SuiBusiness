#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File   : test_v1_push_staff_info_get.py
# @Author : mocobk
# @Email  : mailmzb@qq.com
# @Time   : 2020/3/26 17:35
import pytest
from ProductApi.Push.api import PushApi
from settings.BaseConfig import Env
from test_cases.push.data import v1_push_data

print_results = True


def test_v1_push_staff_info_get_01():
    """获取地推人员信息，返回200，keys 正确"""
    data = v1_push_data.StaffInfoData.Data1
    api = PushApi(data.account.username, data.account.password, data.trading_entity, print_results)
    res = api
    assert res.status_code == 200
    assert sorted(res.data.keys()) == sorted(data.keys)


def test_v1_push_staffs_post_01():
    """提交未通过审核地推任意信息，返回400"""
    data = v1_push_data.StaffsData.Data1
    api = PushApi(data.account.username, data.account.password, data.trading_entity, print_results)
    res = api
    assert res.status_code == 400
    assert res.data['code'] == 4495


def test_v1_push_agent_enter_post_01():
    """提交未通过审核的供应商入驻信息，返回400"""
    data = v1_push_data.AgentEnterData.Data1
    api = PushApi(data.account.username, data.account.password, data.trading_entity, print_results)
    res = api
    assert res.status_code == 400
    assert res.data['code'] == 4495


def test_v1_push_agents_agent_detail_get_01():
    """代理商信息不存在，获取供应商详情，返回400"""
    data = v1_push_data.AgentsAgentDetailData.Data1
    api = PushApi(data.account.username, data.account.password, data.trading_entity, print_results)
    res = api.v1_push_agents_agent_detail_get()
    assert res.status_code == 400


def test_v1_push_staff_profit_get_01():
    """获取地推收益统计，返回200"""
    data = v1_push_data.StaffProfitData.Data1
    api = PushApi(data.account.username, data.account.password, data.trading_entity, print_results)
    res = api
    assert res.status_code == 200
    assert sorted(res.data.keys()) == sorted(data.keys)


def test_v1_push_staff_openInfo_get_01():
    """地推开户统计，返回200"""
    data = v1_push_data.StaffOpenInfoData.Data1
    api = PushApi(data.account.username, data.account.password, data.trading_entity, print_results)
    res = api
    assert res.status_code == 200
    assert isinstance(res.data, list) and len(res.data) > 0


@pytest.mark.skipif(Env().is_production, reason='生产环境上不对外网开放访问')
def test_v1_push_staff_image_post_01():
    """上传地推相关图片，返回201"""
    # TODO: 这个接口传错会返回错误的java代码信息
    # files content-type 必须指定才行 eg. 'image/jpeg'
    data = v1_push_data.StaffImageData.Data1
    api = PushApi(data.account.username, data.account.password, data.trading_entity, print_results)
    res = api
    assert res.status_code == 201
    assert res.data['id_name'] == '徐乐'
    assert res.data['id_number'] == '652901196611026716'


if __name__ == '__main__':
    pytest.main()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File   : api.py
# @Author : mocobk
# @Email  : mailmzb@qq.com
# @Time   : 2019/1/22 9:53
from ProductApi.Push import config
from ProductApi.Sui.api import Sui
from ProductApi.base import ApiBase


class PushApi(ApiBase):

    def __init__(self, username, password, trading_entity="3604098", print_results=False):
        """
        :param username: 用户名
        :param password: 密码
        :param trading_entity: 账本 ID
        """
        super().__init__(print_results)
        self.config: config.Test = getattr(config, self.env.name)
        self.headers = Sui(username, password).authorized_headers()
        self.headers["Trading-Entity"] = trading_entity

    def v1_push_staff_info_get(self):
        """
        Name: 获取地推人员信息
        """
        url = self.config.Url.v1_push_staff_info
        response = self.request(url=url, method='GET', headers=self.headers)
        return response

    def v1_push_staffs_post(self, params):
        """
        Name: 个人入驻或者加入供应商
        """
        url = self.config.Url.v1_push_staffs
        response = self.request(url=url, method='POST', json=params, headers=self.headers)
        return response

    def v1_push_agent_enter_post(self, params):
        """
        Name: 供应商入驻
        """
        url = self.config.Url.v1_push_agent_enter
        response = self.request(url=url, method='POST', json=params, headers=self.headers)
        return response

    def v1_push_agents_agent_detail_get(self):
        """
        Name: 获取供应商详情
        """
        url = self.config.Url.v1_push_agents_agent_detail
        response = self.request(url=url, method='GET', headers=self.headers)
        return response

    def v1_push_staff_profit_get(self):
        """
        GET /v1/push/staff/profit 地推收益统计
        """
        url = self.config.Url.v1_push_staff_profit
        response = self.request(url=url, method='GET', headers=self.headers)
        return response

    def v1_push_staff_openInfo_get(self):
        """
        GET /v1/push/staff/openInfo 地推开户统计
        """
        url = self.config.Url.v1_push_staff_openInfo
        response = self.request(url=url, method='GET', headers=self.headers)
        return response

    def v1_push_staff_image_post(self, params):
        """
        POST /v1/push/staff/image 上传地推相关图片
        """
        url = self.config.Url.v1_push_staff_image
        response = self.request(url=url, method='POST', data={'image_type': params['image_type']},
                                files={'image_file': params['image_file']}, headers=self.headers
                                )
        return response


if __name__ == '__main__':
    api = PushApi(username="119@kd.ssj", password="123456", print_results=True)
    # res1 = api.v1_push_staff_info_get().data

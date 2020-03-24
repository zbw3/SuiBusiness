#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File : data_v1_stroe_api.py
# @Author: GoGo
# @Date : 2020/3/20
# @Desc :

import time


class DataV1StroeApi:

    USERNAME = "119@kd.ssj"
    PASSWORD = "123456"
    Trading_Entity = "3604098"

    @staticmethod
    def data_post_v1_store_products_categorys():
        name = f"商品分类{int(time.time() * 1000)}"
        data = [{
            "case_no": "",
            "case_info": "添加商品分类,添加成功",
            "case_data": {
                "name": name
            },
            "check_data": {
                "status_code": 201
            }
        }, {
            "case_no": "",
            "case_info": "添加商品分类,重复添加，添加失败",
            "case_data": {
                "name": name
            },
            "check_data": {
                "status_code": 400,
                "code": 4445,
                "message": "分类名称不能重复，请重新设置"
            }
        }, {
            "case_no": "",
            "case_info": "添加商品分类,name为空",
            "case_data": {
                "name": ""
            },
            "check_data": {
                "status_code": 400,
                "code": 4357,
                "message": "客户端参数解析失败"
            }
        }]
        return data

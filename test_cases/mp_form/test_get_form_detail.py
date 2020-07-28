#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File   : test_get_form_detail.py
# @Author : mocobk
# @Email  : mailmzb@qq.com
# @Time   : 2020/7/27 14:56
import pytest

from libs.JsonUtils import json_diff


def test_normal_form_details(mocobk, default_activity_form, default_shopping_form):
    """验证进行中的表单详情数据"""

    for form in [default_activity_form, default_shopping_form]:
        form_data = form.data
        res1 = mocobk.v1_form(form_data, return_form_id=True)
        assert res1.status_code == 204
        res2 = mocobk.v1_form_form_id_get(res1.form_id)
        assert res2.status_code == 200
        data = res2.data.get('data', {})
        assert data.get('type') == form_data['type']
        assert data.get('title') == form_data['title']
        assert data.get('contents') == form_data['contents']
        # catalog['status'] 0：正常，-1：删除，1：新增（临时），2：更新（临时）
        for catalog in form_data['catalogs']:
            catalog['status'] = 0
        catalogs_diff = json_diff(form_data['catalogs'], data.get('catalogs', []))
        assert catalogs_diff == [], catalogs_diff


if __name__ == '__main__':
    pytest.main()
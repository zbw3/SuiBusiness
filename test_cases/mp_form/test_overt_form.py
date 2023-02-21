# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time: 2023/2/17 10:17

"""
公开表单相关接口的测试用例
"""
import pytest


def test_v1_overt_form_list(user1):
    """
    /v1/overt_form/list	获取首页公开表单列表
    :param user1:
    :return:s
    """
    response = user1.v1_overt_form_list(method=user1.GET)
    assert response.status_code == 200,response.text
    assert len(response.data.get("data").get("overtFormList")) > 0 ,response.text




def test_in_overt_form(user1):
    """
    验证点击首页的公开表单，进入公开表单详情页是否正常
    :param user1:
    :return:
    """
    res1 = user1.v1_overt_form_list(method=user1.GET)
    overtFormList = res1.data.get("data").get("overtFormList")
    form_ids = [item["formId"] for item in overtFormList]
    for form_id in form_ids:
        res2 = user1.v1_form_profile(form_id=form_id)
        assert res2.status_code == 200 ,res2.text
        assert res2.data.get("data").get("isOvertForm") == True


if __name__ == '__main__':
    pytest.main()
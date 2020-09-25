#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File   : conftest.py
# @Author : mocobk
# @Email  : mailmzb@qq.com
# @Time   : 2020/7/27 14:55
import os

import pytest

from ProductApi.MiniProgramForm.api import FormApi
from ProductApi.MiniProgramForm.form import CreateShoppingForm, CreateActivityForm
from ProductApi.MiniProgramForm.form.poetry_and_future import POETRY_1, POETRY_2

abspath = lambda relpath: os.path.join(os.path.dirname(__file__), relpath)


@pytest.fixture(scope='session')
def user1():
    return FormApi(fuid=FormApi.USER.user1)


@pytest.fixture(scope='session')
def user2():
    return FormApi(fuid=FormApi.USER.user2)


@pytest.fixture(scope='session')
def liu_peng_zhong():
    return FormApi(fuid=FormApi.USER.liu_peng_zhong)


@pytest.fixture(scope='session')
def jiang_duan():
    return FormApi(fuid=FormApi.USER.jiang_duan)


@pytest.fixture(scope='session')
def zhou_ying():
    return FormApi(fuid=FormApi.USER.zhou_ying)


@pytest.fixture(scope='session')
def hu_fei():
    return FormApi(fuid=FormApi.USER.hu_fei)


@pytest.fixture(scope='session')
def default_activity_form():
    return generate_default_form('果霸轰趴')


@pytest.fixture(scope='session')
def default_shopping_form():
    return generate_default_form('果霸商城', is_shopping=True)


def generate_default_form(title=None, is_shopping=False):
    """
    ver: 1.5.0
    update time: 2020/8/4
    :param title:  可以指定表单标题，以区分，也可以使用默认标题 [xx]-测试表单-16:00
    :param is_shopping: 是否是团购接龙，目前不是团购就是活动
    :return: form object
    """
    form = CreateShoppingForm() if is_shopping else CreateActivityForm()
    # 添加标题
    form.set_title(title)
    # 添加文字
    form.add_text(POETRY_1)
    # 添加大图
    form.add_large_img(abspath('./images/2340x1463.jpg'))
    # 添加文字
    form.add_text(POETRY_2)
    # 添加大图
    form.add_large_img(abspath('./images/2560x1600.jpg'))
    # 添加小图
    form.add_small_imgs([
        abspath('./images/600x600.jpg'),
        abspath('./images/730x365.jpg'),
        abspath('./images/757x402.jpg'),
    ])

    if is_shopping:
        form.add_goods('葡萄', '10', abspath('./images/grape.jpg'))
        form.add_goods('西瓜', '2', abspath('./images/watermelon.jpg'))
        form.add_goods('草莓', '8', abspath('./images/strawberry.jpg'))

    # 添加填写项
    form.add_text_question('姓名')
    form.add_number_question('手机号', must=False)
    form.add_number_question('需要数量', must=False)
    form.add_radio_question('你的性别', ['男', '女', '保密'], overt=False, must=False)
    form.add_checkbox_question('你想吃的水果', ['🍎苹果', '🍌香蕉', '🍉西瓜', '🍇葡萄'])
    form.add_text_question('地址', must=False)
    form.add_image_question('请上传你的图片', must=False)
    form.add_text_question('备注', must=False)

    # 设置活动时间(不设置默认为当前时间到30天后)
    form.set_duration_time()
    return form

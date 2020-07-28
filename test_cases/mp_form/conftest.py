#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File   : conftest.py
# @Author : mocobk
# @Email  : mailmzb@qq.com
# @Time   : 2020/7/27 14:55

import pytest
from ProductApi.MiniProgramForm.api import FormApi
from ProductApi.MiniProgramForm.form import CreateShoppingForm, CreateActivityForm
from test_cases.mp_form.poetry_and_future import POETRY_1, POETRY_2
from os.path import abspath


@pytest.fixture(scope='session')
def mocobk():
    return FormApi(fuid=FormApi.USER.mocobk)


@pytest.fixture(scope='session')
def moco():
    return FormApi(fuid=FormApi.USER.moco)


@pytest.fixture(scope='session')
def default_activity_form():
    return generate_default_form('果霸轰趴')


@pytest.fixture(scope='session')
def default_shopping_form():
    return generate_default_form('果霸商城', is_shopping=True)


def generate_default_form(title=None, is_shopping=False):
    """
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
    form.add_text_question('你喜欢什么？', overt=False)
    form.add_number_question('请输入你的手机号', must=False)
    form.add_image_question('请上传你的图片')

    # 设置活动时间(不设置默认为当前时间到30天后)
    form.set_duration_time()
    return form

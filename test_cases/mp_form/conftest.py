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
from ProductApi.MiniProgramForm.form.form import Option
from ProductApi.MiniProgramForm.form.poetry_and_future import POETRY_1, POETRY_2

abspath = lambda relpath: os.path.join(os.path.dirname(__file__), relpath)


@pytest.fixture(scope='session')
def user1():
    return FormApi(fuid=FormApi.USER.user1)


@pytest.fixture(scope='session')
def user2():
    return FormApi(fuid=FormApi.USER.user2)


@pytest.fixture(scope='session')
def user3():
    return FormApi(fuid=FormApi.USER.user3)

@pytest.fixture(scope='session')
def user4():
    return FormApi(fuid=FormApi.USER.user4)

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


@pytest.fixture(scope='function')
def default_activity_form():
    return generate_default_form('果霸轰趴')


@pytest.fixture(scope='function')
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
    # 添加复制区
    form.add_copy_area('前10名加威信，送蓝牙耳机，前20名加威信 送飞科剃须刀，速度速度', 'RfbJerOpM2cv6tY')
    form.add_article_link('公众号链接', 'https://mp.weixin.qq.com/s/yjfVz1iYpkjHVYT089yL0w')
    # form.add_name_list("预设姓名",{"NAME_LIST":{"active":False,"content":""},"NOT_ALLOW_REPEAT":{"active":False},"NAME_LIST_FILL_TYPE":{"active":True,"content":"RADIO_CHOOSE"},"AUTO_FILL":{"active":False}})
    form.add_file('打印机安装教程.docx', '505837', '1', 's90_a120_e150', '1675392261105',
                  'https://qun-oss1.feidee.cn/YjE4/262d6aaeqSl05C18SHH.docx')
    form.add_ws('点击查看', '帮助视频', '如何导出数据',
                   'export/UzFfAgtgekIEAQAAAAAAp5gQSgdaAgAAAAstQy6ubaLX4KHWvLEZgBPEwoNISy9LJI2BzNPgMJqp1efnPIuv7liHjPjwehUD',
                   'sphXQ1FVHVywsWi')
    form.add_applet('wx2eec5fb00157a603', '点此查询', '健康码查询', 'fangkongfuwu/pages/healthCode/step_1/index', '国家政务服务平台')
    form.add_location('广东省深圳市南山区科技南十二路6号', 22.535923004150391, 113.95622253417972)
    form.add_video('11000', '视频.mp4', '1026278', 'https://qun-oss1.feidee.cn/NGRk/d19de08cqSmIF32JwfH_img.jpg',
                   's90_a120_e150', '1675665656347', 'https://qun-oss1.feidee.cn/NGRk/d19de08cqSmIF32JwfH.mp4')
    form.add_audio('599317', '123.m4a', '11217049', 's90_a120_e150', '1675664528982',
                   'https://qun-oss2.feidee.cn/ZjY1/12f71bcaqSm5mu1cK6N.m4a')

    if is_shopping:
        form.add_goods('葡萄', '10', abspath('./images/grape.jpg'))
        form.add_goods('西瓜', '2', abspath('./images/watermelon.jpg'))
        form.add_goods('草莓', '8', abspath('./images/strawberry.jpg'))

    # 添加填写项
    form.add_text_question('姓名')
    form.add_telephone_question('手机号', must=False)
    form.add_number_question('需要数量', must=False)
    form.add_text_question('喜欢的句子', must=False)
    # form.add_radio_question('你的性别', ['男', '女', '保密'], overt=False, must=False)     老版本单选组件，已废弃
    form.add_radio_v2_question('你的性别', [Option('男', False), Option('女', False), Option('保密', False), ], must=False)
    form.add_radio_v2_question('你的国籍', [Option('中国', False), Option('美国', False), Option('其他', True), ], must=False)
    # form.add_checkbox_question('你想吃的水果', ['🍎苹果', '🍌香蕉', '🍉西瓜', '🍇葡萄'])
    form.add_checkbox_v2_question('你想吃的水果', [Option('🍎苹果', False), Option('🍌香蕉', False), Option('🍉西瓜', False)])
    form.add_checkbox_v2_question('喜欢的运动', [Option('篮球', False), Option('羽毛球', False), Option('其他', True)])
    form.add_date_question('出生日期', must=False)
    form.add_text_question('地址', must=False)
    form.add_id_card_question('身份证', must=False)
    form.add_image_question('请上传你的图片', must=False)
    form.add_text_question('备注', must=False)
    form.add_map_location('你所在的位置', must=False)

    # 设置活动时间(不设置默认为当前时间到30天后)
    form.set_duration_time()
    return form

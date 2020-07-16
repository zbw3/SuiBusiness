#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File   : fake.py
# @Author : mocobk
# @Email  : mailmzb@qq.com
# @Time   : 2020/7/15 15:11

from ProductApi.MiniProgramForm.api import FormApi
from ProductApi.MiniProgramForm.form import CreateActivityForm, CreateShoppingForm


class FakeForm:

    def __init__(self, fuid=None):
        """
        :param fuid: 用户群报数 id, 不传则使用配置中默认的
        """
        self.api = FormApi(fuid=fuid)
        self.api.set_logger_level(self.api.INFO)

    def generate_default_form(self, title=None, is_shopping=False):
        """
        :param title:  可以指定表单标题，以区分，也可以使用默认标题 [xx]-测试表单-16:00
        :param is_shopping: 是否是团购接龙，目前不是团购就是活动
        :return:
        """
        form = CreateShoppingForm() if is_shopping else CreateActivityForm()
        # 添加标题
        form.set_title(title)
        # 添加文字
        form.add_text('这是一段文字描述：周末去爬山，记得买水果')
        # 添加大图
        form.add_large_img('https://picsum.photos/500')
        # 添加小图
        form.add_small_imgs(['https://picsum.photos/100'] * 3)

        if is_shopping:
            form.add_goods('葡萄', '10', 'http://mocobk.test.upcdn.net/image/20200715153304815.jpg')
            form.add_goods('西瓜', '2', 'http://mocobk.test.upcdn.net/image/20200715153409003.jpg')

        # 添加填写项
        form.add_text_question('你的喜欢什么？')
        form.add_text_question('你的年龄是？', overt=False)
        form.add_image_question('请上传你的图片')
        form.add_text_question('备注', must=False)

        # 设置活动时间(不设置默认为当前时间到30天后)
        form.set_duration_time()

        return form

    def post_form(self, form):
        res = self.api.v1_form(form.data)
        if res.status_code == 204:
            self.api.logger.info(f'已创建表单: {form.TITLE}')
            self.api.logger.info(form.json)
        else:
            self.api.logger.error('表单创建失败')
            self.api.logger.info(res.text)

    def create_normal_activity_form(self):
        """标准表单"""
        form = self.generate_default_form(title='标准表单', is_shopping=False)
        self.post_form(form)

    def create_no_question_activity_form(self):
        """无填写项表单"""
        form = self.generate_default_form(title='无填写项表单', is_shopping=False)
        form.clear_questions()
        self.post_form(form)

    def create_just_title_activity_form(self):
        """仅含标题表单"""
        form = CreateActivityForm()
        form.set_title('仅含标题表单')
        self.post_form(form)

    def run_create_all(self):
        create_methods = filter(lambda key: key.startswith('create') and callable(getattr(self, key)), dir(self))
        for method in create_methods:
            getattr(self, method)()


if __name__ == '__main__':
    fake = FakeForm(FormApi.USER.mocobk)
    fake.run_create_all()

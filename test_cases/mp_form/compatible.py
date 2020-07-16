# !/user/bin/env python
# _*_ coding: utf-8 _*_
# @File  : compatible.py
# @Author: zy
# @Date  : 2020/7/16
import datetime

from ProductApi.MiniProgramForm.api import FormApi
from ProductApi.MiniProgramForm.form import CreateActivityForm, CreateShoppingForm


class FakeForm:

    def __init__(self, fuid=None):
        """
        :param fuid: 用户群报数 id, 不传则使用配置中默认的
        """
        self.api = FormApi(fuid=fuid)
        self.api.set_logger_level(self.api.INFO)

    '''
       这是没有开启的表单一,有图片、文字、标题的表单
    '''
    def generate_not_open_one_form(self, title=None, is_shopping=False):
        """
        :param title:
        :param is_shopping:
        :return:
        """
        form = CreateShoppingForm() if is_shopping else CreateActivityForm()
        # 添加标题
        form.set_title(title)
        # 添加文字
        form.add_text('这是一个没有开启的表单，有图片、文字、标题的表单')
        form.add_text('表单开启时间在第二天')
        # 添加大图
        form.add_large_img('https://picsum.photos/500')
        # 添加小图
        form.add_small_imgs(['https://picsum.photos/100'] * 5)

        if is_shopping:
            form.add_goods('葡萄', '10', 'http://mocobk.test.upcdn.net/image/20200715153304815.jpg')
            form.add_goods('西瓜', '2', 'http://mocobk.test.upcdn.net/image/20200715153409003.jpg')
            form.add_goods('苹果', '7', 'http://mocobk.test.upcdn.net/image/20200715153409003.jpg')
            form.add_goods('草莓', '20', 'http://mocobk.test.upcdn.net/image/20200715153409003.jpg')
            form.add_goods('橘子', '5', 'http://mocobk.test.upcdn.net/image/20200715153409003.jpg')

        form.set_duration_time(start=(datetime.datetime.now() + datetime.timedelta(days=+1)).strftime("%Y-%m-%d %H:%M"))

        return form

    '''
       这是没有开启的表单二，有图片、文字、标题、填选项的表单
    '''
    def generate_not_open_two_form(self, title=None, is_shopping=False):
        """
            :param title:
            :param is_shopping:
            :return:
            """
        form = CreateShoppingForm() if is_shopping else CreateActivityForm()
        # 添加标题
        form.set_title(title)
        # 添加文字
        form.add_text('这是一个没有开启的表单，有图片、文字、标题、有填选项的表单')
        form.add_text('表单开启时间在第二天')
        # 添加大图
        form.add_large_img('https://picsum.photos/500')
        # 添加小图
        form.add_small_imgs(['https://picsum.photos/100'] * 5)

        if is_shopping:
            form.add_goods('葡萄', '10', 'http://mocobk.test.upcdn.net/image/20200715153304815.jpg')
            form.add_goods('西瓜', '2', 'http://mocobk.test.upcdn.net/image/20200715153409003.jpg')
            form.add_goods('苹果', '7', 'http://mocobk.test.upcdn.net/image/20200715153409003.jpg')
            form.add_goods('草莓', '20', 'http://mocobk.test.upcdn.net/image/20200715153409003.jpg')
            form.add_goods('橘子', '5', 'http://mocobk.test.upcdn.net/image/20200715153409003.jpg')

        # 添加填写项
        form.add_text_question('姓名')
        form.add_text_question('年龄', overt=False)
        form.add_image_question('请上传你的图片', must=False)

        form.set_duration_time(
            start=(datetime.datetime.now() + datetime.timedelta(days=+1)).strftime("%Y-%m-%d %H:%M"))

        return form

    '''
        这是进行中的表单一，只有标题、图片、文字的表单
    '''
    def generate_not_options_form(self, title=None, is_shopping=False):
        """
        :param title:
        :param is_shopping:
        :return:
        """
        form = CreateShoppingForm() if is_shopping else CreateActivityForm()
        # 添加标题
        form.set_title(title)
        # 添加文字
        form.add_text('这是进行中的表单一，只有标题的表单')
        # 添加大图
        form.add_large_img('https://picsum.photos/500')
        # 添加小图
        form.add_small_imgs(['https://picsum.photos/100'] * 5)

        if is_shopping:
            form.add_goods('葡萄', '10', 'http://mocobk.test.upcdn.net/image/20200715153304815.jpg')
            form.add_goods('西瓜', '2', 'http://mocobk.test.upcdn.net/image/20200715153409003.jpg')
            form.add_goods('苹果', '7', 'http://mocobk.test.upcdn.net/image/20200715153409003.jpg')
            form.add_goods('草莓', '20', 'http://mocobk.test.upcdn.net/image/20200715153409003.jpg')
            form.add_goods('橘子', '5', 'http://mocobk.test.upcdn.net/image/20200715153409003.jpg')

        form.set_duration_time()

        return form

    '''
        这是进行中的表单二，有标题、图片、文字、填选项的表单
    '''
    def generate_have_options_form(self, title=None, is_shopping=False):
        """
        :param title:
        :param is_shopping:
        :return:
        """
        form = CreateShoppingForm() if is_shopping else CreateActivityForm()
        # 添加标题
        form.set_title(title)
        # 添加文字
        form.add_text('这是进行中的表单二，有标题、图片、文字、填选项的表单')
        # 添加大图
        form.add_large_img('https://picsum.photos/500')
        # 添加小图
        form.add_small_imgs(['https://picsum.photos/100'] * 5)

        if is_shopping:
            form.add_goods('葡萄', '10', 'http://mocobk.test.upcdn.net/image/20200715153304815.jpg')
            form.add_goods('西瓜', '2', 'http://mocobk.test.upcdn.net/image/20200715153409003.jpg')
            form.add_goods('苹果', '7', 'http://mocobk.test.upcdn.net/image/20200715153409003.jpg')
            form.add_goods('草莓', '20', 'http://mocobk.test.upcdn.net/image/20200715153409003.jpg')
            form.add_goods('橘子', '5', 'http://mocobk.test.upcdn.net/image/20200715153409003.jpg')

        # 添加填写项
        form.add_text_question('姓名')
        form.add_text_question('年龄', overt=False)
        form.add_image_question('请上传你的图片', must=False)

        form.set_duration_time()

        return form

    '''
        这是结束的表单一，只有标题、图片、文字的表单
    '''
    def generate_stop_one_form(self, title=None, is_shopping=False):
        """
        :param title:
        :param is_shopping:
        :return:
        """
        form = CreateShoppingForm() if is_shopping else CreateActivityForm()
        # 添加标题
        form.set_title(title)
        # 添加文字
        form.add_text('这是停止的表单一，只有标题、图片、文字的表单')
        # 添加大图
        form.add_large_img('https://picsum.photos/500')
        # 添加小图
        form.add_small_imgs(['https://picsum.photos/100'] * 5)

        if is_shopping:
            form.add_goods('葡萄', '10', 'http://mocobk.test.upcdn.net/image/20200715153304815.jpg')
            form.add_goods('西瓜', '2', 'http://mocobk.test.upcdn.net/image/20200715153409003.jpg')
            form.add_goods('苹果', '7', 'http://mocobk.test.upcdn.net/image/20200715153409003.jpg')
            form.add_goods('草莓', '20', 'http://mocobk.test.upcdn.net/image/20200715153409003.jpg')
            form.add_goods('橘子', '5', 'http://mocobk.test.upcdn.net/image/20200715153409003.jpg')

        form.set_duration_time(
            end=(datetime.datetime.now() + datetime.timedelta(minutes=+1)).strftime("%Y-%m-%d %H:%M"))

        return form

    '''
        这是结束的表单二，有标题、图片、文字、填选项的表单
    '''
    def generate_stop_two_form(self, title=None, is_shopping=False):
        """
        :param title:
        :param is_shopping:
        :return:
        """
        form = CreateShoppingForm() if is_shopping else CreateActivityForm()
        # 添加标题
        form.set_title(title)
        # 添加文字
        form.add_text('这是停止的表单二，有标题、图片、文字、填选项的表单')
        # 添加大图
        form.add_large_img('https://picsum.photos/500')
        # 添加小图
        form.add_small_imgs(['https://picsum.photos/100'] * 5)

        if is_shopping:
            form.add_goods('葡萄', '10', 'http://mocobk.test.upcdn.net/image/20200715153304815.jpg')
            form.add_goods('西瓜', '2', 'http://mocobk.test.upcdn.net/image/20200715153409003.jpg')
            form.add_goods('苹果', '7', 'http://mocobk.test.upcdn.net/image/20200715153409003.jpg')
            form.add_goods('草莓', '20', 'http://mocobk.test.upcdn.net/image/20200715153409003.jpg')
            form.add_goods('橘子', '5', 'http://mocobk.test.upcdn.net/image/20200715153409003.jpg')

        # 添加填写项
        form.add_text_question('姓名')
        form.add_text_question('年龄', overt=False)
        form.add_image_question('请上传你的图片', must=False)

        form.set_duration_time(
            end=(datetime.datetime.now() + datetime.timedelta(minutes=+1)).strftime("%Y-%m-%d %H:%M"))

        return form

    def post_form(self, form):
        res = self.api.v1_form(form.data)
        if res.status_code == 204:
            self.api.logger.info(f'已创建表单: {form.TITLE}')
            self.api.logger.info(form.json)
        else:
            self.api.logger.error('表单创建失败')
            self.api.logger.info(res.text)

    def create_not_open_one_form(self):
        """未开启的表单一，没有填选项"""
        form = self.generate_not_open_one_form(title='未开启的表单一，没有填选项', is_shopping=True)
        self.post_form(form)

    def create_not_open_two_form(self):
        """未开启的表单二，有填选项"""
        form = self.generate_not_open_two_form(title='未开启的表单二，有填选项', is_shopping=True)
        form.clear_questions()
        self.post_form(form)

    def create_just_title_activity_form(self):
        """仅含标题表单"""
        form = CreateActivityForm()
        form.set_title('仅含标题表单')
        self.post_form(form)

    def create_not_options_form(self):
        """进行中的表单，没有填选项"""
        form = self.generate_not_options_form(title='进行中的表单，没有填选项', is_shopping=True)
        form.clear_questions()
        self.post_form(form)

    def create_have_options_form(self):
        """进行中的表单，有填选项"""
        form = self.generate_not_options_form(title='进行中的表单，有填选项', is_shopping=True)
        form.clear_questions()
        self.post_form(form)

    def create_stop_one_form(self):
        """结束中的表单，没有填选项"""
        form = self.generate_not_options_form(title='结束中的表单，没有填选项', is_shopping=True)
        form.clear_questions()
        self.post_form(form)

    def create_stop_two_form(self):
        """结束中的表单，有填选项"""
        form = self.generate_not_options_form(title='结束中的表单，有填选项', is_shopping=False)
        form.clear_questions()
        self.post_form(form)

    def run_create_all(self):
        create_methods = filter(lambda key: key.startswith('create') and callable(getattr(self, key)), dir(self))
        for method in create_methods:
            getattr(self, method)()


if __name__ == '__main__':
    fake = FakeForm(FormApi.USER.zhou_ying)
    fake.run_create_all()

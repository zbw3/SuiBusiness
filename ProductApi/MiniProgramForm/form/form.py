#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File   : form.py
# @Author : mocobk
# @Email  : mailmzb@qq.com
# @Time   : 2020/7/14 13:57
import json
import os
import time
from random import randint
from datetime import datetime, timedelta
from typing import List, Union

from ProductApi.MiniProgramForm.form.enum import ContentType, RoleType, CatalogType, FormType
from ProductApi.MiniProgramForm.api import FormApi
from ProductApi.MiniProgramForm.form.utils import get_img_url, RandomImageUrl


class Content:
    """表单 文字 大图 小图 项内容"""

    def __init__(self, type_: ContentType = ContentType.WORD, content: Union[str, list] = '表单文字描述部分'):
        if type_ == ContentType.THUMBNAIL and isinstance(content, str):
            raise ValueError('小图类型 content 值必须为列表')
        self.value = {'type': type_.value, 'content': content}


class FormCatalog:
    """商品项的或填写项的内容"""

    def __init__(
            self,
            content: str,
            role: RoleType = RoleType.TITLE,
            type_: ContentType = ContentType.WORD,
            title: str = "",
            status: int = 1
    ):
        self.value = {
            "title": title,
            "content": content,
            "role": role.value,
            "type": type_.value,
            "status": status
        }


class Catalog:

    def __init__(
            self,
            type_: ContentType = ContentType.WORD,
            catalog_type: CatalogType = CatalogType.QUESTION,
            form_catalogs: List[FormCatalog] = None,
            must: bool = True,
            overt: bool = True,
            used: bool = False,
            status: int = 1
    ):
        self.type_ = type_
        self.must = must
        self.overt = overt
        self.catalog_type = catalog_type
        self.status = status
        self.used = used
        self.form_catalogs = form_catalogs or [FormCatalog('填写项标题')]

    @property
    def value(self):
        if self.catalog_type == CatalogType.QUESTION and len(self.form_catalogs) < 1:
            raise ValueError('填写项 form_catalogs 长度必须大于 1')
        if self.catalog_type == CatalogType.GOODS and len(self.form_catalogs) != 3:
            raise ValueError('商品项 form_catalogs 长度必须为 3')
        diff = {
            CatalogType.QUESTION: {"must": self.must, "overt": self.overt},
            CatalogType.GOODS: {'used': self.used}
        }
        return {
            "formCatalogs": [item.value for item in self.form_catalogs],
            "type": self.type_.value,
            "catalogType": self.catalog_type.value,
            "status": self.status,
            **diff[self.catalog_type]
        }

    def add_form_catalog(self, form_catalog: FormCatalog):
        self.form_catalogs.append(form_catalog)


class Form:
    TYPE: FormType = None

    FormType = FormType
    ContentType = ContentType
    RoleType = RoleType
    CatalogType = CatalogType
    Content = Content
    Catalog = Catalog
    FormCatalog = FormCatalog
    RandomImage = RandomImageUrl()

    def __init__(self, _type: FormType = None):
        if _type:
            self.TYPE = _type

        self.COVER = 'https://resources.sui.com/fed/wechat/statistics-tools/templates/bg_banner.png?v1'
        self.TITLE = None
        self.CONTENTS = []
        self.CATALOGS = []
        self.CONFIG = {}
        self.form_api = FormApi()

        self.now = datetime.now()
        self.now_offset = lambda days=0, hours=0, seconds=0: (
                self.now + timedelta(days, hours=hours, seconds=seconds)).strftime('%Y-%m-%d %T')
        self.CONFIG = {
            'actBeginTime': self.now.strftime('%Y-%m-%d %T'),
            'actEndTime': (self.now + timedelta(days=30)).strftime('%Y-%m-%d %T')
        }

    @property
    def data(self):
        if self.TYPE == FormType.SHOPPING:
            goods_catalog = filter(lambda catalog: catalog['catalogType'] == CatalogType.GOODS.value, self.CATALOGS)
            if len(list(goods_catalog)) < 1:
                raise ValueError('团购表单，至少需要添加一个商品')

        return {
            # 有填写项 TYPE = ACTIVITY_V2
            "type": self.TYPE.name if not self.is_activity_v2() else FormType.ACTIVITY_V2.name,
            "cover": self.COVER,
            "title": self.TITLE or f'[{self.TYPE.value}]-测试表单-{time.strftime("%T")}',
            "contents": self.CONTENTS,
            "catalogs": self.CATALOGS,
            "config": self.CONFIG
        }

    @property
    def json(self):
        return json.dumps(self.data, ensure_ascii=False)

    def set_title(self, title):
        if title:
            self.TITLE = f'[{self.TYPE.value}]-{title}-{time.strftime("%T")}'

    def set_cover(self, img_url):
        self.COVER = img_url

    def add_text(self, text: str):
        self._add_content(
            Content(ContentType.WORD, text)
        )

    def add_large_img(self, image: str):
        self._add_content(
            Content(ContentType.IMAGE, get_img_url(image))
        )

    def add_small_imgs(self, images: list):
        self._add_content(
            Content(ContentType.THUMBNAIL, [get_img_url(image) for image in images])
        )

    def add_text_question(self, title, must=True, overt=True):
        self._add_catalog(
            Catalog(
                must=must,
                overt=overt,
                form_catalogs=[FormCatalog(title)]
            )
        )

    def add_image_question(self, title, must=True, overt=True):
        self._add_catalog(
            Catalog(
                type_=ContentType.IMAGE,
                must=must,
                overt=overt,
                form_catalogs=[FormCatalog(title)]
            )
        )

    def add_number_question(self, title, must=True, overt=True):
        self._add_catalog(
            Catalog(
                type_=ContentType.NUMBER_FLOAT,
                must=must,
                overt=overt,
                form_catalogs=[FormCatalog(title)]
            )
        )

    def add_radio_question(self, title, options: List[str], must=True, overt=True):
        if len(options) < 2:
            raise Exception('单选的选项不能少于 2 条')
        self._add_catalog(
            Catalog(
                type_=ContentType.RADIO,
                must=must,
                overt=overt,
                form_catalogs=[FormCatalog(title)] + [FormCatalog(option, RoleType.OPTION) for option in options]
            )
        )

    def add_checkbox_question(self, title, options: List[str], must=True, overt=True):
        if len(options) < 2:
            raise Exception('多选的选项不能少于 2 条')
        self._add_catalog(
            Catalog(
                type_=ContentType.CHECKBOX,
                must=must,
                overt=overt,
                form_catalogs=[FormCatalog(title)] + [FormCatalog(option, RoleType.OPTION) for option in options]
            )
        )

    def set_duration_time(self, start=None, end=None):
        self.CONFIG = {
            'actBeginTime': start or self.now.strftime('%Y-%m-%d %T'),
            'actEndTime': end or (self.now + timedelta(days=30)).strftime('%Y-%m-%d %T')
        }

    def clear_contents(self):
        """清空表单内容项 文字 大图 小图"""
        self.CONTENTS = []

    def clear_goods(self):
        """清空商品项"""
        self.CATALOGS = [catalog for catalog in self.CATALOGS if catalog['catalogType'] != CatalogType.GOODS.value]

    def clear_questions(self):
        """"清空填写项"""
        self.CATALOGS = [catalog for catalog in self.CATALOGS if catalog['catalogType'] != CatalogType.QUESTION.value]

    def is_activity_v2(self):
        if self.TYPE == FormType.ACTIVITY:
            for catalog in self.CATALOGS:
                if catalog['catalogType'] == CatalogType.QUESTION.value:
                    return True
        return False

    def _add_content(self, content: Content):
        self.CONTENTS.append(content.value)

    def _add_catalog(self, catalog: Catalog):
        self.CATALOGS.append(catalog.value)


class CreateActivityForm(Form):
    TYPE = FormType.ACTIVITY


class CreateShoppingForm(Form):
    TYPE = FormType.SHOPPING

    def add_goods(self, title, price='', image=''):
        if image != '':
            image = get_img_url(image)
        self._add_catalog(
            Catalog(
                type_=ContentType.NUMBER,
                catalog_type=CatalogType.GOODS,
                form_catalogs=[
                    FormCatalog(title, RoleType.TITLE, ContentType.WORD, title='商品名称：'),
                    FormCatalog(price, RoleType.PRICE, ContentType.NUMBER, title='价格(¥)：'),
                    FormCatalog(image, RoleType.IMAGE, ContentType.IMAGE, title='商品图片：'),
                ]
            )
        )


if __name__ == '__main__':
    # form = CreateActivityForm()
    # # 添加标题
    # form.add_title('活动表单测试')
    # # 添加文字
    # form.add_text('这是一个文字描述')
    # # 添加大图
    # form.add_large_img('https://picsum.photos/200')
    # # 添加小图
    # form.add_small_imgs(['https://picsum.photos/200'] * 3)
    #
    # # 添加填写项
    # form.add_text_question('你的姓名是？')
    # form.add_text_question('你的年龄是？', must=False)
    #
    # # 设置活动时间(不设置默认为当前时间到30天后)
    # form.set_duration_time(start='2020-07-15 11:50:00', end='2020-07-20 11:50:00')
    #
    # print(form.json)
    #
    # api = FormApi(fuid='1026957780256297009', print_results=True)
    # api.v1_form(form.data)

    """
    创建多图
    """
    form = CreateShoppingForm()
    # 添加标题
    form.set_title('多图表单(大图10 + 小图 90 + 商品 20)')
    # 添加文字
    form.add_text('这是一个文字描述')
    # 添加大图
    for i in range(10):
        form.add_large_img('https://picsum.photos/1000')

    form.add_small_imgs(['https://picsum.photos/800'] * 90)

    # 添加商品
    for i in range(1, 21):
        form.add_goods(str(i), price='2.5', image='https://picsum.photos/500')
    # form.add_goods('香蕉', price='5', image='https://picsum.photos/50')

    # 添加填写项
    form.add_text_question('你选的水果是？')

    print(form.json)

    api = form.form_api
    api.v1_form(form.data)

    """
    创建多商品问题
    """
    # form = CreateShoppingForm()
    # # 添加标题
    # form.set_title('多商品（25）无图片测试')
    # # 添加文字
    # form.add_text('这是一个文字描述')
    #
    # for i in range(1, 26):
    #     form.add_goods(str(i) + '我的商品铺子里的物品我的商品铺子里的物品我的商品铺子里的物品我的商品铺子里', price='2.5', image='')
    # # form.add_goods('香蕉', price='5', image='https://picsum.photos/50')
    #
    # # 添加填写项
    # form.add_text_question('你选的水果是？')
    #
    # print(form.json)
    #
    # api = form.form_api
    # api.v1_form(form.data)

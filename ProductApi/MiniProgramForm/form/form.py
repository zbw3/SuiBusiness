#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File   : form.py
# @Author : mocobk
# @Email  : mailmzb@qq.com
# @Time   : 2020/7/14 13:57
import json
from datetime import datetime, timedelta
from enum import Enum
from typing import List, Union

from ProductApi.MiniProgramForm.api import FormApi


class ContentType(Enum):
    WORD = 'WORD'
    NUMBER = 'NUMBER'  # 添加商品用到
    IMAGE = 'IMAGE'
    THUMBNAIL = 'THUMBNAIL'


class RoleType(Enum):
    TITLE = 'TITLE'
    IMAGE = 'IMAGE'  # 添加商品用到
    PRICE = 'PRICE'  # 添加商品用到


class CatalogType(Enum):
    QUESTION = 'QUESTION'
    GOODS = 'GOODS'


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
            title: str = ""
    ):
        self.value = {
            "title": title,
            "content": content,
            "role": role.value,
            "type": type_.value
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
        if self.catalog_type == CatalogType.QUESTION and len(self.form_catalogs) != 1:
            raise ValueError('填写项 form_catalogs 长度必须为 1')
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
    TYPE = None

    ContentType = ContentType
    RoleType = RoleType
    CatalogType = CatalogType
    Content = Content
    Catalog = Catalog
    FormCatalog = FormCatalog

    def __init__(self):
        self.COVER = 'https://resources.sui.com/fed/wechat/statistics-tools/templates/bg_banner.png?v1'
        self.TITLE = '未填写标题'
        self.CONTENTS = []
        self.CATALOGS = []
        self.CONFIG = {}

        self.now = datetime.now()
        self.CONFIG = {
            'actBeginTime': self.now.strftime('%Y-%m-%d %T'),
            'actEndTime': (self.now + timedelta(days=30)).strftime('%Y-%m-%d %T')
        }

    @property
    def data(self):
        if self.TYPE == 'SHOPPING':
            goods_catalog = filter(lambda catalog: catalog['catalogType'] == CatalogType.GOODS.value, self.CATALOGS)
            if len(list(goods_catalog)) < 1:
                raise ValueError('团购表单，至少需要添加一个商品')

        return {
            "type": self.TYPE,
            "cover": self.COVER,
            "title": self.TITLE,
            "contents": self.CONTENTS,
            "catalogs": self.CATALOGS,
            "config": self.CONFIG
        }

    @property
    def json(self):
        return json.dumps(self.data, ensure_ascii=False)

    def add_title(self, title):
        self.TITLE = title

    def add_cover(self, img_url):
        self.COVER = img_url

    def add_text(self, text: str):
        self._add_content(
            Content(ContentType.WORD, text)
        )

    def add_large_img(self, image: str):
        self._add_content(
            Content(ContentType.IMAGE, self._get_img_url(image))
        )

    def add_small_imgs(self, images: list):
        self._add_content(
            Content(ContentType.THUMBNAIL, [self._get_img_url(image) for image in images])
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

    def set_duration_time(self, start=None, end=None):
        self.CONFIG = {
            'actBeginTime': start or self.now.strftime('%Y-%m-%d %T'),
            'actEndTime': end or (self.now + timedelta(days=30)).strftime('%Y-%m-%d %T')
        }

    def _add_content(self, content: Content):
        self.CONTENTS.append(content.value)

    def _add_catalog(self, catalog: Catalog):
        self.CATALOGS.append(catalog.value)

    def _get_img_url(self, image):
        api = FormApi()
        api.set_logger_level(api.INFO)
        api.logger.info('图片上传中...')
        res = api.v1_image(image)
        if res.status_code == 200:
            return res.data.get('data')
        else:
            raise Exception(f'图片上传失败: {res.text}')


class CreateActivityForm(Form):
    TYPE = 'ACTIVITY'


class CreateShoppingForm(Form):
    TYPE = 'SHOPPING'

    def add_goods(self, title, price='', image=''):
        if image != '':
            image = self._get_img_url(image)
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

    form = CreateShoppingForm()
    # 添加标题
    form.add_title('团购表单测试')
    # 添加文字
    form.add_text('这是一个文字描述')
    # 添加大图
    form.add_large_img('https://picsum.photos/200')

    # 添加商品
    form.add_goods('苹果', price='2.5', image='https://picsum.photos/50')
    form.add_goods('香蕉', price='5', image='https://picsum.photos/50')

    # 添加填写项
    form.add_text_question('你选的水果是？')

    print(form.json)

    api = FormApi()
    api.v1_form(form.data)

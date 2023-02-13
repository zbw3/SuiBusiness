#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File   : form.py
# @Author : mocobk
# @Email  : mailmzb@qq.com
# @Time   : 2020/7/14 13:57
import json
import time
from datetime import datetime, timedelta
from typing import List, Union

from ProductApi.MiniProgramForm.api import FormApi
from ProductApi.MiniProgramForm.form.enum1 import ContentType, RoleType, CatalogType, FormType
from ProductApi.MiniProgramForm.form.utils import get_img_url, RandomImageUrl


class Content:
    """表单 文字 大图 小图 项内容"""

    def __init__(self, type_: ContentType = ContentType.WORD, content: Union[str, list, dict] = '表单文字描述部分'):
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
            status: int = 1,
            **kwargs
    ):
        self.value = {
            "title": title,
            "content": content,
            "role": role.value,
            "type": type_.value,
            "status": status,
            **kwargs
        }


class CopyContent:
    """一键复制区"""

    def __init__(
            self,
            guide: str = "",
            content: str = "RfbJerOpM2cv6tY"

    ):
        self.value = {
            "guide": guide,
            "content": content
        }

class File:
    """正文文件"""
    def __init__(
            self,
            fileName: str = '',
            fileSize: str= "",
            status: str = "",
            tag: str = "",
            uploadTime: str = "",
            url: str = ""
    ):
        self.value = {
            "fileName": fileName,
            "fileSize": fileSize,
            "status": status,
            "tag": tag,
            "uploadTime": uploadTime,
            "url": url
        }


class WS_LINK:
    """正文视频号"""
    def __init__(
            self,
            button_name: str = "",
            main_title: str = "",
            vice_title: str = "",
            vid: str = "",
            ws_id: str = ""):
        self.value = {
            "buttonName": button_name,
            "mainTitle": main_title,
            "viceTitle": vice_title,
            "vid": vid,
            "wsId": ws_id
        }

class APPLET:
    """正文小程序"""
    def __init__(
            self,
            appid: str = "",
            btn_name: str = "",
            main_title: str = "",
            path: str = "",
            vice_title: str = ""
    ):
        self.value = {
            "appId": appid,
            "buttonName": btn_name,
            "mainTitle": main_title,
            "path": path,
            "viceTitle": vice_title

        }


class LOCATION:
    """正文定位"""
    def __init__(
            self,
            address: str = "",
            lat: int = "",
            lon: int = ""
    ):
        self.value = {
            "address": address,
            "latitude": lat,
            "longitude": lon
        }

class VIDEO:
    """正文视频"""
    def __init__(
            self,
            duration: str = "",
            name: str = "",
            size: str = "",
            frame_url: str = "",
            tag: str = "",
            time: str = "",
            url: str = ""
    ):
        self.value = {
            "durationMs": duration,
            "fileName": name,
            "fileSize": size,
            "frameUrl": frame_url,
            "tag": tag,
            "uploadTime": time,
            "url": url

        }

class AUDIO:
    """正文视频"""
    def __init__(
            self,
            duration: str = "",
            name: str = "",
            size: str = "",
            tag: str = "",
            time: str = "",
            url: str = ""
    ):
        self.value = {
            "durationMs": duration,
            "fileName": name,
            "fileSize": size,
            "tag": tag,
            "uploadTime": time,
            "url": url

        }


class LinkContent:
    ''' 公众号链接 '''

    def __init__(
            self,
            title: str = "公众号文章",
            link: str = ""
    ):
        self.value = {
            "title": title,
            "link": link
        }


class Option:
    """
    RADIO_V2 CHECKBOX_V2 的 option 需要指定是否可自定义
    """

    def __init__(self, title: str, custom: bool):
        self.title = title
        self.custom = custom


class Catalog:

    def __init__(
            self,
            type_: ContentType = ContentType.WORD,
            catalog_type: CatalogType = CatalogType.QUESTION,
            form_catalogs: List[FormCatalog] = None,
            must: bool = True,
            overt: bool = True,
            used: bool = False,
            status: int = 1,
            config={"NAME_LIST":{"active":False,"content":""},"NOT_ALLOW_REPEAT":{"active":False},"NAME_LIST_FILL_TYPE":{"active":True,"content":"RADIO_CHOOSE"},"AUTO_FILL":{"active":False}}
    ):
        self.type_ = type_
        self.must = must
        self.overt = overt
        self.catalog_type = catalog_type
        self.status = status
        self.used = used
        self.form_catalogs = form_catalogs or [FormCatalog('填写项标题')]
        # {"NAME_LIST": {"active": True, "content": self.get_nlid()}}
        self.config = config

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
        self.form_api = FormApi()

        self.now = datetime.now()
        self.now_offset = lambda days=0, hours=0, seconds=0: (
                self.now + timedelta(days, hours=hours, seconds=seconds)).strftime('%Y-%m-%d %T')
        self.CONFIG = {
            'actBeginTime': self.now.strftime('%Y-%m-%d %T'),
            'actEndTime': (self.now + timedelta(days=30)).strftime('%Y-%m-%d %T'),
            'limit': -1,
            "perLimit": -1,
            'allowModify': True,
            'relay': 0,
            'formDataPermission': 1,
            'cycle': {
                'frequency': 127,
                'effectiveTime': [
                    {
                        'startTime': 0,
                        'endTime': 2359
                    }
                ]
            },
            "submitBtnName": {
                "type": "PREDEFINED",
                "content": "FILL_IN"
            }
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

    def add_copy_area(self, copy_guide, copy_content):
        self._add_content(
            Content(ContentType.COPY_AREA, content=CopyContent(copy_guide, copy_content).value)
        )

    def add_file(self, name, size, status, tag, time, url):
        self._add_content(
            Content(ContentType.FILE, content=File(name, size, status, tag, time, url).value)
        )

    def add_ws(self, btn_name, main_title, vice_title, vid, ws_id):
        self._add_content(
            Content(ContentType.WS_LINK, content=WS_LINK(btn_name, main_title, vice_title, vid, ws_id).value)
        )

    def add_video(self, duration, name, size, frame_url, tag, time, url):
        self._add_content(
            Content(ContentType.VIDEO, content=VIDEO(duration, name, size, frame_url, tag, time, url).value)
        )

    def add_audio(self, duration, name, size, tag, time, url):
        self._add_content(
            Content(ContentType.AUDIO, content=AUDIO(duration, name, size, tag, time, url).value)
        )

    def add_applet(self, appid, btn_name, main_title, path, vice_title):
        self._add_content(
            Content(ContentType.APPLET, content=APPLET(appid, btn_name, main_title, path, vice_title).value)
        )

    def add_location(self, address, lat, lon):
        self._add_content(
            Content(ContentType.LOCATION, content=LOCATION(address, lat, lon).value)
        )

    def add_article_link(self, article_title, article_link):
        self._add_content(
            Content(ContentType.MP_LINK, content=LinkContent(article_title, article_link).value)
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

    def add_telephone_question(self, title, must=True, overt=True):
        self._add_catalog(
            Catalog(
                type_=ContentType.TELEPHONE,
                must=must,
                overt=overt,
                form_catalogs=[FormCatalog(title)]
            )
        )

    def add_id_card_question(self, title, must=True, overt=True):
        self._add_catalog(
            Catalog(
                type_=ContentType.ID_CARD,
                must=must,
                overt=overt,
                form_catalogs=[FormCatalog(title)]
            )
        )

    def add_date_question(self, title, must=True, overt=True):
        self._add_catalog(
            Catalog(
                type_=ContentType.DATE,
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

    def add_radio_v2_question(self, title, options: List[Option], must=True, overt=True):
        """选项中增加自定义的项"""
        if len(options) < 2:
            raise Exception('单选的选项不能少于 2 条')
        self._add_catalog(
            Catalog(
                type_=ContentType.RADIO_V2,
                must=must,
                overt=overt,
                form_catalogs=[FormCatalog(title)] + [FormCatalog(option.title, RoleType.OPTION, custom=option.custom)
                                                      for option in options]
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

    def add_checkbox_v2_question(self, title, options: List[Option], must=True, overt=True):
        if len(options) < 2:
            raise Exception('多选的选项不能少于 2 条')
        self._add_catalog(
            Catalog(
                type_=ContentType.CHECKBOX_V2,
                must=must,
                overt=overt,
                form_catalogs=[FormCatalog(title)] + [FormCatalog(option.title, RoleType.OPTION, custom=option.custom)
                                                      for option in options]
            )
        )

    def add_map_location(self, title, must=False, overt=True):
        self._add_catalog(
            Catalog(
                type_=ContentType.LOCATION,
                must=must,
                overt=overt,
                form_catalogs=[FormCatalog(title)]
            )
        )

    """添加预设名单"""
    def add_name_list(self, title,config, must=False, overt=True):
        self._add_catalog(
            Catalog(
                type_=ContentType.WORD,
                must=must,
                overt=overt,
                config=config,
                form_catalogs=[FormCatalog(title)]
            )
        )
    """获取预设名单id"""
    def get_nlid(self, user=FormApi.USER.user1):
        # response = FormApi(user).v1_name_list(value=[{"name": "张三"}, {"name": "李四"}])
        response = FormApi(user).v1_form_name_list_template({"templateName":"名单模板测试","originData":"1\n2\n3\n4","value":[{"name":"1"},{"name":"2"},{"name":"3"},{"name":"4"}]})
        # print(response.data.get('data')["nlid"])
        return response.data.get('data')["nlid"]



    def set_duration_time(self, start=None, end=None):
        self.CONFIG['actBeginTime'] = start or self.now.strftime('%Y-%m-%d %T')
        self.CONFIG['actEndTime'] = end or (self.now + timedelta(days=30)).strftime('%Y-%m-%d %T')

    def set_limit(self, limit: int):
        self.CONFIG['limit'] = limit

    def set_per_limit(self, per_limit: int):
        self.CONFIG['perLimit'] = per_limit

    def set_cycle(self, frequency, start: int, end: int):
        self.CONFIG['cycle']['frequency'] = frequency
        self.CONFIG['cycle']['effectiveTime'][0]['startTime'] = start
        self.CONFIG['cycle']['effectiveTime'][0]['endTime'] = end

    def set_allow_modify(self, allow_modify: bool):
        self.CONFIG['allowModify'] = allow_modify

    def set_relay(self, relay: int):
        self.CONFIG['relay'] = relay

    def set_form_data_permission(self, permission: int):
        """
        :param permission: 1:所有人可见；2:管理员可见
        :return:
        """
        self.CONFIG['formDataPermission'] = permission

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
    form = CreateActivityForm()
    # # 添加标题
    form.set_title('活动表单测试')
    # 添加文字
    form.add_text('这是一个文字描述')
    form.add_file('打印机安装教程.docx', '505837','1','s90_a120_e150','1675392261105','https://qun-oss1.feidee.cn/YjE4/262d6aaeqSl05C18SHH.docx')
    form.add_video('点击查看', '帮助视频', '如何导出数据', 'export/UzFfAgtgekIEAQAAAAAAp5gQSgdaAgAAAAstQy6ubaLX4KHWvLEZgBPEwoNISy9LJI2BzNPgMJqp1efnPIuv7liHjPjwehUD','sphXQ1FVHVywsWi')
    form.add_applet('wx2eec5fb00157a603', '点此查询', '健康码查询', 'fangkongfuwu/pages/healthCode/step_1/index', '国家政务服务平台')
    form.add_location('广东省深圳市南山区科技南十二路6号', 'l22.535923004150391', '113.95622253417972')
    # form.add_name_list('22')
    # form.get_nlid()
    # form.add_name_list("名单")
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
    # form = CreateShoppingForm()
    # # 添加标题
    # form.set_title('多图表单(大图10 + 小图 90 + 商品 20)')
    # # 添加文字
    # form.add_text('这是一个文字描述')
    # # 添加大图
    # for i in range(10):
    #     form.add_large_img('https://picsum.photos/1000')
    #
    # form.add_small_imgs(['https://picsum.photos/800'] * 90)
    #
    # # 添加商品
    # for i in range(1, 21):
    #     form.add_goods(str(i), price='2.5', image='https://picsum.photos/500')
    # # form.add_goods('香蕉', price='5', image='https://picsum.photos/50')
    #
    # # 添加填写项
    # form.add_text_question('你选的水果是？')
    #
    # print(form.json)
    #
    # api = form.form_api
    # api.v1_form(form.data)

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

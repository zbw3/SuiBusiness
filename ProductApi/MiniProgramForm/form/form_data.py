#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File   : form_data.py
# @Author : mocobk
# @Email  : mailmzb@qq.com
# @Time   : 2020/7/29 17:28
import random

from ProductApi.MiniProgramForm.api import FormApi
from ProductApi.MiniProgramForm.form.enum import CatalogType, RoleType, CatalogStatus
from ProductApi.MiniProgramForm.form.utils import RandomImageUrl, CustomProvider
from faker import Faker


class QuestionsData:
    def __init__(self):
        self.WORD = []
        self.IMAGE = []
        self.NUMBER_FLOAT = []
        self.RADIO = []
        self.CHECKBOX = []
        self.RADIO_V2 = []
        self.CHECKBOX_V2 = []
        self.TELEPHONE = []
        self.ID_CARD = []
        self.DATE = []
        self.LOCATION = []


class CatalogsData:
    def __init__(self):
        self.GOODS = []
        self.QUESTION = QuestionsData()
        self.BUYER_REMARKS = None
        self.SELLER_REMARKS = None


class PostFormData:
    RandomImage = RandomImageUrl()

    def __init__(self, form_api: FormApi, form_id):
        self.form_detail_data = form_api.v1_form_form_id(form_id).data['data']
        self.faker = Faker('zh_CN')
        self.faker.add_provider(CustomProvider)
        self.info = {
            '姓名': self.faker.name,
            '手机号': self.faker.phone_number,
            '地址': self.faker.address,
            '公司': self.faker.company,
            '备注': self.faker.word_with_emoji,
        }

    @property
    def version(self):
        return self.form_detail_data['version']

    @property
    def _catalogs(self) -> CatalogsData:
        catalogs = CatalogsData()
        for item in self.form_detail_data['catalogs']:
            if CatalogStatus(item['status']) == CatalogStatus.DELETED:  # 已删除
                continue

            catalog_type = item.get('catalogType')

            if CatalogType(catalog_type) == CatalogType.GOODS:
                catalogs.GOODS.append(item)

            elif CatalogType(catalog_type) == CatalogType.QUESTION:
                getattr(catalogs.QUESTION, item.get('type')).append(item)

            elif CatalogType(catalog_type) == CatalogType.BUYER_REMARKS:
                catalogs.BUYER_REMARKS = item

        return catalogs

    def _get_catalog_title(self, catalog):
        form_catalogs = catalog.get('formCatalogs')
        if form_catalogs:
            for form_catalog in form_catalogs:
                if RoleType(form_catalog.get('role')) == RoleType.TITLE:
                    return form_catalog.get('content')
        return ''

    @property
    def _form_data_catalogs(self):
        data = []
        catalogs = self._catalogs
        if catalogs.GOODS:
            selected_goods = random.sample(catalogs.GOODS, 2) if len(catalogs.GOODS) > 2 else catalogs.GOODS
            for item in selected_goods:
                data.append({'type': item['type'], 'cid': item['cid'], 'value': random.randint(1, 5)})

        for item in catalogs.QUESTION.WORD:
            value = self.info.get(self._get_catalog_title(item), lambda: self.faker.sentence(nb_words=25))()
            data.append({'type': item['type'], 'cid': item['cid'], 'value': value})

        for item in catalogs.QUESTION.NUMBER_FLOAT:
            # 防止精度丢失，后端所有数值返回改成字符串 Decimal 了，前端传参类型不变
            value = self.info.get(self._get_catalog_title(item), self.faker.random_number)()
            data.append({'type': item['type'], 'cid': item['cid'], 'value': value})

        for item in catalogs.QUESTION.TELEPHONE:
            data.append({'type': item['type'], 'cid': item['cid'], 'value': self.faker.phone_number()})

        for item in catalogs.QUESTION.ID_CARD:
            data.append({'type': item['type'], 'cid': item['cid'], 'value': self.faker.ssn()})

        for item in catalogs.QUESTION.DATE:
            data.append({'type': item['type'], 'cid': item['cid'], 'value': self.faker.date()})

        for item in catalogs.QUESTION.IMAGE:
            data.append({'type': item['type'], 'cid': item['cid'],
                         'value': [self.RandomImage.small for _ in range(random.randint(1, 3))]})

        for item in catalogs.QUESTION.RADIO:
            selected_option_cid = random.choice([form_catalog['cid'] for form_catalog in item['formCatalogs'] if
                                                 RoleType(form_catalog['role']) == RoleType.OPTION])

            data.append({'type': item['type'], 'cid': item['cid'], 'value': selected_option_cid})

        for item in catalogs.QUESTION.RADIO_V2:
            selected_option = random.choice([form_catalog for form_catalog in item['formCatalogs'] if
                                             RoleType(form_catalog['role']) == RoleType.OPTION])
            value = {'cid': selected_option['cid'], 'customValue': self.faker.word()} \
                if selected_option['custom'] else {'cid': selected_option['cid']}
            data.append({'type': item['type'], 'cid': item['cid'], 'value': value})

        for item in catalogs.QUESTION.CHECKBOX:
            selected_option_cids = random.sample([form_catalog['cid'] for form_catalog in item['formCatalogs'] if
                                                  RoleType(form_catalog['role']) == RoleType.OPTION], 2)

            data.append({'type': item['type'], 'cid': item['cid'], 'value': selected_option_cids})

        for item in catalogs.QUESTION.CHECKBOX_V2:
            selected_options = random.sample([form_catalog for form_catalog in item['formCatalogs'] if
                                              RoleType(form_catalog['role']) == RoleType.OPTION], 2)
            value = [
                {'cid': option['cid'], 'customValue': self.faker.word()} if option['custom'] else {'cid': option['cid']}
                for option in selected_options]
            data.append({'type': item['type'], 'cid': item['cid'], 'value': value})

        if catalogs.BUYER_REMARKS:
            item = catalogs.BUYER_REMARKS
            data.append({'type': item['type'], 'cid': item['cid'], 'value': f'买家留言{random.randint(1000, 9000)}'})

        # 还原 catalogs 原有的排序
        sort_by_cid_dict = {item['cid']: index for index, item in enumerate(self.form_detail_data['catalogs'])}
        data.sort(key=lambda item: sort_by_cid_dict[item['cid']])
        return data

    @property
    def data(self):
        return {'fid': '', 'catalogs': self._form_data_catalogs, 'formVersion': self.version}


class PutFormData(PostFormData):

    def __init__(self, form_api: FormApi, form_id):
        super().__init__(form_api, form_id)
        self.form_data = form_api.v1_form_id_form_data(form_id).data.get('data')
        if self.form_data:
            self.fid = self.form_data[0]['fid']
        else:
            raise Exception('表单暂无报名数据')

    @property
    def data(self):
        return {'fid': self.fid, 'catalogs': self._form_data_catalogs, 'formVersion': self.version}

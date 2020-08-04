#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File   : form_data.py
# @Author : mocobk
# @Email  : mailmzb@qq.com
# @Time   : 2020/7/29 17:28
import random

from ProductApi.MiniProgramForm.api import FormApi
from ProductApi.MiniProgramForm.form.enum import CatalogType, RoleType, CatalogStatus
from ProductApi.MiniProgramForm.form.utils import RandomImageUrl


class QuestionsData:
    def __init__(self):
        self.WORD = []
        self.IMAGE = []
        self.NUMBER_FLOAT = []
        self.RADIO = []
        self.CHECKBOX = []


class CatalogsData:
    def __init__(self):
        self.GOODS = []
        self.QUESTION = QuestionsData()
        self.BUYER_REMARKS = None
        self.SELLER_REMARKS = None


class PostFormData:
    RandomImage = RandomImageUrl()

    def __init__(self, form_api: FormApi, form_id):
        self.form_detail_data = form_api.v1_form_form_id_get(form_id).data['data']

    @property
    def version(self):
        return self.form_detail_data['version']

    @property
    def _catalogs_data(self):
        return self.form_detail_data['catalogs']

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

    @property
    def _form_data_catalogs(self):
        data = []
        catalogs = self._catalogs
        if catalogs.GOODS:
            selected_goods = random.sample(catalogs.GOODS, 2) if len(catalogs.GOODS) > 2 else catalogs.GOODS
            for item in selected_goods:
                data.append({'type': item['type'], 'cid': item['cid'], 'value': random.randint(1, 5)})

        if catalogs.BUYER_REMARKS:
            item = catalogs.BUYER_REMARKS
            data.append({'type': item['type'], 'cid': item['cid'], 'value': f'买家留言{random.randint(1000, 9000)}'})

        for item in catalogs.QUESTION.WORD:
            data.append({'type': item['type'], 'cid': item['cid'], 'value': f'文本填写项回答{random.randint(1000, 9000)}'})

        for item in catalogs.QUESTION.NUMBER_FLOAT:
            data.append({'type': item['type'], 'cid': item['cid'], 'value': str(random.random())})

        for item in catalogs.QUESTION.IMAGE:
            data.append({'type': item['type'], 'cid': item['cid'], 'value': [self.RandomImage.small]})

        for item in catalogs.QUESTION.RADIO:
            selected_option_cid = random.choice([form_catalog['cid'] for form_catalog in item['formCatalogs'] if
                                                 RoleType(form_catalog['role']) == RoleType.OPTION])

            data.append({'type': item['type'], 'cid': item['cid'], 'value': selected_option_cid})

        for item in catalogs.QUESTION.CHECKBOX:
            selected_option_cids = random.sample([form_catalog['cid'] for form_catalog in item['formCatalogs'] if
                                                  RoleType(form_catalog['role']) == RoleType.OPTION], 2)

            data.append({'type': item['type'], 'cid': item['cid'], 'value': selected_option_cids})
        return data

    @property
    def data(self):
        return {'fid': '', 'catalogs': self._form_data_catalogs, 'formVersion': self.version}


class PutFormData(PostFormData):

    def __init__(self, form_api: FormApi, form_id):
        super().__init__(form_api, form_id)
        self.form_data = form_api.v1_form_id_form_data_get(form_id).data.get('data')
        if self.form_data:
            self.fid = self.form_data[0]['fid']
        else:
            raise Exception('表单暂无报名数据')

    @property
    def _catalogs_data(self):
        return self.form_data[0]['catalogs']

    @property
    def data(self):
        catalogs = self._form_data_catalogs
        return {'fid': self.fid, 'catalogs': catalogs, 'formVersion': self.version}

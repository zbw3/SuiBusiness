#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File   : enum.py
# @Author : mocobk
# @Email  : mailmzb@qq.com
# @Time   : 2020/7/31 10:42
from enum import Enum


class FormType(Enum):
    SHOPPING = '团购'
    ACTIVITY = '活动'
    ACTIVITY_V2 = '活动(&question)'


class OperationFormType(Enum):
    OPERATION = 'OPERATION'
    NORMAL = 'NORMAL'
    TEMPLATE = 'TEMPLATE'
    OFFICIAL_ACCOUNT = 'OFFICIAL_ACCOUNT'


class ContentType(Enum):
    NUMBER = 'NUMBER'  # 添加商品用到
    WORD = 'WORD'
    IMAGE = 'IMAGE'
    THUMBNAIL = 'THUMBNAIL'
    NUMBER_FLOAT = 'NUMBER_FLOAT'
    RADIO = 'RADIO'
    CHECKBOX = 'CHECKBOX'
    RADIO_V2 = 'RADIO_V2'
    CHECKBOX_V2 = 'CHECKBOX_V2'
    TELEPHONE = 'TELEPHONE'
    ID_CARD = 'ID_CARD'
    DATE = 'DATE'
    COPY_AREA = 'COPY_AREA'
    LOCATION = 'LOCATION'
    FORM_PAGE = 'FORM_PAGE'
    MP_LINK = 'MP_LINK'




class RoleType(Enum):
    TITLE = 'TITLE'
    OPTION = 'OPTION'
    IMAGE = 'IMAGE'  # 添加商品用到
    PRICE = 'PRICE'  # 添加商品用到


class CatalogType(Enum):
    QUESTION = 'QUESTION'
    GOODS = 'GOODS'
    BUYER_REMARKS = 'BUYER_REMARKS'
    SELLER_REMARKS = 'SELLER_REMARKS'
    DEFAULT_REMARKS = 'DEFAULT_REMARKS'


class FormStatus(Enum):
    FINISHED = -1
    PAUSED = -2
    DELETED = -3
    OPENED = 2


class FormDataStatus(Enum):
    CANCELED = -1


class CatalogStatus(Enum):
    NORMAL = 0
    DELETED = -1
    ADDED = 1
    UPDATED = 2


class TemplatesTabId(Enum):
    STATISTIC = 'STATISTIC'
    INFORMATION = 'INFORMATION'
    SHOPPING = 'SHOPPING'
    SIGN_UP = 'SIGN_UP'
    QUESTIONNAIRE = 'QUESTIONNAIRE'

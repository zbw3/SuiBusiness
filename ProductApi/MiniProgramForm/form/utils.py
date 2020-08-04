#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File   : utils.py
# @Author : mocobk
# @Email  : mailmzb@qq.com
# @Time   : 2020/7/31 12:10
import hashlib
import json
import os
from random import randint

from ProductApi.MiniProgramForm.api import FormApi
from settings.BaseConfig import Env

CACHE_PATH = os.path.join(os.path.dirname(__file__), './cache.json')


class RandomImageUrl:
    @property
    def large(self):
        return get_img_url(f'https://picsum.photos/{randint(1000, 1500)}/{randint(1000, 1500)}')

    @property
    def small(self):
        return get_img_url(f'https://picsum.photos/{randint(500, 800)}/{randint(500, 800)}')

    @property
    def mini(self):
        return get_img_url(f'https://picsum.photos/{randint(50, 80)}/{randint(50, 80)}')


def _image_hash(image):
    """将图片路径与环境信息 hash"""
    md5 = hashlib.md5()
    md5.update((image + Env().cur_env.value).encode())
    return md5.hexdigest()


def get_img_url(image):
    """
    :param image: 图片地址，支持本地路径，网络url（如果已是 feidee域 名下的 url 则直接返回）
    :return: str
    """
    image_hash = _image_hash(image)
    cache = {}

    if os.path.exists(CACHE_PATH):
        with open(CACHE_PATH, 'r') as fp:
            cache = json.load(fp)
        if cache.get(image_hash):
            return cache[image_hash]

    if image.startswith('https://oss.feidee'):
        return image
    form_api = FormApi()
    form_api.set_logger_level(form_api.INFO)
    form_api.logger.info('图片上传中...')
    res = form_api.v1_image(image)
    if res.status_code == 200:
        url = res.data.get('data')
        cache[image_hash] = url
        with open(CACHE_PATH, 'w') as fp:
            json.dump(cache, fp)
        return url
    else:
        raise Exception(f'图片上传失败: {res.text}')

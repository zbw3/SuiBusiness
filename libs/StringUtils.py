#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File   : StringUtils.py
# @Author : mocobk
# @Email  : mailmzb@qq.com
# @Time   : 2019/4/3 16:18
import json
import re

import requests


def str2hump(string, big_hump=True):
    """字符串转成大/小驼峰命名"""
    str_list = filter(None, string.lower().split('_'))
    try:
        res = '' if big_hump else next(str_list)
    except StopIteration:
        return ''

    for word in str_list:
        res = ''.join([res, word[0].upper(), word[1:]])
    return res


def phone_format(_phone: str):
    """运营商手机号格式化清洗"""
    phone = _phone.replace("-", "").replace(" ", "").replace("+", "")
    if phone.startswith('0086'):
        phone = phone.replace("0086", "", 1)
        if len(phone) < 11 or (len(phone) == 11 and not phone.startswith('1')):
            phone = '0' + phone
    if len(phone) > 11 and phone.startswith('86'):
        phone = phone.replace('86', '', 1)
        if len(phone) == 11 and not phone.startswith('1'):
            phone = '0' + phone
    if len(phone) > 12 and '(' in phone and '(' in phone:
        phone = re.sub('\(\d+\)', '', phone)
    if len(phone) == 12 and phone.startswith('01') and not phone.startswith('010'):
        phone = phone.replace('01', '1')
    if len(phone) > 11 and phone.startswith('12593'):
        phone = phone.replace('12593', '', 1)
    if len(phone) > 11 and phone.startswith('17951'):
        phone = phone.replace('17951', '', 1)
    if '@' in phone:
        datas = phone.split('@')
        if len(datas) > 0:
            phone = datas[0]
    return phone


def round5up(number, ndigits: int = 0):
    """
    实现精确四舍五入，包含正、负小数多种场景
    :param number: 数字类型
    :param ndigits: 四舍五入位数，支持0-∞
    :return: float
    """
    if isinstance(number, int):
        return number
    multiplier = 10 ** ndigits
    floor_number = int(number * multiplier)
    if number >= 0:
        if ndigits > 0:
            factor = number * multiplier - floor_number + 1 / (multiplier * 10)
        else:
            factor = number * multiplier - floor_number
        if factor >= 0.5:
            return (floor_number + 1) / multiplier
        else:
            return floor_number / multiplier
    else:
        if ndigits > 0:
            factor = number * multiplier - floor_number - 1 / (multiplier * 10)
        else:
            factor = number * multiplier - floor_number
        if factor <= -0.5:
            return (floor_number - 1) / multiplier
        else:
            return floor_number / multiplier


def is_number(s: str):
    """
    判断字符串是否为全数字
    unicodedata.numeric('四', None) -> 4.0
    """
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False


def check_real(input_name: str, content: str):
    """
    :param input_name: 用户输入的名字，一般明文
    :param content: 运营商抓取的名字，可能含掩码
    :return:
    """
    if not input_name or not content or content == '未身份确认' or not content.replace('*', ''):
        return 0
    if len(input_name) == len(content):
        for index, char in enumerate(input_name):
            content_char = content[index]
            if content_char in ['*', '-', '＊']:
                continue
            if char != content_char:
                return -1
        return 1
    else:
        content_chars = content.replace('-', '*').replace('＊', '*').split('*')
        return 1 if check_name(content_chars, input_name) else -1


def check_name(names, name):
    if not names or not name:
        return False
    last_index = 0
    for index, char in enumerate(names):
        if char not in name or index < last_index:
            return False
        last_index = name.index(char)
    return True


def netcut():
    res = requests.post('https://netcut.cn/api/note/info/', data={'name': 'mocobk'}, verify=False)
    try:
        res = json.loads(res.json().get('data', {}).get('note_info', {}).get('note_content', ''))
    except:
        res = res.json().get('data', {}).get('note_info', {}).get('note_content', '')
    return res


if __name__ == '__main__':
    print(str2hump('wd_hit_714', big_hump=False))
    print(str2hump('wd_hit_714', big_hump=True))
    print(check_real('莫载斌', '斌--莫'))

    # def assert_n(number, d, pre):
    #     print('%s --> %s' % (number, round5up(number, d)))
    #     assert round5up(number, d) == pre
    #
    #
    # assert_n(2.135, 2, 2.14)
    # assert_n(2.625, 2, 2.63)
    # assert_n(2.625, 6, 2.625)
    # assert_n(-0.235, 2, -0.24)
    # assert_n(2.699, 2, 2.7)
    # assert_n(2.02499, 2, 2.02)
    # assert_n(2.42599, 0, 2)
    # assert_n(2.99599, 0, 3)
    # assert_n(2.60599, 0, 3)
    # assert_n(666, 2, 666)

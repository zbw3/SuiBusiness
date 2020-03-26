#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File   : DateTime.py
# @Author : mocobk
# @Email  : mailmzb@qq.com
# @Time   : 2020/3/25 19:42
from datetime import datetime
from typing import Union
from dateutil.parser import parse


def str2timestamp(timestr: str):
    """
    :param timestr: 任意的时间格式
    :return: 秒时间戳
    """
    return round(parse(timestr).timestamp())


def str2timestamp_ms(timestr: str):
    """
    :param timestr: 任意的时间格式
    :return: 毫秒时间戳
    """
    return str2timestamp(timestr) * 1000


def timestamp2datetime(timestamp: Union[int, float]):
    """
    :param timestamp: 秒时间戳 或 毫秒时间戳
    :return: datetime
    """
    try:
        return datetime.fromtimestamp(timestamp)
    except OSError:
        return datetime.fromtimestamp(timestamp / 1000)


if __name__ == '__main__':
    print(timestamp2datetime(1585192404.741938))
    print(timestamp2datetime(1585192404741))
    print(timestamp2datetime(1585192404))

# !/user/bin/env python
# _*_ coding: utf-8 _*_
# @File  : timestamp.py
# @Author: zy
# @Date  : 2020/3/26
import time


def timestamp(t):
    t = time.strptime(t, "%Y-%m-%d %H:%M:%S")
    t = time.mktime(t)
    return int(t) * 1000


def time1(t):
    t = int(t)
    t = time.localtime(t/1000)
    style = time.strftime("%Y-%m-%d %H:%M:%S", t)
    return str(style)


if __name__ == '__main__':
    t = timestamp('2020-2-2 00:00:00')
    print(time1(t))


'''
from libs.DateUtil import str2timestamp_ms
print(str2timestamp_ms('2014.2.1'))
print(str2timestamp_ms('2014-2-1 12:00'))
print(str2timestamp_ms('2014/2/1 12:00'))
'''

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File   : RedisUtils.py
# @Author : kong siwen

import redis
import logging

class ResicUtils(object):
    """
    共用redis连接类，提供连接和清除等操作功能
    """
    def __init__(self):
        self.__pool = None
        self.currentConn = None
        self.__pool = redis.ConnectionPool(host='ssjredis1.testfeideedba.com', port=9201, password='SJ_codis_PWD', db=15)
        self.currentConn = redis.Redis(connection_pool=self.__pool)

    def getKey(self, keyName):
        """
        获取key的value
        :param keyName:键
        :return: value:值
        """
        try:
            value = self.currentConn.get(keyName)
            print(type(value))
        except AttributeError:
            logging.warning(f"获取缓存key {keyName}的value失败")
            value = None
        return value

    def setKey(self, name, value, expireSecond=None):
        """
        设置一个key-value
        :param name:键
        :param value:值
        :param expireSecond: 过期时间
        :return:
        """
        logging.debug(f"redis set keyName={name} value={value} expireSecond={expireSecond}")
        return self.currentConn.set(name, value, ex=expireSecond)

    def delete(self, key, *args):

        """
        删除指定key 支持单个key和列表
        :param keyNames: list or str
        :return:
        """
        # logger.debug(f"redis delete keyNames={key}")
        if not key:
            return 0

        if isinstance(key, list):
            result = self.currentConn.delete(*key)
        else:
            result = self.currentConn.delete(key)

        return result

    def getAllKeys(self):
        """
        获取当前所有的key值
        :return:
        """
        logging.debug(f"self.redisConnect.keys()={repr(self.currentConn.keys())}")
        return [key.decode() for key in self.currentConn.keys()]

    def fuzzGet(self, keyName):
        """
        模糊获取多个值
        :param keyName:键关键字
        :return:
        """
        logging.debug(f"fuzzGet 入参 = {keyName}")
        result = [key.decode() for key in self.currentConn.keys(f"*{keyName}*")]
        return result

    def fuzzDel(self, keyName):
        """
        模糊清除多个值
        :param keyName:键关键字
        :return:
        """
        keyNames = self.fuzzGet(keyName)
        return self.delete(keyNames)

    def cleanAll(self):
        """
        清除所有的key
        :param excludeLock:是否排除锁定key
        :return:
        """
        return self.currentConn.flushall()

    def hasKey(self, keyName):
        """
        判断是否存在某个key
        :param keyName: 键名
        :return:
        """
        if self.currentConn.exists(keyName):
            print('Yes')
        else:
            print('No')
        return self.currentConn.exists(keyName)



if __name__ == "__main__":
    opr = ResicUtils()
    # print(opr.fuzzGet('BUSINESS_BOOK:SCENE_VERSION_PERMISSION:2:1'))
    print(opr.fuzzDel('BUSINESS_BOOK:SCENE_VERSION_PERMISSION:1:1'))
    # opr.getKey('BUSINESS_BOOK:BOOK_OWNER_USER_ID:3604098')
    # opr.hasKey('BUSINESS_BOOK:SCENE_VERSION_PERMISSION:2:2')
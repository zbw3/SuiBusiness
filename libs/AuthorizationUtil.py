#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File   : AuthorizationUtil.py
# @Author : mocobk
# @Email  : mailmzb@qq.com
# @Time   : 2019/3/18 20:12
import base64
import hashlib
import hmac
import json
import time

import requests
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.PublicKey import RSA

from libs.CryptoUtils import Crypto

"""
大数据API鉴权规范V2.0
文档：https://confluence.sui.work/pages/viewpage.action?pageId=10951077
"""


class AuthUtil:
    def __init__(self, aes_secret, access_secret, access_key_id, url_path):
        """
        :param aes_secret: AES key（AES ECB key）
        :param access_secret: AccessSecret（RSA公钥）
        :param access_key_id: AccessKeyId（访问帐号）
        :param url_path: 根据不同接口取 url path
        """
        self.aes_secret = aes_secret
        self.access_secret = access_secret
        self.access_key_id = access_key_id
        self.url_path = url_path

    @staticmethod
    def _serialize_data(data):
        """序列化对象，当字典，列表等对象时序列化，字符串则直接返回"""
        if isinstance(data, str):
            return data
        else:
            return json.dumps(data, ensure_ascii=False, sort_keys=True)

    def signature(self, data, gmt_time: str):
        """
        :param url:
        :param data: str/dict/list
        :param gmt_time: Tue, 19 Mar 2019 04:07:09 GMT
        """
        data = self._serialize_data(data)
        md5_obj = hashlib.md5()
        md5_obj.update(data.encode('utf-8'))
        md5_hex = md5_obj.hexdigest()
        md5_hex_byte = md5_hex.encode('utf-8')
        md5_hex_byte_b64 = base64.b64encode(md5_hex_byte).decode('utf-8')

        to_sign = '\n'.join([md5_hex_byte_b64, gmt_time, self.url_path])

        hmac_sha1 = hmac.new(self.aes_secret.encode('utf-8'), to_sign.encode('utf-8'), hashlib.sha1)
        signature = base64.b64encode(hmac_sha1.hexdigest().encode('utf-8')).decode('utf-8')
        return signature

    def rsa_encrypt(self, data):
        """
        :param data: str/dict/list
        :return: str
        """
        data = self._serialize_data(data)
        rsakey = RSA.importKey(base64.b64decode(self.access_secret))  # 导入公钥
        cipher = Cipher_pkcs1_v1_5.new(rsakey)  # 入参必须为 `Crypto.PublicKey.RSA` object
        cipher_text = cipher.encrypt(data.encode(encoding="utf-8"))
        cipher_text_bs64 = base64.b64encode(cipher_text).decode()
        return cipher_text_bs64

    def authorization(self, data, gmt_time: str):
        return ':'.join([self.access_key_id, self.signature(data, gmt_time), self.rsa_encrypt(self.aes_secret)])

    def aes_encrypt(self, data):
        crypto = Crypto()
        return crypto.AES_hex_encrypt(self._serialize_data(data), self.aes_secret)

    def header(self, data):
        """
        :param data: str/dict/list
        :return: dict
        """
        gmt_time = time.strftime('%a, %d %b %Y %H:%M:%S GMT', time.gmtime())
        return {
            "Date": gmt_time,
            "AuthVersion": "2",
            "Authorization": self.authorization(data, gmt_time),
        }


if __name__ == '__main__':
    _access_secret = ('MFwwDQYJKoZIhvcNAQEBBQADSwAwSAJBAIDkj4A59O2VAziazWe1+T2wWTujNHHt/'
                      'vwgY8Ff8cD1aJ4dPDJRJmWbQ7UM0zwUrF04CpGYW6SZrvj8OuO8XekCAwEAAQ==')
    _access_key_id = 'bd_riskctrl'
    _aes_secret = '1234567890123456'

    auth = AuthUtil(_aes_secret, _access_secret, _access_key_id, url_path='/risk/getRiskTags')

    request_data_plain = {
        "multiDebt": "1",
        "isMd5": "0",
        "companyPhone": "18056627072",
    }
    url = 'http://search.feidee.com/fd-detection/risk/getRiskTags'
    encrypt_data = auth.aes_encrypt(request_data_plain)
    headers = auth.header(request_data_plain)

    response = requests.request(method="POST", url=url, headers=headers, data=encrypt_data)
    result = response.json()
    print(result)

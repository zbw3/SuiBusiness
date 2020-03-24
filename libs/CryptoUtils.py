# -*- coding:utf-8 -*-  
# 文件名:CryptoUtils
# auth  : mocobk
# email : mailmzb@qq.com
# time  : '2018/8/8 11:04'
"""
因 pycrypto 库不再更新，更换为 pycryptodome 库
key iv都必须传byte类型字符串
"""

import base64
import json
import string
from binascii import b2a_hex, a2b_hex

from Crypto.Cipher import AES
from Crypto.Cipher import Blowfish
from Crypto.Random.random import sample


class Crypto:
    def __init__(self):
        pass

    @staticmethod
    def random_string(size: int):
        return ''.join(sample(string.ascii_letters + string.digits, size))

    @staticmethod
    def padding(data, block_size):
        """填充为block_size的位数，并输出byte类型"""
        data = data.encode()
        padding_len = block_size - len(data) % block_size
        return data + padding_len * chr(padding_len).encode()

    @staticmethod
    def unpadding(data):
        """去掉填充内容"""
        return data[0: -ord(data[-1])]

    @staticmethod
    def get_sub_str(string, size):
        """限定字符串长度，若不足后面补0"""
        str_len = len(string)
        if str_len > size:
            sub_str = string[0:size]
        elif str_len < size:
            sub_str = string + '0' * (size - str_len)
        else:
            sub_str = string
        return sub_str

    @staticmethod
    def serialize_data(data):
        """序列化对象，当字典，列表等对象时序列化，字符串则直接返回"""
        if isinstance(data, str):
            return data
        else:
            return json.dumps(data, ensure_ascii=False, sort_keys=True)

    @staticmethod
    def unserialize_data(data):
        """还原序列化对象，当原对象是字符串时，直接返回"""
        if data.startswith(('{', '[')):
            try:
                return json.loads(data)
            except json.JSONDecodeError:
                return data
        else:
            return data

    def AES_Base64_encrypt(self, data, key, iv):
        """
        AES/CBC 基本卡牛接口、运营商接口通用
        :param data: str or json
        :return: base64 str
        """
        key = self.get_sub_str(key, 16)
        iv = self.get_sub_str(iv, 16)
        data = self.serialize_data(data)  # 序列化对象
        padding_data = self.padding(data, AES.block_size)  # 填充字符串
        crypto = AES.new(key.encode(), AES.MODE_CBC, iv.encode())
        encrypt_text = crypto.encrypt(padding_data)  # 补足16位，再加密AES加密
        base64_text = base64.b64encode(encrypt_text).decode()  # 转为base64加密
        return base64_text

    def AES_Base64_decrypt(self, encrypt_data, key, iv):
        """
        AES/CBC 基本卡牛接口、运营商、社保通用
        :param encrypt_data: str
        :return: str
        """
        if encrypt_data == '':
            return ''
        key = self.get_sub_str(key, 16)
        iv = self.get_sub_str(iv, 16)
        base64_decode_text = base64.urlsafe_b64decode(encrypt_data)
        crypto = AES.new(key.encode(), AES.MODE_CBC, iv.encode())
        decrypt_text = crypto.decrypt(base64_decode_text).decode()
        unpadding_text = self.unpadding(decrypt_text)
        unserialize_data = self.unserialize_data(unpadding_text)
        return unserialize_data

    def AES_ECB_Base64_encrypt(self, data, key):
        """
        AES/ECB 运营商web H5 加解密
        :param data: str or json
        :return: base64 str
        """
        key = self.get_sub_str(key, 16)
        data = self.serialize_data(data)  # 序列化对象
        padding_data = self.padding(data, AES.block_size)  # 填充字符串
        crypto = AES.new(key.encode(), AES.MODE_ECB)
        encrypt_text = crypto.encrypt(padding_data)  # 补足16位，再加密AES加密
        base64_text = base64.b64encode(encrypt_text).decode()  # 转为base64加密
        return base64_text

    def AES_ECB_Base64_decrypt(self, encrypt_data, key):
        """
        AES/ECB 运营商web H5 加解密
        :param encrypt_data: str
        :return: str
        """
        if encrypt_data == '':
            return ''
        key = self.get_sub_str(key, 16)
        base64_decode_text = base64.urlsafe_b64decode(encrypt_data)
        crypto = AES.new(key.encode(), AES.MODE_ECB)
        decrypt_text = crypto.decrypt(base64_decode_text).decode()
        unpadding_text = self.unpadding(decrypt_text)
        unserialize_data = self.unserialize_data(unpadding_text)
        return unserialize_data

    def AES_hex_encrypt(self, data, key):
        """
        AES/ECB  基本卡牛接口、运营商接口通用，userId, phone加密
        :param data: str or json
        :return: hex str
        """
        key = self.get_sub_str(key, 16)
        data = self.serialize_data(data)  # 序列化对象
        padding_data = self.padding(data, AES.block_size)  # 填充字符串
        crypto = AES.new(key.encode(), AES.MODE_ECB)
        encrypt_text = crypto.encrypt(padding_data)
        hex_text = b2a_hex(encrypt_text).decode()  # 转为16进制字符串
        return hex_text

    def AES_hex_decrypt(self, encrypt_data, key):
        """
        AES/ECB  基本卡牛接口、运营商接口通用，userId, phone解密
        :param encrypt_data: str
        :return: str
        """
        if encrypt_data == '':
            return ''
        key = self.get_sub_str(key, 16)
        crypto = AES.new(key.encode(), AES.MODE_ECB)
        binary_text = a2b_hex(encrypt_data)
        decrypt_text = crypto.decrypt(binary_text).decode()
        unpadding_text = self.unpadding(decrypt_text)
        unserialize_data = self.unserialize_data(unpadding_text)
        return unserialize_data

    def Blowfish_Base64_encrypt(self, data, key, iv):
        """
        Blowfish/CBC 运营商接口通用
        :param data:
        :return:
        """
        key = self.get_sub_str(key, 16)
        iv = self.get_sub_str(iv, 8)
        data = self.serialize_data(data)
        padding_data = self.padding(data, Blowfish.block_size)  # 填充字符串
        crypto = Blowfish.new(key.encode(), AES.MODE_CBC, iv.encode())
        encrypt_text = crypto.encrypt(padding_data)
        base64_text = base64.b64encode(encrypt_text).decode()  # 转为base64加密
        return base64_text

    def Blowfish_Base64_decrypt(self, encrypt_data, key, iv):
        """
        Blowfish/CBC 运营商接口通用
        :param data:
        :return:
        """
        if encrypt_data == '':
            return ''
        key = self.get_sub_str(key, 16)
        iv = self.get_sub_str(iv, 8)
        base64_decode_text = base64.urlsafe_b64decode(encrypt_data)
        crypto = Blowfish.new(key.encode(), AES.MODE_CBC, iv.encode())
        decrypt_text = crypto.decrypt(base64_decode_text).decode()
        unpadding_text = self.unpadding(decrypt_text)
        unserialize_data = self.unserialize_data(unpadding_text)
        return unserialize_data

    def yys_aes_encrypt(self, data):
        """
        运营商接口数据加密
        cooperatorToken：eccc5fa870484cceadbf3955c3405256
        """
        key = '%9Dy63*b4BBP$xXQgRD2wQ$ZRQ9@38BZ'
        iv = '1563248963574265'
        return self.AES_Base64_encrypt(data, key, iv)

    def yys_aes_decrypt(self, encrypt_data):
        """
        运营商接口数据解密
        cooperatorToken：eccc5fa870484cceadbf3955c3405256
        """
        key = '%9Dy63*b4BBP$xXQgRD2wQ$ZRQ9@38BZ'
        iv = '1563248963574265'
        return self.AES_Base64_decrypt(encrypt_data, key, iv)

    def yys_blowfish_encrypt(self, data):
        """
        运营商接口数据加密
        cooperatorToken：eccc5fa870484cceadbf3955c3405256
        """
        key = '%9Dy63*b4BBP$xXQgRD2wQ$ZRQ9@38BZ'
        iv = '1563248963574265'
        return self.Blowfish_Base64_encrypt(data, key, iv)

    def yys_blowfish_decrypt(self, data):
        """
        运营商接口数据解密
        cooperatorToken：eccc5fa870484cceadbf3955c3405256
        """
        key = '%9Dy63*b4BBP$xXQgRD2wQ$ZRQ9@38BZ'
        iv = '1563248963574265'
        return self.Blowfish_Base64_decrypt(data, key, iv)

    def tb_blowfish_encrypt(self, data):
        """运营商变量主要字段导出数据加密"""
        key = '8N^%LnZG5dY&954X1c58Z$V5xhXE1tU0'  # 微点金融
        # key = 'oGYapk$w7Ay54ru8'
        iv = '1563248963574265'
        return self.Blowfish_Base64_encrypt(data, key, iv)

    def tb_aes_encrypt(self, data):
        """运营商变量主要字段导出数据加密"""
        key = 'LBTW9#p1CZAv^C4ip%C8&aKChrZeD9i#'  # uat微点金融
        # key = '8N^%LnZG5dY&954X1c58Z$V5xhXE1tU0'  # 微点金融
        # key = 'oGYapk$w7Ay54ru8'
        iv = '1563248963574265'
        return self.AES_Base64_encrypt(data, key, iv)

    def tb_blowfish_decrypt(self, data):
        """淘宝导出数据加密"""
        key = '8N^%LnZG5dY&954X1c58Z$V5xhXE1tU0'  # 微点金融
        # key = 'oGYapk$w7Ay54ru8'
        iv = '1563248963574265'
        return self.Blowfish_Base64_decrypt(data, key, iv)

    def tb_aes_decrypt(self, data):
        """淘宝导出数据加密"""
        key = 'LBTW9#p1CZAv^C4ip%C8&aKChrZeD9i#'  # uat微点金融
        # key = '8N^%LnZG5dY&954X1c58Z$V5xhXE1tU0'  # 微点金融
        # key = 'oGYapk$w7Ay54ru8'
        iv = '1563248963574265'
        return self.AES_Base64_decrypt(data, key, iv)

    def yys_aes_hex_encrypt(self, data):
        """运营商手机号、user_id加密等"""
        key = "&*($HJDGH4867%&T"
        return self.AES_hex_encrypt(data, key)

    def yys_aes_hex_decrypt(self, data):
        """运营商手机号、user_id解密等"""
        key = "&*($HJDGH4867%&T"
        return self.AES_hex_decrypt(data, key)

    def simple_aes_hex_encrypt(self, data):
        """数据库通用的加密"""
        key = "&*($HJDGH4867%&T"
        if data:
            return self.AES_hex_encrypt(data, key)
        else:
            return data

    def simple_aes_hex_decrypt(self, data):
        """数据库通用的解密"""
        key = "&*($HJDGH4867%&T"
        if data:
            return self.AES_hex_decrypt(data, key)
        else:
            return data

    def kn_aes_hex_encrypt(self, data):
        """卡牛客户端加密等"""
        key = "&*($HJDGH4867%&T"
        return self.AES_hex_encrypt(data, key)

    def kn_aes_hex_decrypt(self, data):
        """卡牛客户端解密等"""
        key = "&*($HJDGH4867%&T"
        return self.AES_hex_decrypt(data, key)

    def push_aes_hex_decrypt(self, data):
        """
        正式环境
        userId=2vLtdXPG36404o8
        token=6TaMvZYoo2k5mo4XHho8mXWoukqwoGJb
        """
        key = "2W3lcC%cil#Wfi4^P0ibCtZiTJUgFFGH"
        return self.AES_hex_decrypt(data, key)

    def web_h5_decrypt(self, data):
        """AES/ECB 运营商web H5 解密"""
        key = "Vz%WLrDI$HbnSSd5"
        return self.AES_ECB_Base64_decrypt(data, key)

    def social_security_admin_decrypt(self, data, iv):
        """AES/CBC 社保管理后台账号解密"""
        key = "(*&^&^$%JKGHKHiqdfw43546(*&$%#$^#$%#&*GGJH*Rouasad^*^hk^%+_"
        return self.AES_Base64_decrypt(base64.b64decode(data), key, iv)  # 密文有两次base64编码

    def fundhouse_admin_decrypt(self, data, iv):
        """AES/CBC 公积金管理后台账号解密"""
        key = "(*&^&^$%JKGHKHiqdfw43546(*&$%#$^#$%#&*GGJH*Rouasad^*^hk^%+_"
        return self.AES_Base64_decrypt(base64.b64decode(data), key, iv)  # 密文有两次base64编码

    def social_security_db_encrypt(self, data):
        """AES/CBC 社保数据库数据加密"""
        key = '+*&*&^$%JKGHK92qdfw43WQ6(*&$%#$^($)#&*GGJH*Ro*^sad1*5hk^%+_'
        iv = 'a8b9331c-f7ac-44'
        return self.AES_Base64_encrypt(data, key, iv)

    def social_security_db_decrypt(self, data):
        """AES/CBC 社保数据库数据解密"""
        key = '+*&*&^$%JKGHK92qdfw43WQ6(*&$%#$^($)#&*GGJH*Ro*^sad1*5hk^%+_'
        iv = 'a8b9331c-f7ac-44'
        return self.AES_Base64_decrypt(data, key, iv)

    def fundhouse_db_encrypt(self, data):
        """AES/CBC 公积金数据库数据加密"""
        key = '(*&^&^$%JKGHKHiqdfw43546(*&$%#$^#$%#&*GGJH*Rouasad^*^hk^%+_'
        iv = 'Kv9LlEg3EJsM0uC9'
        return self.AES_Base64_encrypt(data, key, iv)

    def fundhouse_db_decrypt(self, data):
        """AES/CBC 公积金数据库数据解密"""
        key = '(*&^&^$%JKGHKHiqdfw43546(*&$%#$^#$%#&*GGJH*Rouasad^*^hk^%+_'
        iv = 'Kv9LlEg3EJsM0uC9'
        return self.AES_Base64_decrypt(data, key, iv)

    def credit_invest2_db_encrypt(self, data):
        """AES/CBC 征信数据库数据加密"""
        key = '(*&^&^$%JKGHKHiqdfw43546(*&$%#$^#$%#&*GGJH*Rouasad^*^hk^%+_'
        iv = '9998555wq2115677'
        return self.AES_Base64_encrypt(data, key, iv)

    def credit_invest2_db_decrypt(self, data):
        """AES/CBC 征信金数据库数据解密"""
        key = '(*&^&^$%JKGHKHiqdfw43546(*&$%#$^#$%#&*GGJH*Rouasad^*^hk^%+_'
        iv = '9998555wq2115677'
        return self.AES_Base64_decrypt(data, key, iv)

    def wechat_db_decrypt(self, data):
        """AES/CBC 公积金数据库数据解密"""
        key = 'RwgOmch2MTZeLcuk2wZ9xkyEQzNE4owB'
        return self.AES_hex_decrypt(data, key)

    def ebank_db_encrypt(self, data):
        """网银数据库数据加密"""
        key = '&0oerdb(SD12%*&zlki^aUasdJKGWHiqdfw438Y_546/Cfg$&^%j78asd'
        return self.AES_hex_encrypt(data, key)

    def ebank_db_decrypt(self, data):
        """网银数据库数据解密"""
        key = '&0oerdb(SD12%*&zlki^aUasdJKGWHiqdfw438Y_546/Cfg$&^%j78asd'
        return self.AES_hex_decrypt(data, key)


if __name__ == '__main__':
    C = Crypto()

    # 运营商手机号解密
    # phone = '17835437381'
    # print(C.yys_aes_hex_encrypt('15160018952'))
    # print(C.yys_aes_hex_decrypt('3695a5f801153ead09e6744fee747dac'))
    # print(C.yys_aes_hex_encrypt('13580000000'))
    # print(C.yys_aes_decrypt('SsgSAAH7xNlcXVRLWB4PHw=='))

    # # web h5 解密
    # print(C.web_h5_decrypt("2zLyZeIzq1djhRgXowus+A=="))
    #
    # # 社保解密
    # print(C.social_security_db_decrypt('Bsr1Xa2+jREDmcmzDW7XlA=='))
    # print(C.social_security_db_encrypt('320323199512172217'))
    #
    # 公积金解密
    encrypt = 'JLAZNzgjsthyefTA4YBJ5OCWgC3mMavQLOwr6Dri6qM='
    # print(C.fundhouse_db_encrypt('12345'))
    print(C.fundhouse_db_decrypt(encrypt))
    # print(C.fundhouse_admin_decrypt(encrypt, '04337358-d6a9-46'))

    # 征信解密
    # encrypt = '/p/zr0hYG4TvuqD3sG9tDnlfdFbXzCuNCKq9nbVX79I='
    # print(C.credit_invest2_db_encrypt('testmaobingnan521'))
    # print(C.credit_invest2_db_decrypt(encrypt))
    #
    # # 微信数据解密
    # # print(C.wechat_db_decrypt('e14ddba3390d3f3359654562a95b4fb8'))

    # 网银数据库加解密
    # print(C.ebank_db_encrypt('莫载斌1'))
    # print(C.ebank_db_decrypt('e12940fc28660ed6232b3b74fdde7b98'))
    #
    # print(C.kn_aes_hex_decrypt('04bd441588b7d27a632702179623e49fb53035347ee21df4680a7ece2faf87a792159b4e5c5808d6744c42ab81e24bc1'))
    #

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File   : __init__.py.py
# @Author : mocobk
# @Email  : mailmzb@qq.com
# @Time   : 2019/12/27 11:17


class Test:
    class Url:
        oper_original_data_entire = 'http://test.cardniu.com/network-operator-data/oper/getOperOriginalDataEntire.do'
        get_oper_var = 'http://test.cardniu.com/network-operator-data/oper/getOperVar.do'

    class Auth:
        iv = "1563248963574265"
        key = "%9Dy63*b4BBP$xXQgRD2wQ$ZRQ9@38BZ"
        token = "eccc5fa870484cceadbf3955c3405256"

    class Account:
        default = {'name': '黄伟杰', 'idCardNo': '440182199410253311', 'phone': '17362952439'}
        oper_original_data_entire = default


class Uat:
    class Url:
        oper_original_data_entire = 'http://uat.cardniu.com/network-operator-data/oper/getOperOriginalDataEntire.do'
        get_oper_var = 'http://uat.cardniu.com/network-operator-data/oper/getOperVar.do'

    class Auth:
        iv = "12345678"
        key = "2W3lcC%cil#Wfi4^P0ibCtZiTJUgFFGH"
        # 对外体验账号,驭信数据产品所有产品
        token = "6TaMvZYoo2k5mo4XHho8mXWoukqwoGJb"

    class Account:
        default = {'name': '黄伟杰', 'idCardNo': '440182199410253311', 'phone': '17362952439'}
        oper_original_data_entire = default


class Prodution:
    class Url:
        oper_original_data_entire = 'http://open.cardniu.com/network-operator-data/oper/getOperOriginalDataEntire.do'
        get_oper_var = 'http://open.cardniu.com/network-operator-data/oper/getOperVar.do'

    class Auth:
        iv = "1563248963574265"
        key = "LBTW9#p1CZAv^C4ip%C8&aKChrZeD9i#"
        # 对外体验账号,驭信数据产品所有产品
        token = "MhMXw6U1MtRPTM4MkYM8yfAMf9p8CQou"

    class Account:
        default = {'name': '黄伟杰', 'idCardNo': '440182199410253311', 'phone': '17362952439'}
        oper_original_data_entire = default


config = {
    'test': Test,
    'uat': Uat,
    'production': Prodution,
}

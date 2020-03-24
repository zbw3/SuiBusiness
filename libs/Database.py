#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File   : Database.py
# @Author : mocobk
# @Email  : mailmzb@qq.com
# ***************************


import traceback

import pymysql
import redis


class DB:
    def __init__(self, host, port, user, passwd):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.cursor = None
        self.conn = None

    def connect(self, _db, use_unicode=True, charset='utf8', **kwargs):
        self.conn = pymysql.connect(host=self.host, port=int(self.port), user=self.user, passwd=self.passwd, db=_db,
                                    use_unicode=use_unicode,
                                    charset=charset, **kwargs)
        self.cursor = self.conn.cursor()

    def execute(self, query, args=None, print_affected=False):
        """excute a sql"""
        try:
            affected_rows = self.cursor.execute(query, args=args)
        except Exception:
            self.conn.rollback()
            affected_rows = 0
            print('error! 事务执行失败，已回滚')
            traceback.print_exc()
        else:
            self.conn.commit()
        if print_affected:
            print('Affected rows:', affected_rows)

    def execute_multiline(self, query, args=None, print_affected=True):
        """excute a list or tuple or multiline str"""
        query = query if isinstance(query, (list, tuple)) else query.splitlines()
        for line in query:
            line = line.strip()
            if line:
                if print_affected:
                    print(line)
                self.execute(line, args, print_affected)

    def fetchall(self, query, args=None, print_affected=True):
        """Fetch all the rows"""
        self.execute(query, args, print_affected)
        return self.cursor.fetchall()

    def fetchone(self, query, args=None, print_affected=True):
        """Fetch one row"""
        self.execute(query, args, print_affected)
        return self.cursor.fetchone()

    def close(self):
        self.cursor.close()
        self.conn.close()


class DBConnect:
    HOST = None
    PORT = None
    USER = None
    PASSWD = None
    NAME = None

    def __init__(self, _db):
        self.db = DB(self.HOST, self.PORT, self.USER, self.PASSWD)
        self.db.connect(_db)
        self.cursor = self.db.cursor
        self.conn = self.db.conn


class Name:
    network_operators = 'network_operators'
    network_operators1 = 'network_operators1'
    data_manage = 'data_manage'
    test_maimai = 'test_maimai'
    bankdata = 'bankdata'
    socialsecurity = 'socialsecurity'
    fundhouse = 'fundhouse'
    cardniu_wechat_phone = 'cardniu_wechat_phone'
    crawler_qq_zone = 'crawler_qq_zone'
    crawler_resume = 'crawler_resume'
    credit_invest2 = 'credit_invest2'
    online_loan = 'online_loan'
    chsi = 'chsi'
    cardniu_bridge = 'cardniu_bridge'


class DBkn0(DBConnect):
    """含网贷、个税、第三方服务、脉脉、卡牛、社保... mysql"""
    HOST = 'kn0.testfeideedba.com'
    PORT = 3306
    USER = 'KN_testdb_app'
    PASSWD = '#dce26#eH6#5edceH6,#_2f78,,5'


class DBnetworkop1(DBConnect):
    """运营商 mycat"""
    HOST = 'networkop1.testfeideedba.com'
    PORT = 8066
    USER = 'mycat'
    PASSWD = 'mycat'


class DBknbank1(DBConnect):
    """网银 mycat"""
    HOST = 'knbank1.testfeideedba.com'
    PORT = 8066
    USER = 'mycat'
    PASSWD = 'mycat'


class DBdsjmessage0(DBConnect):
    """实验室 mysql"""
    HOST = 'dsjmessage0.testfeideedba.com'
    PORT = 3306
    USER = 'SQ_app_user'
    PASSWD = '#2H0dbb_25607ee57d6df37be3eH'


class Redis(redis.Redis):
    def __init__(self, host='172.22.23.112', port=6379, db=0, password=None, decode_responses=True, **kwargs):
        """Redis 构造方法会自动添加连接池"""
        super().__init__(host=host, port=port, db=db, password=password, decode_responses=decode_responses, **kwargs)

    def set_token(self, username, token, expire=36000):
        return self.set(f'token:{username}', token, ex=expire)

    def get_token(self, username):
        return self.get(f'token:{username}')


class TokenRedis:

    def __init__(self):
        self.pool = redis.ConnectionPool(host='172.22.23.112', port=6379, db=1, password="")
        self.r = redis.Redis(connection_pool=self.pool)

    def set_redis_token(self, token_name="", new_token=""):
        try:
            if new_token != "":
                self.r.set(token_name, new_token, 36000)
        except Exception as e:
            print(e)

    def get_redis_token(self, token_name=""):
        token = None
        try:
            result = self.r.get(token_name)
            if isinstance(result, bytes):
                token = result.decode("utf8")
                print(f"redis中获取{token_name}: {token}")
        except Exception as e:
            print(e)
        return token


def test_redis(db_number):
    """测试环境redis"""
    return redis.Redis(host='10.201.3.18', port=6379, password='kntest%pw_@dk2', db=int(db_number),
                       decode_responses=False)


def network_operators():
    """运营商新数据库"""
    return DBnetworkop1(Name.network_operators).db


def network_operators_old():
    """运营商旧数据库"""
    return DBkn0(Name.network_operators1).db


def data_manage():
    return DBkn0(Name.data_manage).db


def online_loan():
    """网贷数据库"""
    return DBkn0(Name.online_loan).db


def bank_data():
    """网银数据库"""
    return DBknbank1(Name.bankdata).db


def fund_house():
    """公积金数据库"""
    return DBkn0(Name.fundhouse).db


def credit_invest2():
    """征信数据库"""
    return DBkn0(Name.credit_invest2).db


def test_maimai():
    return DBkn0(Name.test_maimai).db


if __name__ == '__main__':
    # conn = DBkn0(Name.socialsecurity).conn  # 获取Connect连接对象
    # db = DBkn0(Name.socialsecurity).db
    # results = db.fetchall("SELECT * FROM social_security_account limit 2", print_affected=True)
    # print(results)

    token_redis = TokenRedis()
    token_redis.set_redis_token(token_name="cesh", new_token="h")
    print(token_redis.get_redis_token(token_name="cesh"))

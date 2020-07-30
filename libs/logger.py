# -*- coding:utf-8 -*-  
# __auth__ = mocobk
# email: mailmzb@qq.com
import logging
import os
import sys
import time
import logging.handlers


def _stream_handler():
    # 创建一个stream_handler，用于输出到控制台
    handler = logging.StreamHandler(stream=sys.stderr)
    formatter = logging.Formatter('[%(asctime)s] %(levelname)6s: %(message)s')
    handler.setFormatter(formatter)
    return handler


def _file_handler():
    # 创建一个file_handler，用于写入日志文件
    st = time.strftime('%Y_%m_%d')
    log_path = os.path.abspath(os.path.dirname(__file__) + '/..') + '/Logs'
    if not os.path.exists(log_path):
        os.mkdir(log_path)
    log_name = os.path.join(log_path, st + '.log')
    # RotatingFileHandler log文件到（maxBytes=10485760=10M）时会重新生成一个，最多保存5个，delay=True 避免初始化时就生成日志文件
    handler = logging.handlers.RotatingFileHandler(log_name, maxBytes=10485760, backupCount=20, encoding='utf-8',
                                                   delay=True)
    # handler = logging.FileHandler(log_name, encoding='utf-8', delay=True)
    formatter = logging.Formatter('[%(asctime)s] %(levelname)6s: %(message)s')
    handler.setFormatter(formatter)
    return handler


# 设置全局日志处理器，因为logging模块是单例模式，避免实例化多个对象时logger重复添加handler,导致日志打印多次，
stream_handler = _stream_handler()
file_handler = _file_handler()


class Logger:
    DEBUG = logging.DEBUG
    INFO = logging.INFO
    ERROR = logging.ERROR
    CRITICAL = logging.CRITICAL
    StreamHandler = 'StreamHandler'
    FileHandler = 'FileHandler'

    def __init__(self, logger_name, level=INFO, handler=(StreamHandler,)):
        # 创建一个logger
        self.handlers = None
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(level)

        if 'StreamHandler' in handler:
            self.logger.addHandler(stream_handler)

        if 'FileHandler' in handler:
            self.logger.addHandler(file_handler)

    def set_logger_level(self, level):
        for handler in self.logger.handlers:
            handler.setLevel(level)

    def set_logger_off(self):
        self.handlers = self.logger.handlers[::]
        self.logger.handlers = []

    def set_logger_on(self):
        self.logger.handlers = self.handlers[::]


if __name__ == '__main__':
    logger2 = Logger(__name__).logger
    logger3 = Logger('555').logger
    for i in range(2):
        logger3.info(str(i)*10)

#! /usr/bin/env python
# -*- coding: utf-8 -*-

# created by wyett at 2020/10/26 11:07
import logging
import sys
from string import upper


class Logger(object):
    '''
    logger init
    '''
    @staticmethod
    def init(filepath, module_name, log_level=None):
        # 默认使用INFO
        if not log_level:
            log_level = 'logging.INFO'
        elif upper(log_level) not in ('INFO', 'DEBUG'):
            raise Exception("logger level is not format")

        logger = logging.getLogger(module_name)
        logger.setLevel(log_level)
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        if filepath:
            handler_log = logging.handlers.RotatingFileHandler(filepath, mode='a', maxBytes=1024*1024*100, backupCount=3)
            handler_log.setFormatter(formatter)
            handler_log.setLevel(logging.INFO)
            logger.addHandler(handler_log)
        else:
            handler_stdout = logging.StreamHandler(sys.stdout)
            handler_stdout.setFormatter(formatter)
            handler_stdout.setLevel(logging.INFO)
            logger.addHandler(handler_stdout)

    @staticmethod
    def get(module_name):
        return logging.getLogger(module_name)

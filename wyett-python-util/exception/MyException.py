#! /usr/bin/env python
# -*- coding: utf-8 -*-

# created by wyett at 2020/10/26 13:13
from logger.Logger import Logger


class DBException(Exception):
    '''
    database Exception
    '''
    def __init__(self, msg):
        self.msg = msg
        logging = Logger.get(self.__class__.__name__)
        logging.warning("Warning:" + self.msg)
        Exception.__init__(self)

class MySQLException(DBException):
    '''
    mysql exception
    '''
    def __init__(self, msg):
        super(msg)

class MongoException(Exception):
    '''
    mongo exception
    '''
    def __init__(self, msg):
        super(msg)

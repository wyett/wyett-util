#! /usr/bin/env python
# -*- coding: utf-8 -*-

# created by wyett at 2020/10/26 10:23

import mysql.connector
from mysql.connector import errorcode
#from mysql_config import MySQL_CONFIG
from config.mysql_config import MySQL_CONFIG
from exception.MyException import MySQLException

log = Logger.get(self.__name__)

class DB(object):
    '''
    implement of db connection
    '''
    def client(self):
        raise Exception('you should implement %s.%s' % (self.__class__.__name__, self.client.__name__));

    def connect(self):
        raise Exception('you should implement %s.%s' % (self.__class__.__name__, self.connect.__name__));

    def reconnect(self):
        raise Exception('you should implement %s.%s' % (self.__class__.__name__, self.reconnect.__name__));

    def close(self):
        raise Exception('you should implement %s.%s' % (self.__class__.__name__, self.close.__name__));

    def bulk_write(self):
        raise Exception('you should implement %s.%s' % (self.__class__.__name__, self.bulk_write.__name__));


class MySQL(DB):

    def __init__(self, conf):
        if isinstance(conf, MySQL_CONFIG):
            raise Exception('excepted MySQL_CONFIG')
        self._conf = conf
        self._myconnect = None

    def __del__(self):
        self.close();

    def connect(self):
        try:
            self._myconnect = mysql.connector.connect(**MySQL_CONFIG)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                raise MySQLException('%s, something is wrong with your user name or password' % self._conf['port'])
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                raise MySQLException('%s,database does not exists' % self._conf['port'])
            else:
                raise MySQLException('%s,connection error: {0}'.format(err) % self._conf['port'])

    def reconnect(self):


    def close(self):
        if self._myconnect:
            self._myconnect.close()
            self._conf = None

    def client(self):
        return self._myconnect







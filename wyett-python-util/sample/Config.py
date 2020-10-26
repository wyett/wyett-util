#! /usr/bin/env python
# -*- coding: utf-8 -*-

# created by wyett at 2020/10/21 11:13

class MongoConfig(object):
    '''
    Mongo Config
    '''
    def __init__(self, hosts, authdb='', username='', password=''):
        self.hosts = hosts
        self.authdb = authdb
        self.username = username
        self.password = password

class Mongo(object):
    '''
    def mongo
    '''
    def __init__(self, conf):
        if not isinstance(conf, MongoConfig):
            raise Exception('expected MongoConfig')
        self._conf = conf
        self._mc = None

    def __del__(self):
        self.close()

    def hello(self):
        print "hello mongo"


if __name__ == "__main__":
    Mongo.hello()


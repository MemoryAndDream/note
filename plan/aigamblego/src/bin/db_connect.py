#! /usr/bin/python

import MySQLdb 
import re  
import os  
import shutil 
import logging 
import logging.handlers 
import time 
import string

class BaseDAO:
    
    def __init__(self, host, port, database, user, password,logger_f):
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password
        self.logger = logger_f
        self.connect()

    def connect(self):
        self.logger.debug('connect db')
        try:
            self.conn = MySQLdb.connect(host=self.host, port=self.port, db=self.database, user=self.user, passwd=self.password)
        except Exception, e:
            self.logger.error('%s, %s' % (type(e), e))

    def __del__(self):
        self.conn.cursor().close()
        self.conn.close()

    def Close(self):
        self.conn.cursor().close()
        self.conn.close()
    
    def Query(self, sql):
      for _ in range(1):
        try:
            cursor = self.conn.cursor()
            self.logger.debug(sql)
            cursor.execute(sql)
            rows = cursor.fetchall()
            return rows
        except Exception, e:
            self.logger.error('%s' % (sql))
            self.logger.error('%s, %s' % (type(e), e))
        

    def Update(self, sql):
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql)
            self.conn.commit()
            return
        except Exception, e:
            self.logger.error('%s' % (sql))
            self.logger.error('%s, %s' % (type(e), e))

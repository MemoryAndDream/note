# -*- coding: utf-8 -*-
"""
File Name：     db_util
Description :
Author :       meng_zhihao
date：          2018/5/15
"""
if __name__ == '__main__':
    import sys
    sys.path.append('../')
import os,sys,random
import MySQLdb
from MySQLdb.converters import conversions
from settings import DATABASES

class DBUtil(object):
    conv = conversions

    @classmethod
    def _get_cursor_by_rds(self, db_name, RDS):
        db_set = RDS
        self.conv[0] = float
        self.conv[246] = float
        conn = MySQLdb.connect(host=db_set['HOST'], port=int(db_set['PORT']), \
                               user=db_set['USER'], passwd=db_set['PASSWORD'], db=db_name, charset="utf8", conv=self.conv)
        cursor = conn.cursor()
        return (conn, cursor)

    @classmethod
    def get_cursor(self, db_name):
        RDS1 = DATABASES['default']
        return DBUtil._get_cursor_by_rds(db_name, RDS1)

    @classmethod
    def close_cursor(self, conn, cursor):
        cursor.close()
        conn.close()


if __name__ == '__main__':
    sys.path.append('../')
    conn, cursor = DBUtil.get_cursor('web_detect')
    query = 'select * from webpage_hash '
    cursor.execute(query)
    print cursor.fetchall()
    #print cursor.execute(query)
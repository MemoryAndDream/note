# -*- coding: utf-8 -*-
"""
File Name：     chromeHeadless
Description :
Author :       meng_zhihao
date：          2018/7/9
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import getpass
import time
from tools.db_util import DBUtil
from selenium_operate import ChromeOperate
from tools.md5_convert import *
username = getpass.getuser()
import sys
reload(sys)
sys.setdefaultencoding('utf8')
#default_path = r'C:\Users\%s\AppData\Local\Google\Chrome\User Data' % username
default_path = r'D:\User Data'
arguments=[]
arguments.append('headless')
so = ChromeOperate(executable_path=r'C:\Users\Administrator\Desktop\chromedriver.exe',User_data_dir= r'D:\User Data',arguments=arguments)

driver =so.driver
# driver = webdriver.Chrome()
# driver = webdriver.PhantomJS()
time.sleep(5)

time_range = 60*60*14
start_time = time.time()  # url,hash?
print('打开链接')
driver.get('https://www.baidu.com/s?wd=python')
print('打开浏览器')
print(driver.title)

conn, cursor = DBUtil.get_cursor('web_detect')


def row_to_dict(row):
    (hash,value,index_num) = row
    value_dict = {'hash': hash, 'value': value, 'index_num': index_num}
    return value_dict

def find_record(hash):
    query = 'select hash,value,index_num from hash_value where hash=%s'
    cursor.execute(query,(hash,))
    rows =  cursor.fetchall()
    return [row_to_dict(a) for a in rows]

def save_record(hash,value,index=0):
    query = "replace into hash_value(hash,value,index_num) values('%s','%s',%s) "%(hash,value,index)
    print query
    cursor.execute(query)
    conn.commit()

while True:  #需要考虑到网络断开之类的问题
    # 打印网页渲染后的源代码
    infos = so.find_elements_by_xpath('//table[@class="c-table opr-toplist-table"]/tbody//tr')
    for info in infos:
       # print info.text,info.get_attribute("outerHTML")
        rs = info.find_element_by_xpath('.//span/a')
       # print rs.text, rs.get_attribute("outerHTML")
        rs = rs.text
        index = info.find_element_by_xpath('.//td[@class="opr-toplist-right"]').text
        if rs:
            hash = convert_str(rs)
            old_record = find_record(hash)
            if not old_record or old_record[0]['index_num']<int(index):
                save_record (hash,rs,index)


# getElementText {'sessionId': u'2e4f15406514889417f91379ecc5191d', 'id': u'0.5623611823843127-1'}
# 民房墙体抠出百万
# getElementText {'sessionId': u'2e4f15406514889417f91379ecc5191d', 'id': u'0.5623611823843127-2'}
# 70城房价出炉
# getElementText {'sessionId': u'2e4f15406514889417f91379ecc5191d', 'id': u'0.5623611823843127-3'}
# 特朗普认错改口


    if time.time() - start_time > time_range:
        break
    time.sleep(180)
    so.refresh()

so.quit()
cursor.close()
conn.close()



# encoding: utf-8  

""" 
@author: Meng.ZhiHao 
@contact: 312141830@qq.com 
@file: seleniumTest.py 
@time: 2018/1/29 11:30 
"""
import selenium
import os
#使用前需要先关闭原有chrome
#pyinstaller -F -p C:\Users\Administrator\PycharmProjects\onlinetest\seleniumTest C:\Users\Administrator\PycharmProjects\onlinetest\seleniumTest\seleniumTest.py
from  selenium_operate import ChromeOperate
import ConfigParser
import os,sys
exe_path = os.path.dirname(sys.argv[0])

dataconf = ConfigParser.ConfigParser()
if os.path.exists(exe_path+r'\config.txt'):dataconf.read(exe_path+r'\config.txt')
else:dataconf.read(os.path.dirname(__file__)+r'\dist\config.txt')
exec_time = dataconf.get('main','time').strip()
executable_path = dataconf.get('main','executable_path').strip()
print executable_path
import cron_task

def taobao():
    print executable_path
    cop = ChromeOperate('https://fuwu.taobao.com/ser/detail.htm?spm=a1z13.8114203.1234-fwlb.5.66c25acaQRsoGC&service_code=ts-1796606&tracelog=category&scm=1215.1.1.51052018%E3%80%81',executable_path=executable_path)
    #cron_task.timer_task(exec_time)
    #cop.driver.refresh()
    #cop.driver.find_element_by_xpath("//div[@class='tb-sk-btns']/a").click()

def jingdong():
    cop = ChromeOperate('http://miao.item.taobao.com/564003208573.htm?spm=5070.7116889.1996665613.3.iQXafH',executable_path= executable_path)


if __name__ == '__main__':
    taobao()


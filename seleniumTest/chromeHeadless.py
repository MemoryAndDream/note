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
option = webdriver.ChromeOptions()
#option.add_argument('headless')  #
username = getpass.getuser()
#default_path = r'C:\Users\%s\AppData\Local\Google\Chrome\User Data' % username
default_path = r'D:\User Data'
#option.add_argument('--user-data-dir=%s' % default_path)  #设置用户目录的情况用headless才能打开第一个页面，不然要手动输入第一条链接
#option.add_argument("--profile-directory=Profile1")
option.add_argument('google-base-url=%s' % 'https://www.baidu.com/')



driver = webdriver.Chrome(chrome_options=option,executable_path=r'C:\Users\Administrator\Desktop\chromedriver.exe')
# driver = webdriver.Chrome()
# driver = webdriver.PhantomJS()
time.sleep(5)

print('打开链接')
driver.get('https://www.baidu.com/')
driver.save_screenshot(u"首页.png")
print('打开浏览器')
print(driver.title)
driver.find_element_by_id('kw').send_keys(u'测试')  #windows下必须用unicode
driver.find_element_by_id("su").send_keys(Keys.RETURN)
driver.save_screenshot(u"测试.png")
# 打印网页渲染后的源代码
#print driver.page_source
time.sleep(60)
print('关闭')
driver.quit()
print('测试完成')
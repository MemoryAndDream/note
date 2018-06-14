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
from PIL import Image,ImageEnhance
from tools import verify_code_lian_zhong
exe_path = os.path.dirname(sys.argv[0])

dataconf = ConfigParser.ConfigParser()
if os.path.exists(exe_path+r'\config.txt'):dataconf.read(exe_path+r'\config.txt')
else:dataconf.read(os.path.dirname(__file__)+r'\dist\config.txt')
exec_time = dataconf.get('main','time').strip()
executable_path = dataconf.get('main','executable_path').strip()
print executable_path
import cron_task
import json
import time
from selenium.webdriver.common.keys import Keys


def taobao():
    print executable_path
    cop = ChromeOperate('https://fuwu.taobao.com/ser/detail.htm?spm=a1z13.8114203.1234-fwlb.5.66c25acaQRsoGC&service_code=ts-1796606&tracelog=category&scm=1215.1.1.51052018%E3%80%81',executable_path=executable_path)
    #cron_task.timer_task(exec_time)
    #cop.driver.refresh()
    #cop.driver.find_element_by_xpath("//div[@class='tb-sk-btns']/a").click()

def jingdong():
    cop = ChromeOperate('http://miao.item.taobao.com/564003208573.htm?spm=5070.7116889.1996665613.3.iQXafH',executable_path= executable_path)

def get_auth_code(driver,codeEelement):
    '''获取验证码'''
    driver.save_screenshot('login.png')  #截取登录页面
    imgSize = codeEelement.size   #获取验证码图片的大小
    imgLocation = codeEelement.location #获取验证码元素坐标
    rangle = (int(imgLocation['x']),int(imgLocation['y']),int(imgLocation['x'] + imgSize['width']),int(imgLocation['y']+imgSize['height']))  #计算验证码整体坐标
    login = Image.open("login.png")
    frame4=login.crop(rangle)   #截取验证码图片
    frame4.save('authcode.png')
    authcodeImg = Image.open('authcode.png')
    authCodeText = verify_code_lian_zhong.main('vobile123',
         'vobile@123',
         'http://api.fxhyd.cn/appapi.aspx?actionid=captcha&tradeid=1528804539952',
         "http://v1-http-api.jsdama.com/api.php?mod=php&act=upload",
         5,
         5,
         1013,
         '',
        img_path='authcode.png')
    return authCodeText

def verify_code():
    cop = ChromeOperate('https://www.jsdati.com/login',executable_path= executable_path)
    ele = cop.find_element_by_id('login-captcha-img')
    code =   get_auth_code(cop.driver,ele)
    print code
    name_input = cop.find_element_by_name('username')
    psd_input = cop.find_element_by_name('password')
    captcha_input = cop.find_element_by_name('captcha')
    cop.input_words(name_input,'vobile123')
    cop.input_words(psd_input, 'vobile@123')
    cop.input_words(captcha_input, code)

    time.sleep(3)
    captcha_input.send_keys(Keys.ENTER )

    time.sleep(200)


if __name__ == '__main__':
    print verify_code()


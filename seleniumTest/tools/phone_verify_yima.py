# -*- coding: utf-8 -*-
"""
File Name：     phone_verify
Description :
Author :       meng_zhihao
date：          2018/6/11
"""
# 使用易码平台获取手机验证码

import requests
import time
username='mengzaizai'
password='aaaaaa'
class YiMaPhoneVerify(object):
    def __init__(self):
        self.token = self.login()

    def get_phone(self,itemid): #可选字段运营商 指定号码 省市 排除号码段
        data = {}
        data['token']=self.token
        data['excludeno'] ='170.171.180'
#        data['mobile'] = '15504494874'
        url = 'http://api.fxhyd.cn/UserInterface.aspx?action=getmobile'
        return requests.get(url,params=data).text.split('|')[1]

    def get_msg(self,itemid,mobile):
        for i in range(12):
            time.sleep(5)
            url='http://api.fxhyd.cn/UserInterface.aspx?action=getsms&token=%s&itemid=%s&mobile=%s&release=1'%(self.token,itemid,mobile)
            rsp = requests.get(url).text
            if rsp.split('|')[1]:return rsp.split('|')[1]
        return ''

    def login(self):
        data = 'action=login&username=%s&password=%s'%('mengzaizai','aaaaaa')
        rsp = requests.get('http://api.fxhyd.cn/UserInterface.aspx?%s'%data)
        return rsp.text.split('|')[1]

    def release(self,mobile,itemid):
        url =  'http://api.fxhyd.cn/UserInterface.aspx?action=release&token=TOKEN&itemid=%s&mobile=%s'%(itemid,mobile)
        rsp = requests.get(url)
        return rsp.text.split('|')[1]



itemid=160 #大众点评
ym = YiMaPhoneVerify()
mobile = ym.get_phone(itemid)
#请求验证码
print ym.get_msg(itemid,mobile)
ym.release(mobile,itemid)
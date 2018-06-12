# -*- coding: utf-8 -*-
"""
File Name：     phone_verify
Description :
Author :       meng_zhihao
date：          2018/6/11
"""
# 使用易码平台获取手机验证码

import requests

username='mengzaizai'
password='aaaaaa'
class YiMaPhoneVerify(object):
    def __init__(self):
        self.phone= self.get_phone()

    def get_phone(self):
        return

    def get_code(self):
        pass

    def login(self):
        data = 'action=login&username=%s&password=%s'%('mengzaizai','aaaaaa')
        requests.get('http://api.fxhyd.cn/UserInterface.aspx',)
        pass



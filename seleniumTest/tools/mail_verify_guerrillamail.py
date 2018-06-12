# -*- coding: utf-8 -*-
"""
File Name：     mail_verify
Description :
Author :       meng_zhihao
date：          2018/6/11
"""
import requests
import uuid
import time
import json

uuid_str=str(uuid.uuid1())[:4]
timestamp = int(round(time.time() * 1000))
s = requests.Session()
data = {'email_user': 'meng%s'%uuid_str, 'site': 'guerrillamail.com','lang':'zh'}



class mail_verify(object):
    def __init__(self):
        uuid_str = str(uuid.uuid1())[:6]
        self.email_user = 'meng%s'%uuid_str
        self.sess = requests.Session()

    def set_mail(self):
        set_url = 'https://www.guerrillamail.com/ajax.php?f=set_email_user'
        r = self.sess.post(set_url, data=data)
        print r.json()
        return r.json()['alias_error']

    def get_mail(self):
        for i in range(6):
            time.sleep(5)
            timestamp = int(round(time.time() * 1000))
            check_url = 'https://www.guerrillamail.com/ajax.php?f=check_email&seq=1&site=guerrillamail.com&_=%s' % timestamp
            r = self.sess.get(check_url)
            if r.json():
                return r.json()['list'][0]
            return r.json()['list']

    def forget_me(self):
        url = 'https://www.guerrillamail.com/ajax.php?f=forget_me'
        data = {"site":"guerrillamail.com"}
        self.sess.post(url,data)



if __name__ == '__main__':
    m = mail_verify()
    m.set_mail()
    print m.email_user
    m.get_mail()
    m.forget_me()




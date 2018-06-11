# -*- coding: utf-8 -*-
import urllib, urllib2, sys
import ssl
import json
import requests
import pdb
import base64
#每秒查询率QPS是对一个特定的查询服务器在规定时间内所处理流量多少的衡量标准。免费账号不保证qps


def get_accesstoken():
    client_id='KxoUFHYQDbsN9fpcX4DINxgW'
    client_secret ='7PXE7uudCVKn9taWsRpVGlQ4UzhwMO90'
    # client_id 为官网获取的AK， client_secret 为官网获取的SK
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=%s&client_secret=%s'%(client_id,client_secret)
    request = urllib2.Request(host)
    request.add_header('Content-Type', 'application/json; charset=UTF-8')
    response = urllib2.urlopen(request)
    content = response.read()
    if (content):
        print(content)

def api_execte(url,data):
    #opener = urllib2.build_opener()
    #data = urllib.urlencode(data)
    #method = urllib2.Request(url, data)
    #method.add_header('Content-Type', 'application/x-www-form-urlencoded')
    #result = opener.open(method, timeout=10)
    #page_buf = result.read()
    r=requests.post(url,headers={'Content-Type': 'application/x-www-form-urlencoded'},data=data)
    return r.text


#get_accesstoken()
#24.f1f8b953feaac77c470e9229c560ffeb.2592000.1516419148.282335-10563554

def word_in_pic(accessToken):#图片中的文字识别

    url ='https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic?access_token=%s'%accessToken


    print url
    data={}
    #data['url']='http://www.mt30.com/Soft/UploadSoft/201504/2015041803341239.png'#也可以用图片
    #图像数据，base64编码后进行urlencode，要求base64编码和urlencode后大小不超过4M，最短边至少15px，最长边最大4096px,支持jpg/png/bmp格式
    ## 二进制方式打开图文件
    f = open(r'1.jpg', 'rb')
    # 参数image：图像base64编码
    img = base64.b64encode(f.read())
    data['image']=img
    api_execte(url,data)

class BaidDuOcr(object):
    def __init__(self,accessToken=''):
        if accessToken:
            self.accessToken = accessToken
            self.url  ='https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic?access_token=%s'%accessToken


    def ocr_by_url(self,img_url):
        data = {}
        data['url'] = img_url
        return api_execte(self.url, data)


    def ocr_by_file(self, file_path):
        data = {}
        # data['url']='http://www.mt30.com/Soft/UploadSoft/201504/2015041803341239.png'#也可以用图片
        # 图像数据，base64编码后进行urlencode，要求base64编码和urlencode后大小不超过4M，最短边至少15px，最长边最大4096px,支持jpg/png/bmp格式
        ## 二进制方式打开图文件
        f = open(r'%s'%file_path, 'rb')
        # 参数image：图像base64编码
        img = base64.b64encode(f.read())
        data['image'] = img
        return api_execte(self.url, data)

    # 返回{"log_id": 3141525952912134862, "words_result_num": 2, "words_result": [{"words": "编辑短信021354"}, {"words": "发送至1069016399"}]}


if __name__ == '__main__':
   # accessToken = '24.a393e24f84cb3a69108c265bbfca6d19.2592000.1529551040.282335-10563554'
    #word_in_pic(accessToken)
    #get_accesstoken()

    bo = BaidDuOcr('24.a393e24f84cb3a69108c265bbfca6d19.2592000.1529551040.282335-10563554')
    #print bo.ocr_by_file(r'D:\pyproject\mytest\1.jpg')
    print bo.ocr_by_url(r'http://www.mt30.com/Soft/UploadSoft/201504/2015041803341239.png')
# -*- coding: utf-8 -*-
"""
File Name：     md5_convert
Description :
Author :       meng_zhihao
date：          2018/7/17
"""
#字符串md5,用你的字符串代替’字符串’中的内容。


import hashlib

def convert_str(s):
    md5=hashlib.md5(s).hexdigest()

    print(md5)
    return md5

#求文件md5

#文件位置中的路径，请用双反斜杠，

# 如’D:\\abc\\www\\b.msi’ file='[文件位置]’
def convert_file(f):
    md5file=open(file,'rb')
    md5=hashlib.md5(md5file.read()).hexdigest()
    md5file.close()
    print(md5)

if __name__ == '__main__':
    convert_str('测试')
    convert_str('测试')
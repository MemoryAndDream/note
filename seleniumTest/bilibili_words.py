# -*- coding: utf-8 -*-
"""
File Name：     bilibili_words
Description : bilibili 弹幕收集器
Author :       meng_zhihao
date：          2018/7/23
"""
from selenium_operate import ChromeOperate
import sys
reload(sys)
sys.setdefaultencoding('utf8')
def main(needLogin=False):
    arguments=[]
    if not needLogin:
        #arguments.append('headless')
        pass
    so = ChromeOperate(executable_path=r'C:\Users\Administrator\Desktop\chromedriver.exe',User_data_dir= r'D:\User Data',arguments=arguments)
    driver = so.driver
    driver.get('https://www.bilibili.com/')



if __name__ == '__main__':
    if len(sys.argv)==2:
        stype = sys.argv[1]
        if stype=='login': #第一次需要先带界面登录
            main(True)
            sys.exit()
    main()


'''目前的智能推荐关于搜索的比较多，而关于二次元的就比较少了 歌曲 小说 动漫 漫画 购物 智能推荐做到位的话会给人很多方便

推荐一种是基于人，另一种是基于目标本身绘制关系图  基于人的不好弄，

'''
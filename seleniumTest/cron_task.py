# encoding: utf-8  

""" 
@author: Meng.ZhiHao 
@contact: 312141830@qq.com 
@file: cron_task.py 
@time: 2018/1/29 13:35 
"""
import time
import datetime
def timer_task(time_str):
    while True:
        time.sleep(0.5)
        exec_time = datetime.datetime.strptime(time_str,'%Y-%m-%d %H:%M:%S')
        if datetime.datetime.now() > exec_time:
            print 'exec',str(datetime.datetime.now())
            break


if __name__ == '__main__':
    timer_task('2018-01-29 14:02:00')
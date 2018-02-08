#coding=utf-8
#通过查询数据库得出最优选择，采用e贪心算法进行尝试，初始0.3概率均匀尝试加倍或不加倍
#目前是完全利用，不尝试
import time
from db_connect import *
import logging
from time import strftime, localtime
import ConfigParser
import random


class MechineChoice:
    def __init__(self,logger,tryrate,decayRadio,isEqualityTry=False):

        pass
        self.tryrate=tryrate
        self.logger = logger
        dbconf = ConfigParser.ConfigParser()
        dbconf.read('etc/db.conf')
        self.con=self.GetCon('data_db',dbconf,logger)
        self.decayRadio=decayRadio
        self.isEqualityTry=isEqualityTry

    def getChoice(self,mechineScore,humanChoice):#查询同一情况下不同选择的收益率，选最大收益率的选择  需要加尝试机制
        mechineChoice=1

        if self.isEqualityTry:
            if random.random()<1:  #e 概率均匀尝试 后面可以开小一点#当人选择好的策略时，尝试多肯定会输钱  实战就算尝试也要用soft方法
                #更优秀的尝试应该是根据胜率*收益率来查
                if random.random()<0.5:
                    mechineChoice=1
                else:
                    mechineChoice=2
                return mechineChoice

        else:
            #非均匀尝试  根据胜率来尝试 初始胜率设置是个问题  初始胜率需要专家信息  最好干脆就是傻瓜策略下的计算值，不然是0就不去试验了
            #觉得可能会赢的策略自己加几条进去
            tryrate=self.tryrate
            if random.random() < tryrate:  # 这个数字的大小决定了尝试的热情 对手越死板越不应该尝试
                # 更优秀的尝试应该是根据胜率*收益率来查
                if random.random() < self.calculateChioceRate(mechineScore,humanChoice,1):
                    mechineChoice = 1
                else:
                    mechineChoice = 2
                return mechineChoice


        resultTuple=self.con.Query('SELECT mechineChoice,\
        averageEarnings from coreDB where mechineScore =%s and humanChoice =%s'%(mechineScore,humanChoice))
        result=sorted(resultTuple,key=lambda d: d[1],reverse=True)#降序排列
        pass
        mechineChoice= result[0][0]

        return mechineChoice

    def updateDateBase(self,ms,hc,mc,result,isbest):##更新收益  反馈对比结果  isbest=-1/0/1 负，平，胜
        pass
        #self.con.Update('INSERT into coreDB(mechineScore,humanChoice,mechineChoice) values (%s,%s,%s)'%(ms,hc,mc))
        count=self.con.Query('SELECT averageEarnings,eventCount from coreDB\
         where mechineScore =%s and humanChoice =%s and mechineChoice=%s'%(ms,hc,mc))[0][1]

        averageEarnings= self.con.Query('SELECT averageEarnings,eventCount from coreDB\
         where mechineScore =%s and humanChoice =%s and mechineChoice=%s'%(ms,hc,mc))[0][0]

        choiceBestCount=self.con.Query('SELECT choiceBestCount from coreDB\
         where mechineScore =%s and humanChoice =%s and mechineChoice=%s'%(ms,hc,mc))[0][0]

        otherBestCount = self.con.Query('SELECT choiceBestCount,ifBestEarn from coreDB\
            where mechineScore =%s and humanChoice =%s and mechineChoice=%s' % (ms, hc, (3 - mc)))[0][0]

        newAverageEarnings=(count*averageEarnings+result)*1.0/(count+1)
        newCount=count+1
        if isbest == 1:
            self.con.Update('UPDATE coreDB SET averageEarnings=%s,eventCount=%s,choiceBestCount=%s \
            where mechineScore =%s and humanChoice =%s and mechineChoice=%s ' % (
                newAverageEarnings,newCount,choiceBestCount+isbest,ms, hc, mc))
            #反馈，输了两边都要反馈,平局只修正一边
            self.con.Update('UPDATE coreDB SET choiceBestCount=%s \
                where mechineScore =%s and humanChoice =%s and mechineChoice=%s ' % (
                otherBestCount + 1-isbest, ms, hc, (3-mc)))

        if isbest == -1:
            self.con.Update('UPDATE coreDB SET averageEarnings=%s,eventCount=%s,choiceBestCount=%s \
            where mechineScore =%s and humanChoice =%s and mechineChoice=%s ' % (
                newAverageEarnings,newCount,choiceBestCount,ms, hc, mc))
            #反馈，输了两边都要反馈,平局只修正一边
            self.con.Update('UPDATE coreDB SET choiceBestCount=%s \
                where mechineScore =%s and humanChoice =%s and mechineChoice=%s ' % (
                otherBestCount -isbest, ms, hc, (3-mc)))

        if isbest==0:
            self.con.Update('UPDATE coreDB SET averageEarnings=%s,eventCount=%s,choiceBestCount=%s \
            where mechineScore =%s and humanChoice =%s and mechineChoice=%s ' % (
                newAverageEarnings,newCount,choiceBestCount,ms, hc, mc))
            #反馈，输赢都要反馈,平局两边都不加，两边都不算胜利，不然影响后面计算
            self.con.Update('UPDATE coreDB SET choiceBestCount=%s \
                where mechineScore =%s and humanChoice =%s and mechineChoice=%s ' % (
                otherBestCount , ms, hc, (3-mc)))
        self.allHistoryDataDecay()  #这样搞只有当修改时才是(x+1)*0.9 其他时候都是x*0.9

        return

    def calculateChioceRate(self,mechineScore,humanChoice,mechineChoice):#计算应该选择某种尝试的概率，必输的就不尝试了
        ms,hc,mc=mechineScore,humanChoice,mechineChoice
        choiceBestCount = self.con.Query('SELECT choiceBestCount,ifBestEarn from coreDB\
            where mechineScore =%s and humanChoice =%s and mechineChoice=%s' % (ms, hc, mc))[0][0]
        ifBestEarn = self.con.Query('SELECT choiceBestCount,ifBestEarn from coreDB\
            where mechineScore =%s and humanChoice =%s and mechineChoice=%s' % (ms, hc, mc))[0][1]
        eventCount= self.con.Query('SELECT averageEarnings,eventCount from coreDB\
         where mechineScore =%s and humanChoice =%s and mechineChoice=%s'%(ms,hc,mc))[0][1]

        otherEventCount = self.con.Query('SELECT averageEarnings,eventCount from coreDB\
            where mechineScore =%s and humanChoice =%s and mechineChoice=%s' % (ms, hc, 3-mc))[0][1]

        otherBestCount=self.con.Query('SELECT choiceBestCount,ifBestEarn from coreDB\
            where mechineScore =%s and humanChoice =%s and mechineChoice=%s' % (ms, hc, (3-mc)))[0][0]
        otherIfBestEarn = self.con.Query('SELECT choiceBestCount,ifBestEarn from coreDB\
            where mechineScore =%s and humanChoice =%s and mechineChoice=%s' % (ms, hc, (3-mc)))[0][1]#

        if choiceBestCount * ifBestEarn + otherBestCount * otherIfBestEarn != 0:
            chioceRate = choiceBestCount * ifBestEarn*1.0 / (choiceBestCount * ifBestEarn + otherBestCount * otherIfBestEarn)  # 这里因为输赢不翻倍，选择翻倍和不翻倍规避收益没区别
        else:  # 没有数据时不能通过胜率判断尝试概率
            chioceRate = 0.5
        #多赢一倍  少输也是一倍  不像彩票输了2块 赢了500w
        return chioceRate

    def initDateBase(self,ms,hc,mc,averageEarnings,eventCount,choiceBestCount,ifBestEarn):
        pass
        self.con.Update('INSERT into coreDB(mechineScore,humanChoice,\
        mechineChoice,averageEarnings,eventCount,choiceBestCount,ifBestEarn) \
        values (%s,%s,%s,%s,%s,%s,%s)'%(ms,hc,mc,averageEarnings,eventCount,choiceBestCount,ifBestEarn))
        return#如果设置成0就永远不会尝试了

    def allHistoryDataDecay(self):#衰变率 1不衰变
        ratio=self.decayRadio
        pass
        if ratio!=1:
            self.con.Update('UPDATE coreDB SET eventCount=eventCount*%s,choiceBestCount=choiceBestCount*%s;'%(ratio,ratio))
        return

    def singleRecordDecay(self, ms,hc,mc,isbest):
        if isbest==-1:#结果是差选项再衰变
            pass
            ratio=self.decayRadi


            self.con.Update( 'UPDATE coreDB SET eventCount=eventCount*%s,choiceBestCount=choiceBestCount*%s \
            where mechineScore =%s and humanChoice =%s and mechineChoice=%s;'\
                             % (ratio, ratio,ms,hc,mc))

        return

    def emptyTable(self):
        pass
        self.con.Update('DELETE from coreDB;')
        return


    def GetCon(self, DBname, dbconf, logger):
        host = dbconf.get(DBname, 'host')
        port = dbconf.getint(DBname, 'port')
        name = dbconf.get(DBname, 'name')
        user = dbconf.get(DBname, 'user')
        password = dbconf.get(DBname, 'pass')
        time.sleep(0.2)
        con = BaseDAO(host, port, name, user, password, logger)
        return con


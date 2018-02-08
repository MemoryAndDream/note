#coding=utf-8
#游戏主程序
import random
from mechineChoice  import *
def getRand():
    return int(random.random()*9)+1
def calculateResult(hs,ms,hc,mc):#得到的是电脑的收益
    if(hs>ms):
        return -1*hc*mc
    if(hs<ms):
        return 1*hc*mc
    if(hs==ms):
        return 0



def run(mechineChoice):

    #generate humanScore(hs 1-9) mechineScore(ms 1-9)
    hs=1
    ms=1
    hs=getRand()
    ms=getRand()
    #ms=1
    print '你的牌大小',hs
    pass
    #input humanChoice
    hc='y'#全加倍策略
    if hs>4:#5加倍策略
        hc='y'
    else:
        hc='n'
   # hc=raw_input('是否加倍 y/n:')#输入法

    if hc == 'y':
        print '你选择加倍'
        hc=2
    elif hc == 'n':
        print '你选择不加倍'
        hc=1
    else:
        hc=1

    pass
    #calculate mechineChoice
    #根据当前最优策略选择电脑的策略并更新数据库
    mc=mechineChoice.getChoice(ms,hc)
    #mc = int(random.random()*2)+1

    if mc==2:
        print '电脑加倍'
    if mc ==1:
        print '电脑不加倍'
    print '电脑分数',ms
#    result=calculateResult(hs,ms,hc,mc)
    result=calculateResult(hs,ms,hc,mc) #加倍或弃权模型

    isbest=0
    #判断是否是最优选项
    if calculateResult(hs,ms,hc,mc)>calculateResult(hs,ms,hc,(3-mc)): #系统收益越小  平局是个问题 必须加等于，否则平局也会导致极端情况被视为best
        print 'ai做出了正确的选择'
        isbest=1

    if calculateResult(hs, ms, hc, mc) == calculateResult(hs, ms, hc,
                                                         (3 - mc)):  # 系统收益越小  平局是个问题 必须加等于，否则平局也会导致极端情况被视为best
        isbest = 0

    if calculateResult(hs, ms, hc, mc) < calculateResult(hs, ms, hc,
                                                         (3 - mc)):  # 系统收益越小  平局是个问题 必须加等于，否则平局也会导致极端情况被视为best
        isbest = -1

    mechineChoice.updateDateBase(ms,hc,mc,result,isbest)
    return result
def buildDataBase(mechineChoice):
#建立初始的数据库
#后面重新搞可以用UPDATE coreDB SET averageEarnings =0 where 1=1
#UPDATE coreDB SET eventCount =0 where 1=1
    pass
    mechineChoice.emptyTable()  #清空数据库
    for ms in range(1,10,1):#1-9
        for hc in range(1,3,1):
            for mc in range(1,3,1):#initDateBase(self,ms,hc,mc,     averageEarnings,eventCount,choiceBestCount,   ifBestEarn)
                ifBestEarn=abs(calculateResult(1,2,hc,mc)- calculateResult(1,2,hc,3-mc))#2*2-2-1  1*2-1-1
                if ms==9 and mc==1:
                    mechineChoice.initDateBase(ms , hc , mc , 1,10, 0, ifBestEarn)#设置极端情况 设置极端一点就不会选了
                elif ms==1 and mc == 2:
                    mechineChoice.initDateBase(ms , hc , mc , -4, 10, 0, ifBestEarn)
                else:
                    mechineChoice.initDateBase(ms, hc, mc, 1,1,1,ifBestEarn)#以后修正极端情况
    #exit()

def main():
    year = strftime("%Y", localtime())
    mon = strftime("%m", localtime())
    day = strftime("%d", localtime())
    logname = 'var/log/' + year + '-' + mon + '-' + day + '.log'
    # logname='1.log'
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        filename=logname,
                        filemode='a')  # a是追加，w是覆盖
    logger = logging.getLogger(logname)


    tryrate=0.5 #尝试比例
    a= MechineChoice(logger,tryrate,0.9)  #每次实战衰变  0.8 十次衰变到10分之一 0.9 10次到3份子一  (x+1) *0.9  x=9时稳定
    #buildDataBase(a)#初始化数据库的时候用一次
    count=0
    money=30
    firstmoney=money
    logger.info('ai尝试比例:'+str(tryrate))
    logger.info('开局资金:'+str(firstmoney))
    largestmoney=money  #常量不是引用
    while money >0:
        if money>largestmoney:
            largestmoney=money
        print '第',count,'局'
        print '你的钱数：',money
        money =money-run(a)
        count+=1
    print '你坚持了',count,'亏光前最高收益',largestmoney-firstmoney
    logger.info('你坚持了'+str(count)+'亏光前最高收益'+str(largestmoney-firstmoney))

def test():#专家数据修正
    pass

def init():#初始化数据库并算一波专家数据  这里最好均匀尝试
    year = strftime("%Y", localtime())
    mon = strftime("%m", localtime())
    day = strftime("%d", localtime())
    logname = 'var/log/' + year + '-' + mon + '-' + day + '.log'
    # logname='1.log'
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        filename=logname,
                        filemode='a')  # a是追加，w是覆盖
    logger = logging.getLogger(logname)


    tryrate=1 #尝试比例
    a= MechineChoice(logger,tryrate,1,True)  #不衰变 均匀尝试
    buildDataBase(a)#初始化数据库的时候用一次
    count=0
    money=100
    firstmoney=money
    logger.info('ai尝试比例:'+str(tryrate))
    logger.info('开局资金:'+str(firstmoney))
    largestmoney=money  #常量不是引用
    while count <500:
        if money>largestmoney:
            largestmoney=money
        print '第',count,'局'
        print '你的钱数：',money
        money =money-run(a)
        count+=1
    print '你坚持了',count,'亏光前最高收益',largestmoney-firstmoney
    logger.info('你坚持了'+str(count)+'亏光前最高收益'+str(largestmoney-firstmoney))


if __name__ == '__main__':#这么写是为了被导入时不会乱执行
    main()
    #init()

#选择永远加倍的策略 随着训练的加深，越来越快输光 第二把400+  第三把183 第四把313  第五把274 第六把102 第七把572  减小尝试概率
#尝试概率0.2时101,182，
#即对于全加倍策略，4以上就该加倍    针对对方策略不同，应采取的策略也不同

#人采用>5策略 尝试多了肯定输钱
#两个机器互相搞就是先后顺序的博弈了

#有些策略是不应该去尝试的，比如9的时候就应该加倍，是否加倍要看的是最优选择的概率而不是收益概率！  胜率（相对于其他选择）*收益率（获胜能收益）


#下一步是研究实战如何修正专家数据，增加灵活度  比如修正初始专家数据（用几百轮训练出的平均值）的count后作为初始值
#并换模型测试  不能用博弈论来思考，因为对手的行为不同 最优策略是不同的，如果对手傻逼就应该激进
#平局的bestchoice收入计算错误 平局都不加

#计算时整数除法要*1.0！或者一步步debug

#增加历史数据修正  修正次数为double best和eventcount等比例修正   根据衰变定律 衰变速度正比于当前重量，因此每过一次衰变（总次数或那个状态的次数
# ，如果用总次数的话修正的太快了，专家次数容易下降太快，也许可以看情况衰变，比如连续犯错了再衰变# ）乘以固定倍率（固定倍率比较符合衰变定律比如9/10，越修正越小是不科学的）
#机器学习的原则是随机应变  对于这个模型，很多东西是多余的，因为克制性几乎没有  战术针对是根据个性来针对的，而这个模型专家策略比实战情况重要

#coding:UTF-8
import datetime

dt1 = datetime.datetime(2020,3,15)
baseday = datetime.datetime(2019,12,31)

interval = dt1 - baseday
numday = interval.days + 43830
print(interval,numday)


'''
def dateC(dates):#定义转化日期戳的函数,dates为日期戳
    delta=datetime.timedelta(days=dates)
    today=datetime.datetime.strptime('1899-12-30','%Y-%m-%d')+delta#将1899-12-30转化为可以计算的时间格式并加上要转化的日期戳
    return datetime.datetime.strftime(today,'%Y-%m-%d')#制定输出日期的格式
    
a = dateC(numday)
print(a)
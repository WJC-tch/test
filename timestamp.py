#coding:UTF-8
 
import time
from datetime import date,datetime,timedelta
import xlrd
import openpyxl

localtime = time.localtime(time.time()) 
today_Year = localtime.tm_year
today_Month = localtime.tm_mon
today_Day = localtime.tm_mday
today_time = time.strftime("%H:%M", time.localtime())
print (localtime, today_Year, today_Month, today_Day, today_time)

dt1 = datetime(today_Year,today_Month,today_Day)
baseday = datetime(2019,12,31)

interval = dt1 - baseday
num_day = interval.days + 43830

'''#Test part
def dateC(dates):#定义转化日期戳的函数,dates为日期戳
    delta=timedelta(days=dates)
    today=datetime.strptime('1899-12-30','%Y-%m-%d')+delta#将1899-12-30转化为可以计算的时间格式并加上要转化的日期戳
    return datetime.strftime(today,'%Y-%m-%d')#制定输出日期的格式
    
a = dateC(num_day)
print(a)'''

path = r'C:\Users\j02wu\Desktop\Gift4TimeSheet\TSE_FOLDERNew\TSE_900238.xlsm'
excel_Read= xlrd.open_workbook(path)
table = excel_Read.sheet_by_name('TimeSheet')
day_col = table.col_values(15)
time_ColPos = 70
for day in day_col[70:]:
    time_ColPos = time_ColPos+1
    if num_day == day:
        print("Yes")
        break       
print(time_ColPos)

#Titel_row = table.row_values(69) way to find row of start. Easy way is x col
excel_write = openpyxl.load_workbook(path)
table_write = excel_write['TimeSheet']
table_write.cell(time_ColPos, 24, today_time)
excel_write.save(path)
        

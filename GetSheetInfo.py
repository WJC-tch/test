import xlrd

path = r'C:\Users\j02wu\Desktop\Gift4TimeSheet\TSE_FOLDERNew\TSE_900238.xlsm'
excel= xlrd.open_workbook(path)

table = excel.sheet_by_name('TimeSheet')

rows_num = table.nrows

day_col = table.col_values(15)

print(day_col)
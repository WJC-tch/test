import xlwings as xw


path = r'C:\Users\jattc\Desktop\Gift4TimeSheet\TSE_FOLDERNew\TSE_900238.xlsm'

wb = xw.Book(path)

TSheet = wb.sheets['TimeSheet']

sht.range('X142').value="9:30"
import os


# if 10 in range(5):
#     print(True)

filename = 'MonthlyReports\expedia_report_monthly_march_2018.xlsx'


# # year = int(''.join(list(filter(str.isdigit, filename))))
# # print(year)

# # month = 4
# # print(len(str(12345)))

# with open("file.lst", "r") as lst_file:
#     if os.stat("file.lst").st_size != 0: 
#         contents = lst_file.read()
#         if filename in contents:
#             print("File '{}' has been already processed".format(filename))
#             raise Exception("duplicate error")
#         else: pass
#     else: pass



# import openpyxl

# path = str(input('xlsx path: '))

# wb = openpyxl.load_workbook(path)
# ws = wb.worksheets

# print(ws)

# print(filename.split("\\")[1])

# from checkFile import checkFile
# month, val, year = checkFile(filename) 
# date_obj = [month, val, year]
# reg_date_format = "{}-{}".format(date_obj[0][:3], year)
# print(reg_date_format)

# from checkFile import checkFile
# from summaryReport import summaryReport
# month, year = checkFile(filename) 
# date_obj = [month, year]
# summaryReport(filename, date_obj)

from checkFile import checkFile
from vocReport import vocReport
month, year = checkFile(filename) 
date_obj = [month, year]
vocReport(filename, date_obj)
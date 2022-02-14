import openpyxl 
import logging as lg
from datetime import date

lg.basicConfig(filename='MonthlyReportsAccessLog.log',format='%(asctime)s %(message)s', level=lg.DEBUG)
lg.info('Read-Only Request Initiated')

month = input("Month:").lower()
year = input("Year:").lower()
wb = openpyxl.load_workbook("MonthlyReports/expedia_report_monthly_{}_{}.xlsx".format(month, year))
ws = wb['Summary Rolling MoM']
print(type(ws['A'][4].value))

# def getRequest(month, year):
#     wb = openpyxl.load_workbook("MonthlyReports/expedia_report_monthly_{}_{}.xlsx".format(month, year))
#     ws = wb['Summary Rolling MoM']
#     labels = ['Month, Year']
#     values = ['{},{}'.format(month, year)]
#     # get labels
#     for cell in ws['1']:
#         if cell.value is not None:
#             labels.append(cell.value)
#     for row in ws.iter_rows(30):
#         # search rows for labels and requested month 
#         for cell in row:
#             # get values
#             if cell.value is None:
#                 pass
#             if date(cell.value) == date(year,month):
#                 for data in ws.iter_col(row):
#                     if data.value is not None:
#                         values.append(data.value)
#             else:
#                 pass
#     zippedInfo = zip(labels, values)
#     lg.info('Information Retrieved')
#     return labels #zippedInfo

# def printRequest(zippedData):
#     dict = dict(zippedData)
#     for item in dict:
#         print('{}: {}'.format(item[0], item[1]))
#     return lg.info('Information Printed')

#     # checking if file exists; error below
#     if wb:
#         # checking if sheet with needed info exists; error below
#         for sheet in wb:
#             if sheet.title == "Summary Rolling MoM":
#                 headers = []
#                 values = []
#                 for row in sheet:
#                     # if rowj
#                     for column in row:
#                         cell_coordinates = (column.row, column.column)
#                         return 
#             elif sheet.title == "Summary Rolling MoM" not in wb:
#                 lg.error("Error: Data sheet 'Summary Rolling MoM' does not exist. Check file.")
#             else:
#                 continue
#     else:
#         lg.error("Error: Requested file does not exist. Check dates and file formatting.")

# # print("Calls Offered: {}".format())
# # print("Abandon after 30s: {}".format())
# # print("FCR: {}".format())
# # print("DSAT: {}".format())
# # print("CSAT: {}".format())


# lg.info('Request Sent')
# zipped = getRequest(month,year)
# printRequest(zipped)
# lg.info('Request Complete')

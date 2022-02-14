import openpyxl 
import logging as lg
# import datetime

# dateObject = datetime.datetime.strptime('1-2018', '%m-%Y')
# print(dateObject)


# initiate log
lg.basicConfig(filename='MonthlyReportsAccessLog.log',format='%(asctime)s %(message)s', level=lg.DEBUG)
lg.info('Request Initiated')

# input monthly report request
month = input("Month:").lower()
year = input("Year:")
wb = openpyxl.load_workbook("MonthlyReports/expedia_report_monthly_{}_{}.xlsx".format(month, year))
ws = wb['Summary Rolling MoM']

# function to gather data
def getRequest(month, year):
    wb = openpyxl.load_workbook("MonthlyReports/expedia_report_monthly_{}_{}.xlsx".format(month, year))
    ws = wb['Summary Rolling MoM']
    dateStr = '{},{}'.format(month, year)
    labels = ['Month, Year']
    values = [dateStr]
    # get labels
    for cell in ws['1']:
        if cell.value is not None:
            labels.append(cell.value)
        else:
            pass
    for row in ws.iter_rows(30):
        # search rows for labels and requested month 
        for cell in row:
            # get values
            if cell.value is None:
                pass
            elif cell.value.strftime("%B, %Y") == dateStr:
                for data in ws.iter_col(row):
                    if data.value is not None:
                        values.append(data.value)
            else:
                pass
    zipped = zip(labels, values)
    lg.info('Information Retrieved')
    return print(dict(zipped))

# function to print data
def printRequest(zippedData):
    data = dict(zippedData)
    for item in data:
        print('{}: {}'.format(item[0], item[1]))
    return lg.info('Information Printed')


lg.info('Request Sent')
zipped = getRequest(month,year)
printRequest(zipped)
lg.info('Request Complete')

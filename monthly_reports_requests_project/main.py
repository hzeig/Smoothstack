import openpyxl 
import logging as lg
import datetime


log_format = '%(asctime)s %(message)s'

# initiate log
lg.basicConfig(
    filename = 'MonthlyReportsAccessLog.log',
    format = log_format, 
    level = lg.DEBUG
    )

def getReport(month, year):
    # log request
    lg.info('Request Initiated')

    # input monthly report request
    dateStr = '{}-{}'.format(month[0:3], year)
    lg.info('Date Input: {}'.format(dateStr))

    wb = openpyxl.load_workbook("MonthlyReports/expedia_report_monthly_{}_{}.xlsx".format(month, year))
    ws = wb['Summary Rolling MoM']
    lg.info('Workbook Activated')

    labels = ['Month, Year']
    values = ['{},{}'.format(month, year)]
    # get labels
    for cell in ws['1']:
        if cell.value is not None:
            labels.append(cell.value)
        else:
            pass
    for row in ws.iter_rows(min_row=2, max_row=30, min_col=1, max_col=30):
        # # search rows for labels and requested month 
        for cell in row:
            # get values
            if cell.value is not None and str(cell.value).lower() == dateStr:
                for data in ws[row]:
                    if data.value is not None:
                        values.append(data.value)
            else:
                pass
    zipped = zip(labels, values)
    lg.info('Information Retrieved')

    data = dict(zipped)
    for key, value in data.items():
        print('{}: {}'.format(key, value))
    lg.info('Information Printed')
    lg.info('Request Complete')


month = input("Enter month name: (i.e. January)").lower()
year = input("Enter year: (i.e. 2014)")
getReport(month, year)

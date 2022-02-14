import pandas as pd
import logging as lg
# import openpyxl 

month = input("Month:").lower()
year = input("Year:").lower()

lg.basicConfig(filename='monthly_reports_requests_project/MonthlyReportsAccessLog.log',encoding='utf-8',format='%(asctime)s %(message)s', level=lg.DEBUG)
# lg.debug('This message should go to the log file')
# lg.info('So should this')
# lg.warning('And this, too')
# lg.error('And non-ASCII stuff, too, like Øresund and Malmö')

def monthRequest(month, year):
    data = pd.read_csv("monthly_reports_requests_project/MonthlyReports/expedia_report_monthly_{}_{}.xlsx".format(month, year))
    print(data.head())

monthRequest(month, year)
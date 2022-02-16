import pandas as pd
import logging as lg
import datetime


log_format = '%(asctime)s %(message)s'
log_name = 'MonthlyReportsAccessLog.log'

# initiate log
lg.basicConfig(
    filename = log_name,
    format = log_format, 
    level = lg.DEBUG
    )

def getReport(month, year):
    # log request
    lg.info('Request Initiated')

    # input monthly report request
    # date_str = '{},{}'.format(month, year)
    datetime_obj = datetime.datetime.strptime(month+"-"+year, "%B-%Y")
    lg.info('Date Requested: {}'.format(datetime_obj))

    filename = "MonthlyReports/expedia_report_monthly_{}_{}.xlsx".format(month, year)
    lg.debug('Opening file {}'.format(filename))

    report_df = pd.read_excel(
        filename, 
        sheet_name="Summary Rolling MoM",
        engine="openpyxl"
        )
    lg.info('File opened')


    lg.debug('Formatting to Pandas DataFrame')
    labels = [column for column in report_df.columns if column[:7] != 'Unnamed:']
    datein_df = report_df[report_df.eq(datetime_obj).any(1)].dropna(1)

    print(datein_df)
    
    # final_df = 

    lg.info('Information Printed')
    print("Report for {}, {}:".format(month, year))
    # print(final_df)
    lg.info('Request Complete')


month = input("Enter month name (i.e. January):").lower()
year = input("Enter year (i.e. 2018):")
getReport(month, year)

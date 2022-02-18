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


    lg.debug('Collecting Report Features')
    # Collecting item labels, excluding headers 'Unnamed: #'
    labels = [column for column in report_df.columns if column[0] != 'U'] 
    
    lg.info('Finding Column with Datetime Object')
    date_col = report_df.dtypes[report_df.dtypes == object]
    col_name = list(date_col.index)
    dates_df = pd.to_date_time(report_df[col_name])

    lg.info('Searching Datetime Column for Requested Date')
    for name, item in dates_df.iterrows():
        print(item.dt.month)
    
    # for index in range(dates_df.shape[0]):            
    #     item = dates_df.iloc[index,:]
    #     print(type(item))
    #     print(item)
        #     print(item)
        #     # if item.month == month:
        #         # values = report_df.iloc[:,index]
        # else:
            # pass
    

   # print(values)
    # condition = [item for item in dates_df if item.month == datetime_obj]
    # report_df.loc[]
            # if item.month == month and item.year == year:
            #     row = item.index
            
    # print(row)

        # else:
        #     values = report_df[[labels]][i]
        #     return values



    lg.debug('Collecting Report Statistics')
    datein_df = report_df[report_df.eq(datetime_obj).any(1)].dropna(1)

    
    # final_df = 

    lg.info('Information Printed')
    # print("Report for {}, {}:".format(month, year))
    # print(final_df)
    lg.info('Request Complete')


month = input("Enter month name (i.e. January):").lower()
year = input("Enter year (i.e. 2018):")
getReport(month, year)

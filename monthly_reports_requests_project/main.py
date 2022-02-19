import os
import pandas
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

########################### REPORT REQUEST FUNCTIONS #######################


#### TO DO (info and debug log for everything)
# Check file formatting --> if incorrect raise exception 
# Open or create file.lst
# Check if file in file.lst --> if yes, skip and message to log; if no, proceed
# Get file month and year data (datetime or string?)
# Run last weekend code on first tab
#   a. collect labels and values 
#   b. print report in separate report file (open automatically if possible)
# Run this weekend code on second tab
#   a. pull month column
#       - search first by datetime, then by string
#       - if more than one month exists, check for year (if no year, raise formatting error)
#   b. 
# Append file name to file.lst


def getInfo(filename):
    lg.info('Request Initiated')

    month_dict = {
        "January":  1,
        "February": 2,
        "March":    3,
        "April":    4,
        "May":      5,
        "June":     6,
        "July":     7,
        "August":   8,
        "September":9,
        "October":  10,
        "November": 11,
        "December": 12
    }

    
    # check file formatting
    accepted_format = "MonthlyReports/expedia_report_monthly_*.xlsx"
    # # accepted_format = accepted_format.format(month=[x for x in month_dict.keys], year=)
    # if filename == accepted_format:
    #     print(True)
    # else:


    # check if file in file.lst
#     with open("file.lst", 'a') as lst_file:
#         os.system(lst_file)
#         contents = lst_file.read()
#         if file in contents:
#             lg.debug("File '{}' has been already processed".format(filename))
#             break

#     # input monthly report request
#     # date_str = '{},{}'.format(month, year)
#     datetime_obj = datetime.datetime.strptime(month+"-"+year, "%B-%Y")
#     lg.info('Date Requested: {}'.format(datetime_obj))

#     # list of processed files
#     # file_lst =  

#     # filename = "MonthlyReports/expedia_report_monthly_{}_{}.xlsx".format(month, year)
#     # lg.debug('Opening file {}'.format(filename))

#     report_df = pd.read_excel(
#         filename, 
#         sheet_name="Summary Rolling MoM",
#         engine="openpyxl"
#         )
#     lg.info('File opened')


#     lg.debug('Collecting Report Features')
#     # Collecting item labels, excluding headers 'Unnamed: #'
#     labels = [column for column in report_df.columns if column[0] != 'U'] 
    
#     lg.info('Finding Column with Datetime Object')
#     date_col = report_df.dtypes[report_df.dtypes == object]
#     col_name = list(date_col.index)
#     dates_df = pd.to_date_time(report_df[col_name])

#     lg.info('Searching Datetime Column for Requested Date')
#     for name, item in dates_df.iterrows():
#         print(item.dt.month)
    
#     # for index in range(dates_df.shape[0]):            
#     #     item = dates_df.iloc[index,:]
#     #     print(type(item))
#     #     print(item)
#         #     print(item)
#         #     # if item.month == month:
#         #         # values = report_df.iloc[:,index]
#         # else:
#             # pass
    

#    # print(values)
#     # condition = [item for item in dates_df if item.month == datetime_obj]
#     # report_df.loc[]
#             # if item.month == month and item.year == year:
#             #     row = item.index
            
#     # print(row)

#         # else:
#         #     values = report_df[[labels]][i]
#         #     return values



#     # lg.debug('Collecting Report Statistics')
#     # datein_df = report_df[report_df.eq(datetime_obj).any(1)].dropna(1)

    
#     # final_df = 

#     lg.info('Information Printed')
#     # print("Report for {}, {}:".format(month, year))
#     # print(final_df)
#     lg.info('Request Complete')


###################### REPORT REQUEST PROGRAM ##################################

lg.info("Request Initiated")
directory = "MonthlyReports"

request_ask = input("Request a specific file? [y/[n]]").lower()
if request_ask == 'y' or request_ask == 'yes':
    filename = input("Full file name:") 
    lg.info("Specific Report Request for File: {}".format(file))
    print("Requesting report for file: {}".format(file))
    file = os.path.join(directory, filename)
    if os.path.isfile(file):
        getInfo(file)
# Create general report for 'no' or Enter
elif request_ask == 'n' or request_ask == 'no' or request_ask == '': 
    lg.info("Exhaustive Report Request for Reports in {}".format(directory))
    print("Requesting Exhaustive Report")
    for filename in os.listdir(directory):
        file = os.path.join(directory, filename)
        if os.path.isfile(file):
            getInfo(file)
# Ask again if other input
else:
    Exception("Input is Incorrect. Try again.") 
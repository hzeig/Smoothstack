from distutils.log import error
import logging as lg
import os
import shutil
import pandas as pd
import openpyxl
import datetime
from summaryReport import summaryReport
from promoterReport import promoterReport



log_format = '%(asctime)s %(message)s'
log_name = 'MonthlyReportsAccessLog.log'

# initiate log
lg.basicConfig(
    filename = log_name,
    format = log_format, 
    level = lg.DEBUG
    )



def createReport(filename):




    with open("file.lst", "a") as lst_file:
        lst_file.writelines("\n" + filename)
        lst_file.close()




class Error(Exception):
    """Base class for other exceptions"""
    pass

class FileNameError(Error):
    """Raised when file format is incorrect"""
    pass

class DuplicateError(Error):
    """Raised when file has already been processed \
        and is listed in file.lst"""


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
# Print full report into .txt file 
# Append file name to file.lst


def getInfo(filename):
    lg.info("getInfo() Function Start")

    month_dict = {
        "january":  1,
        "february": 2,
        "march":    3,
        "april":    4,
        "may":      5,
        "june":     6,
        "july":     7,
        "august":   8,
        "september":9,
        "october":  10,
        "november": 11,
        "december": 12
    }

    error_directory = "ErrorFiles"


    #### check file formatting ###
    try:
        # extract month from title, error check formatting
        for key in month_dict:
            if key in filename:
                month = key
                month_val = month_dict[key]
        
        # extract year from title, error check formatting
        year = int(''.join(list(filter(str.isdigit, filename))))
        if len(str(year)) != 4 or str(year)[:2] != '20':
            raise FileNameError

        # error check general formatting
        accepted_format = "MonthlyReports\expedia_report_monthly_{}_{}.xlsx".\
            format(month, year)
        if filename == accepted_format:
            lg.info("File is in expected format")
            pass
        else:
            lg.debug("File Name:{} \nExpected Format:{}".format(filename, accepted_format))
            raise FileNameError
        
        # error check if file in file.lst
        if os.path.exists("file.lst"):
            with open("file.lst", "r") as lst_file:
                if os.stat("file.lst").st_size != 0: 
                    contents = lst_file.read()
                    if filename in contents:
                        lg.debug("File '{}' has been already processed".format(filename))
                        raise DuplicateError
                    else: pass
                else: pass

        ### opening file ###
        
        # obtaining dataframes from workbook tabs
        summary_df = pd.read_excel(
            filename, 
            sheet_name="Summary Rolling MoM",
            engine="openpyxl"
            )
        lg.info('Summary report file opened.')
        
        promoter_df = pd.read_excel(
            filename, 
            sheet_name="VOC Rolling MoM",
            engine="openpyxl"
            )
        lg.info('Summary report file opened.')

        ### Summary Report ###
        wb = openpyxl.load_workbook(filename)
        ws = wb.worksheets
        print(ws)

        


        ### 

        with open("file.lst", "a") as lst_file:
            lst_file.writelines("\n" + filename)
            lst_file.close()

    except UnboundLocalError:
        lg.info("File MONTH is not in expected format. Moving to error folder.")
        if not os.path.exists(error_directory):
            os.mkdir(error_directory)
        shutil.move(filename, error_directory)
        lg.info("File moved to error folder.")
            

    except FileNameError:
        lg.info("File NAME is not in expected format. Moving to error folder.")
        if not os.path.exists(error_directory):
            os.mkdir(error_directory)
        shutil.move(filename, error_directory)
        lg.info("File moved to error folder.")
    
    except DuplicateError:
        lg.info("File has already been processed.")
        lg.info("Skipping report.")        



#     # input monthly report request
#     # date_str = '{},{}'.format(month, year)
#     datetime_obj = datetime.datetime.strptime(month+"-"+year, "%B-%Y")
#     lg.info('Date Requested: {}'.format(datetime_obj))

#     # list of processed files
#     # file_lst =  




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
    lg.info('getInfo() Function End')


###################### REPORT REQUEST PROGRAM ##################################

lg.info("*********Request Initiated*********")
directory = "MonthlyReports"

request_ask = input("Request a specific file? [y/[n]]").lower()
if request_ask == 'y' or request_ask == 'yes':
    filename = input("Full file name:") 
    lg.info("Specific Report Request for File: {}".format(filename))
    print("Requesting report for file: {}".format(filename))
    file = os.path.join(directory, filename)
    if os.path.isfile(file):
        getInfo(file)
        lg.info('File Processed')
        print("Request Complete")
    else:
        raise FileNotFoundError
# Create general report for 'no' or Enter
elif request_ask == 'n' or request_ask == 'no' or request_ask == '': 
    lg.info("Exhaustive Report Request for Reports in {}".format(directory))
    print("Exhaustive Report Request in Processing")
    counter = 0
    total = len([item for item in os.listdir('MonthlyReports')])
    for filename in os.listdir(directory):
        file = os.path.join(directory, filename)
        if os.path.isfile(file):
            getInfo(file)
            counter += 1
            lg.info('File {}/{} Processed'.format(str(counter), str(total)))
        else:
            raise FileNotFoundError
# Ask again if other input
else:
    raise Exception("Input is incorrect. Please restart program.") 


lg.info('*********Request Complete*********')
print("Request Complete")
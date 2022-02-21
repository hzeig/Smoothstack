# from distutils.log import error
import logging as lg
import os
from checkFile import checkFile
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

# NitPicking :
# - fix months / no need for month val

class Error(Exception):
    """Base class for other exceptions"""
    pass

class CheckFailError(Error):
    """Raised when file fails checks."""
    pass

class ReportFailError(Error):
    """Raised when data extraction for reports fails."""


def createReport(path):

    filename = path.split("\\")[1]

    try:
        # check file formatting
        if checkFile(path):
            month, month_val, year = checkFile(path)
            date_obj = [month, month_val, year]
        else:
            raise CheckFailError
        
        # collect report data
        if summaryReport(path, date_obj) and promoterReport(path, date_obj):
            summary = summaryReport(path, date_obj)
            promoters = promoterReport(path, date_obj)
        else:
            raise ReportFailError

        # create report file
        lg.info("Creating report file.")
        reportname = "report_{}_{}.txt".format(month, year)
        with open(reportname, "a") as report:
            report.writelines("Full Report for {}, {}".format(month.capitalize(), year))
            report.writelines("\n" + summary)
            report.writelines("\n" + promoters)
        report.close()
        lg.debug("Complete report {} now available.".format(reportname))

        # track file as processed
        lg.info("Saving name of processed file to tracker 'file.lst'.")
        with open("file.lst", "a") as lst_file:
            lst_file.writelines("\n" + filename)
        lst_file.close()
        lg.info("Tracking complete.")

        # done
        lg.info("Process complete.")

    except CheckFailError: 
        lg.error("CheckFileError: File did not pass checks. Moved to error folder.")
    
    except ReportFailError:
        lg.error("ReportFailError: Unable to extract data for report due to file formatting.")





###################### REPORT REQUEST PROGRAM ##################################

lg.info("*********Request Initiated*********")
directory = "MonthlyReports"

request_ask = input("Request a specific file? [y/[n]]").lower()
if request_ask == 'y' or request_ask == 'yes':
    filename = input("Full file name:") 
    lg.info("Specific Report Request for File: {}".format(filename))
    print("Requesting report for file: {}".format(filename))
    path = os.path.join(directory, filename)
    if os.path.isfile(path):
        createReport(path)
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
        path = os.path.join(directory, filename)
        if os.path.isfile(path):
            createReport(path)
            counter += 1
            lg.info('File {}/{} Processed'.format(str(counter), str(total)))
        else:
            raise FileNotFoundError
# Ask again if other input
else:
    raise Exception("Input is incorrect. Please restart program.") 


lg.info('*********Request Complete*********')
print("Request Complete")
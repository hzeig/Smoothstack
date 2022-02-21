import os
import logging as lg
import shutil

log_format = '%(asctime)s %(message)s'
log_name = 'MonthlyReportsAccessLog.log'

# initiate log
lg.basicConfig(
    filename = log_name,
    format = log_format, 
    level = lg.DEBUG
    )



class Error(Exception):
    """Base class for other exceptions"""
    pass

class FileNameError(Error):
    """Raised when file format is incorrect"""
    pass

class DuplicateError(Error):
    """Raised when file has already been processed \
        and is listed in file.lst"""


def checkFile(filename):
    lg.info("Checking file for processing.")

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

        return filename
        
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

import logging as lg
import os
import datetime
from time import strftime
import openpyxl 


class Error(Exception):
    """Base class for other exceptions"""
    pass

class DateMissingError(Error):
    """Raised when date not found."""
    pass

class DataMissingError(Error):
    """Raised when some part of data not found."""



def summaryReport(path, date_obj):
    wb = openpyxl.load_workbook(path) 
    lg.info("Opened file workbook.")

    ws = wb["Summary Rolling MoM"]
    lg.info("Opened worksheet 'Summary Rolling Mom'.")
    
    lg.info("Searching for report data.")
    reg_date_format = "{}, {}".format(date_obj[0], date_obj[2])
    month = date_obj[0]
    data = []
    try:
        lg.info("Finding date.")
        for column in ws:
            for cell in column:
                if isinstance(cell.value, datetime.date):
                    cell_date = cell.value.strftime("%B, %Y")
                    if cell_date == reg_date_format:
                        row = cell.row
                        print(row)
                        lg.info("Date found in row {}".format(row))

    except DateMissingError:
        lg.error("DateMissingError: Date from file name not found in file.")



    try:
        lg.info("Collecting data.")
        for cell in row[1:6]:
            data.append(cell.value)
        print(data)

    except DataMissingError:
        lg.error("DataMissingError: Data for file date not found.")

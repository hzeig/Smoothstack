import logging as lg
import os
import datetime
import openpyxl



class Error(Exception):
    """Base class for other exceptions"""
    pass

class DateMissingError(Error):
    """Raised when date not found."""
    pass

class DataMissingError(Error):
    """Raised when some part of data not found."""


def promoterReport(path, date_obj):
    
    wb = openpyxl.load_workbook(path) 
    lg.info("Opened file workbook.")

    ws = wb["VOC Rolling MoM"]
    lg.info("Opened worksheet 'VOC Rolling Mom'.")
    
    lg.info("Gathering report data.")
    reg_date_format = "{}, {}".format(date_obj[0], date_obj[2])
    month = date_obj
    data = []
    try:
        lg.info("Locating file date.")
        for column in ws:
            for cell in column:
                if isinstance(cell.value, datetime.date):
                    cell_date = cell.value.strftime("%B, %Y")
                    if cell_date.lower() == reg_date_format:
                        column = cell.column
                        lg.info("Date data found in column {} of file.".format(column))


        lg.info("Collecting data.")
        for cell in ws[column][1:6]:
            if cell.value > 1:
                data.append(cell.value)
            else:
                data.append(cell.value*100)
        report = "Summary Report {}: \n\
                Calls Offered: {} \n\
                Abandon after 30s: {}% \n\
                FCR: {}% \n\
                DSAT: {}% \n\
                CSAT: {}% "\
                .format(cell_date, *data)
        lg.info("Data successfully gathered.")
        lg.debug(report)
        
        return report

    except DateMissingError:
    lg.error("DateMissingError: Date from file name not found in file.")

    except DataMissingError:
    lg.error("DataMissingError: Data for file date not found.")
from checkFile import checkFile
from summaryReport import summaryReport
from promoterReport import promoterReport

def createReport(filename):

    if checkFile(filename):
        summary = summaryReport(filename)
        promoters = promoterReport(filename)

    abbr_filename = filename.split("\\")[1]
    with open("Key_Data_{}.txt".format(), "a") as lst_file:
        lst_file.writelines(summary)
        lst_file.writelines(promoters)
        lst_file.close()    

    with open("file.lst", "a") as lst_file:
        lst_file.writelines("\n" + filename)
        lst_file.close()
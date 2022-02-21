from checkFile import checkFile
from summaryReport import summaryReport
from vocReport import promoterReport

def createReport(path):

    filename = path.split("\\")[1]
    if checkFile(path):
        # summary = summaryReport(path)
        # promoters = promoterReport(path)
        print(filename)

    # with open("Key_Data_{}.txt".format(), "a") as lst_file:
    #     lst_file.writelines(summary)
    #     lst_file.writelines(promoters)
    #     lst_file.close()    

    with open("file.lst", "a") as lst_file:
        lst_file.writelines("\n" + filename)
        lst_file.close()


path = 'MonthlyReports\expedia_report_monthly_march_2018.xlsx'
createReport(path)
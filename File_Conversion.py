mypath = 'G:\study\Bioinformatics Training\project'
from os import listdir
from os.path import isfile, join
textfiles = [ join(mypath,f) for f in listdir(mypath) if isfile(join(mypath,f)) and '.data' in  f]


import xlwt
import xlrd
for textfile in textfiles:
    f = open("G:\study\Bioinformatics Training\project\processed.cleveland.data", 'r+')
    row_list = []
    for row in f:
        row_list.append(row.split(','))#condition for splitting
    column_list = zip(*row_list)
    workbook = xlwt.Workbook()
    worksheet = workbook.add_sheet('Sheet1')
    i = 0 
    for column in column_list:
        for item in range(len(column)):
            worksheet.write(item, i, column[item])
        i+=1
    workbook.save(textfile + '.xls')
#xls - старый формат xlsx
#pip install xlrd
from selenium.webdriver.common.devtools.v85.page import print_to_pdf
from xlrd import open_workbook

workbook = open_workbook("../tmp/file_example_XLS_10.xls")
print(workbook.nsheets) #кол-во листов в файле
print(workbook.sheet_names())#имена листов, которые есть в файле
sheet = workbook.sheet_by_index(0)#взять нулевой лист
print(sheet.nrows) #вывести кол-во строк
print(sheet.ncols) #выести кол-во столбцов
print(sheet.cell_value(rowx=9, colx=3))#вывести значение ячейки

#пример цикла. распечатать каждую строчку
for rx in range(sheet.nrows):
    print(sheet.row(rx))

#CVS не рассмотрели, типа простой. с ним работать как со списками, т.к. там разграничение запятой
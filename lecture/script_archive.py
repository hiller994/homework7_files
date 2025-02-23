#раньше была отдельная библиотека, теперь она встроена в питон

from zipfile import ZipFile

with ZipFile("../tmp/Hello.zip") as zip_file:
    print(zip_file.namelist()) #список файлов, которые есть ахрихе, не распаковывая его
    text = zip_file.read('Hello.txt') #зачитать файл, зная его названия, без распаковки архива
    print(text) #выводим содержимое файла
    #zip_file.extract('Hello.txt') #Распаковка архива, тут мы вытягиваем 1 файл по названию. Распаковка будет в корневую папку

    #распаковка с указанием пути
    zip_file.extract('Hello.txt', path='../tmp')
#для работы с pdf в питоне нужно установить инструменты
#pip install pypdf
import os.path

from pypdf import PdfReader #чтобы читать пдф

#создадим переменную и передадим путь к нашему файлу
reader = PdfReader("../tmp/Python Testing with Pytest (Brian Okken).pdf")

print(reader.pages) #выведит все страницы поштучно
print(len(reader.pages)) #Функция len() возвращает длину (количество элементов) в объекте. Покажет кол-во страниц
assert len(reader.pages) == 256 #можем проверить, что в пдф определенное кол-во страниц

#можно вывести конкретную страницу
print(reader.pages[1])

#можно вывести текст с конкретной страницы
print(reader.pages[1].extract_text())
assert 'Simple, Rapid, Effective, and Scalable' in reader.pages[1] #проверка, что данный текст находится на 1ой страницу

#можно проверить размер файла
print(os.path.getsize("../tmp/Python Testing with Pytest (Brian Okken).pdf")) #размер файла в байтах 3035139
assert os.path.getsize("../tmp/Python Testing with Pytest (Brian Okken).pdf") == 3035139

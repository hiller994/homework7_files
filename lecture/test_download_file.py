import os.path
import time
import pytest
import requests
from selene import query
from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.ie.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from script_os import TMP_DIR


def test_text_in_downloads_file():
    #переопределение сохранения пути файла, вместо места по умолчанию
    options = webdriver.ChromeOptions()
    prefs = {
        #"download.default_directory": r"C:\qa_guru_rep\homework7_files\tmp", #абсолютный путь в папку, в которую нужно сохранить файл
        "download.default_directory": TMP_DIR, #из файла script_os
        "download.prompt_for_downloads": False #игнорирует окна, которые просят подтвердить скачивание
    }
    options.add_experimental_option("prefs", prefs) #добавляем эти опции
    #и потом переопределяем наш драйвер (как в селениуме, но с использованием webdriwer_manager):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    #где:
    #service=Service(ChromeDriverManager().install()) - сам вебдрайвер, указание пути к вебдрайверу (стандартная часть)
    #options=options - наш кастом

    #Теперь закинем это чудо в селен
    browser.config.driver = driver #ему присваиваем наш драйвер созданный

    #--------------------------------------------------------------
    #ЦЕЛЬ
    #скачать файл readme на сайте https://github.com/pytest-dev/pytest/blob/main/README.rst

    #1 способ скачивания файла через кнопку
    #browser.open("https://github.com/pytest-dev/pytest/blob/main/README.rst")
    #browser.element("[data-testid='download-raw-button']").click()
    #time.sleep(4)

    #2 способ скачивания файла, когда кнопки нет. Через зашитую ссылку в коде
    browser.open("https://github.com/pytest-dev/pytest/blob/main/README.rst")
    download_url = browser.element("[data-testid='raw-button']").get(query.attribute("href")) #мы находим объект и указываем на хреф
    print(download_url)
    content = requests.get(url=download_url).content #это скачивание через запрос, в следующием уроке. Тут будет бинарный файл в формате 010101010


    #СОХРАНЕНИЕ ФАЙЛА (сохр. бинарного файла)
    with open("../tmp/readmi2.rst", 'wb') as file: #эта строчка - ОТКРЫТИЕ ОБЪЕКТА КАК ФАЙЛ
    #'wb' - это для передачи контента в файл
        file.write(content) #и у этого объекта "file" мы пишем content, т.е. то, что мы ранее достали


    #with - контекстный менеджер, который позволяет открывать объект, работать с ним
    #делаем assert контекста в файле
    with open("../tmp/readmi2.rst") as file:
        file_content_str = file.read() #читаем файл
        assert "test_answer2" in file_content_str #проверяем, что текст "" присутствует в объекте file_content_str
#--------------------------------------------------------------

#пример с использование констант из файла script_os.py
with open(os.path.join(TMP_DIR, "readmi2.rst"), 'wb') as file:
    pass

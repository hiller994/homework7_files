import os
import time
from zipfile import ZipFile
import pytest

CURRENT_FILE = os.path.abspath(__file__) #можно загнать это в переменную для дальнейшего использования
CURRENT_DIR = os.path.dirname(CURRENT_FILE) #определяет директорию файла с обрезунием названия самого файла
TMP_DIR = os.path.join(CURRENT_DIR, "tmp")
FILE_DIV = os.path.join(CURRENT_DIR, "files_homework7")
ARCH_DIV = os.path.join(FILE_DIV, 'new_zip2025.zip')

@pytest.fixture(scope='module', autouse=True)
def create_new_archive():
    with ZipFile(os.path.join(FILE_DIV, "new_zip2025.zip"), 'w') as new_zip:
        new_zip.write("tmp/Python Testing with Pytest (Brian Okken).pdf")  # добавили пдф
        new_zip.write("tmp/file_example_XLSX_50.xlsx")  # добавили пдф
        new_zip.write("tmp/csvtest.csv")

    yield
    os.remove(ARCH_DIV)






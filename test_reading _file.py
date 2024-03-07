import csv

from pypdf import PdfReader
import zipfile
from openpyxl import load_workbook
import os
from zipfile import ZipFile
import shutil

with ZipFile("resources/zip.zip", 'w') as zip_file:
    zip_file.write("resources/xlsx.xlsx")
    zip_file.write("resources/pdf.pdf")
    zip_file.write("resources/users.csv")


def test_csv():
    with zipfile.ZipFile('resources/zip.zip') as zip_file:
        with zip_file.open('resources/users.csv') as csv_file:
            content = csv_file.read().decode('utf-8-sig')
            csvreader = list(csv.reader(content.splitlines()))
            second_row = csvreader[0]

            assert second_row[0] == 'name;age;status;items'


def test_pdf():
    with zipfile.ZipFile('resources/zip.zip') as zip_file:
        with zip_file.open('resources/pdf.pdf') as pdf_file:
            reader = PdfReader(pdf_file)
            num_pages = len(reader.pages)
            for page_number in range(num_pages):
                page = reader.pages[page_number]
                text = page.extract_text()

                assert "Тестовый" in text


def test_xlsx():
    ARCHIVE_DIR = 'resources/zip.zip'
    TMP_DIR = 'tmp'

    with zipfile.ZipFile(ARCHIVE_DIR, 'r') as zip_ref:
        zip_ref.extractall(TMP_DIR)

    path = os.path.join(TMP_DIR, 'resources/xlsx.xlsx')
    open_xlsx = load_workbook(path)
    sheet = open_xlsx.active
    name = sheet.cell_value = sheet['B2'].value

    assert name == 'тест 1'

    os.remove('resources/zip.zip')
    shutil.rmtree('tmp')

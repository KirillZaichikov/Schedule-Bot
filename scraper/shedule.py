from openpyxl import load_workbook
import pathlib
import sys


class GroupOfFiles:
    list_of_excel_files = []
    def __init__(self):
        path = pathlib.Path(r"C:\Users\user\Documents\ВУЗ\Schedule-Bot\scraper")
        print(path.glob("*.xlsx"))
        for i in path.glob("*.xlsx"):
            self.list_of_excel_files.append(i)


class WorkWithFile:
    def __init__(self):
        self.path_to_file = ''

    def find_excel_file(self):
        path = (pathlib.Path(__file__)).parents[0]
        for i in path.glob("*.xlsx"):
            self.path_to_file = i
            break

    def get_groups(self):
        if self.path_to_file:
            wb = load_workbook(self.path_to_file)
            return wb.sheetnames
        else:
            print("Excel-файл не найден!")


x = WorkWithFile()
x.find_excel_file()
x1 = x.get_groups()
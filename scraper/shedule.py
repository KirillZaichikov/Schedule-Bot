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


class ReadExcel():
    @staticmethod
    def Read(path_to_file, group):
        workbook = load_workbook(path_to_file)
        sheet = workbook[group]
        return sheet


x = WorkWithFile()
x.find_excel_file()
x_1 = ReadExcel.Read(path_to_file=x.path_to_file, group="ИС 23")
for i in x_1.iter_rows(min_row=16):
    for cel in i:
        if cel.value != None:
            print(cel.value)
    print("\n")
from pathlib import Path
from openpyxl.worksheet.worksheet import Worksheet as ws
import pyinputplus as pyip
import openpyxl

from sys import argv

def main():
    if(len(argv) == 4):
        try:
            start = int(argv[1])
            end = int(argv[2])
        except TypeError:
            print("""Usage
%s
 + py main.py start(int) end(int) file""" % ("-" * 45))
            return

    else:
        print("""Usage
%s
 + py main.py start(int) end(int) file""" % ("-" * 45))
        return

    path = Path(argv[3])
    wb = openpyxl.load_workbook(path)

    sheet = wb.active
    if sheet == None:
        return

    num = end - start
    ws.insert_rows(sheet, start, num+1)
    wb.save("output.xlsx")


if __name__ == "__main__":
    main()

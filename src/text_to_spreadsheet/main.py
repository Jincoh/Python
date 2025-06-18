from pathlib import Path

import openpyxl
from openpyxl.utils import cell

from sys import argv

def main():
    wb = openpyxl.Workbook()
    sheet = wb.active
    if sheet == None:
        print("look ma no sheet")
        return
    paths = []
    for i in range(1, len(argv)):
        paths.append(Path(argv[i])) 

    for i in range(len(paths)):
        count = 1
        with open(paths[i]) as f:
            for x in f.readlines():
                sheet.cell(row=count, column=i+1).value = x
                count += 1

    wb.save("wb.xlsx")

if __name__ == "__main__":
    main()

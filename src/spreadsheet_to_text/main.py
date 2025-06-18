from pathlib import Path

import openpyxl
from openpyxl.utils import cell

def main():
    path = Path("wb.xlsx")
    wb = openpyxl.load_workbook(path)
    sheet = wb.active
    if sheet == None:
        return
    
    citer = sheet.iter_cols()

    lst = [[x.value for x in col] for col in citer]
    print(lst)

    count = 0

    for slist in lst:
        count += 1
        with open(f"ofile{count}", "w") as f:
            for x in slist:
                f.write(str(x))

if __name__ == "__main__":
    main()

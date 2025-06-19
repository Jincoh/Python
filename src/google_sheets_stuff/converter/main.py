import ezsheets
from pathlib import Path
from sys import argv

import logging
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")
#logging.debug("test")
def main():
    if len(argv) != 2:
        print("Usage: py main.py [filename]")
        return

    #path = Path("argv[1]")
    ezsheets.upload(argv[1])
    logging.debug(ezsheets.listSpreadsheets())

    sdict = ezsheets.listSpreadsheets()
    es = ""
    for key, value in sdict.items():
        if value == argv[1]:
            es = key
            break
    logging.debug(es)
    wb = ezsheets.Spreadsheet(es)
    logging.debug(wb)
    
    temp = wb.downloadAsExcel("someSpreadsheet.xlsx")


if __name__ == "__main__":
    main()

import ezsheets
import json
from pathlib import Path

def main():
    path = Path("outfile.json")
    wb = ezsheets.Spreadsheet("13To5htUEvYgvmo95IWGMPJKKXY4oGdRQ7iquGOdwRiY")
    
    if wb == None:
        return

    sheet = wb[0]
    x = sheet.getColumn(3)

    print(x)
    lst = [i for i in x if i != ""]
    print(lst)
    
    with open(path, "w") as f:
        json.dump(lst, f, indent=4)

if __name__ == "__main__":
    main()

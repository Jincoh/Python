import openpyxl
import json

from pathlib import Path

def main():
    path = Path(Path.home() / "Documents/CalcWorksheets/censuspopdata.xlsx")
    opath = Path("outfile.json")
    wb = openpyxl.load_workbook(path)
    sheet = wb.active
    if sheet == None:
        print("error sheet = None")
        return
    counties = list(sheet.columns)[2]
    pops = list(sheet.columns)[3]

    popdict = {}
    for i in range(len(counties)): 
        popdict.setdefault(counties[i].value, 0)
        squiglyBegon = pops[i].value

        if(type(squiglyBegon) == int):
            popdict[counties[i].value] += squiglyBegon

    for key in popdict.keys():
        countys = f"county: {key}"
        countys = countys.ljust(25)
        population = f"Population: {popdict[key]}"
        population.ljust(25)


    with open(opath, "w") as f:
        json.dump(popdict,f, indent=4)

if __name__ == "__main__":
    main()

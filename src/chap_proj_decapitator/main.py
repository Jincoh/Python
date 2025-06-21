import csv

from pathlib import Path

def main():
    path = Path("./cfile.csv")
    opath = Path("./ofile.csv")
    with open(path) as f:
        dr = csv.DictReader(f)
        with open(opath, "w") as ff:
            dw = csv.writer(ff)
            for row in dr:
                dw.writerow(row.values())

            

if __name__ == "__main__":
    main()

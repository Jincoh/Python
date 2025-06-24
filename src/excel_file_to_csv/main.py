import pandas as pd
import os
import re

from pathlib import Path

def main():
    ipath = Path("./indir")
    opath = Path("./outdir")
    
    reg = re.compile(r"(.*)(\.xlsx$)")
    for dr, subdir, files in os.walk(ipath):
        for file in files:
            if re.match(reg, file):
                print(f"{dr}/{file}")
                res = reg.search(file)
                if res == None:
                    continue
                print(res.group(1))
                rf = pd.read_excel(f"{dr}/{file}")
                rf.to_csv(opath / f"{res.group(1)}.csv")


if __name__ == "__main__":
    main()

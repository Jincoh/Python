from pathlib import Path
from os import listdir
from sys import argv
import re

def main():
    p = Path(argv[1])

    flist = listdir(p)
    reg = re.compile("[fF]lag")
    for x in flist:
        tmpp = p / x
        with open(tmpp, "r") as f:
            contents = f.read()

            if re.search(reg, contents):
                print("Match found in file: %s" % (x))
            f.close()

if __name__ == "__main__":
    main()

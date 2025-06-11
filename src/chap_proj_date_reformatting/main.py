import os
import shutil
import re

from pathlib import Path

def main():
    infpath = Path("files_with_american_format")
    outfpath = Path("files_with_euro_format")
    reg = re.compile(r"(.*)([0-1][0-9]-[0-3][0-9]-\d\d\d\d)")
    for _, _, z in os.walk(infpath):
        for f in z:
            datematch = reg.search(f)
            if datematch != None:
               date = datematch.group(1,2)
               prefix, date = datematch.group(1,2)
               m,d,y = date.split("-")
               shutil.copy(infpath / f, outfpath / ("%s%s-%s-%s" % (prefix,d,m,y)))

if __name__ == "__main__":
    main()

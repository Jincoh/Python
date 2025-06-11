import os
import re
import shutil

from pathlib import Path
from sys import argv

def main():
    if len(argv) == 4 and argv[1] == "makegap":
        path, reg, files = pathutil(argv[3])
        makegaps(path, reg, files, argv[2])
    elif (len(argv) == 3 and argv[1] == "fillgaps"):
        path, reg, files = pathutil(argv[2])
        fillgaps(path, reg, files)
    else:
        print("""Usage: 
%s
 + python3 main.py fillgaps [target]  eg.
  - python3 main.py fillgaps ./target

 + python3 main.py makegap [filename] [target] eg.
  - python3 main.py makegap file001 ./target""" % ("-" * 45))


def pathutil(pathstr):
    path = Path(pathstr)
    reg = re.compile(r"(.*)(\d\d\d)(.*)")
    files = os.listdir(path)
    files.sort()
    return path, reg, files

def fillgaps(path, reg, files):
    lastnum = 000
    for file in files:
        matches = reg.search(file)

        if matches != None:
            num = int(matches.group(2)) 

            if lastnum != num - 1:
                num2 = num -1

                if num2 < 10:
                    i = "00%s" % num2
                elif num2 < 100:
                    i = "0%s" % num2
                else:
                    i = "%s" % num2

                open(path / ("%s%s%s" % (matches.group(1), i, matches.group(3))), "w")

            lastnum = num

def makegaps(path, reg, files, infile):
    if infile in files:
        matches = reg.match(infile)
        if matches != None:
            num = int(matches.group(2))
        else:
            print("Error:\nfilename is improperly formatted")
            return

        for file in reversed(files):
            matchf = reg.match(file)
            numf = int(matchf.group(2)) 
            if numf > num:
                num2 = numf + 1

                if num2 < 10:
                    i = "00%s" % (num2)
                elif num2 < 100:
                    i = "0%s" % (num2)
                else:
                    i = num2

                shutil.move(path / file, path / ("%s%s%s" % (matchf.group(1), i, matchf.group(3))))

    open(path / infile, "w")


        
if __name__ == "__main__":
    main()

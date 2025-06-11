import os
import send2trash

from sys import argv
from pathlib import Path

def main():
    if len(argv) > 1:
        path = Path(argv[1])
    else:
        path = Path("./")
    
    for d,_,f in os.walk(path):
        for file in f:
            size = os.path.getsize(("%s/%s" % (d, file)))
            #print("%s/%s" % (d, file))
            #print(1e+8)

            if size > 1e+8:
                print("%s/%s" % (d, file))
                print(size)

if __name__ == "__main__":
    main()

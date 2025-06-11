import os
import shutil
from sys import argv
from pathlib import Path

def main():
    if len(argv) < 4:
        print("""Usage:
%s
 + main.py [sourceDir] [fileExtension] [targetDir]
  - eg. main.py ./ py target"""
              % ("-" * 45))

        return
        
    path = Path(argv[1])

    tdir = os.listdir(path)
    for x in tdir:
        splitl = x.split(".", -1)
        suffix = ""
        if len(splitl) > 1:
            suffix = splitl[1]

        if suffix == argv[2]:
            shutil.copy(path / x, argv[3])


if __name__ == "__main__":
    main()

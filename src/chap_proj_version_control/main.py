import zipfile
import os

from pathlib import Path

def main():
    tpath = Path(r"target")
    biggest = 0
    for files in os.listdir(tpath):
        if (len(files) > 4 and int(files[4]) > biggest):
            biggest = int(files[4])

    zfile = zipfile.ZipFile(tpath / ("apb_%s.zip" % (biggest + 1)), "a")
    for dirs,_,files in os.walk(r"./"):
        for file in files:
            if dirs != "./target":
                zfile.write(("%s/%s" % (dirs, file)), compress_type=zipfile.ZIP_DEFLATED)
    zfile.close()

if __name__ == "__main__":
    main()

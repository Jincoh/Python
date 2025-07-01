from posix import listdir
from PIL import Image
from pathlib import Path
import os

def main():
    ipath = Path("indir/Logo.png")
    tpath = Path("tdir")
    opath = Path("outdir")
    

    logo = Image.open(ipath)
    lst = os.listdir(tpath)
    for file in lst:
        target = Image.open(tpath / file)

        targetcp = target.copy()
        lwidth, lheight = logo.size
        twidth, theight = targetcp.size
        targetcp.paste(logo, (twidth-lwidth, theight -lheight) )

        targetcp.save(opath / file)

if __name__ == "__main__":
    main()

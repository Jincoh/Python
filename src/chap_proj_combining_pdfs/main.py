import PyPDF2 as pdf
import os

from pathlib import Path
from sys import argv

def main():
    path = Path("./")
    lst = os.listdir(path)
    lst.sort()
    lst2 = []
    for file in lst:
        if file != "main.py":
            lst2.append(file)

    pwriter = pdf.PdfWriter()

    with open(lst[0], "rb") as f:
        pdfile = pdf.PdfReader(f)

        for i in range (len(pdfile.pages)):
            pwriter.add_page(pdfile.pages[i])

    for i in range(1,len(lst2)):
        print(lst2[i])

        with open(path / lst2[i], "rb") as f:
            pdfile = pdf.PdfReader(f)

            for j in range(int(argv[1]), len(pdfile.pages)):
                pwriter.add_page(pdfile.pages[j])
                

    with open("pdfOutfile.pdf", "wb") as f:
        pwriter.write("pdfOutfile.pdf")
        
    print(f.closed)

if __name__ == "__main__":
    main()

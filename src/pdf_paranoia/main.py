import PyPDF2 as pdf
import PyPDF2.errors as pderrors
import os
import re

from pathlib import Path

import logging
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    path = Path("./files")
    for d, sd, files, in os.walk(path):
        logging.debug(f"file = {files}, subdir = {sd}, directory = {d} ")
        for f in files:
            if re.match(r".*\.pdf", f):
                p = Path(d, f)
                logging.debug(p)

                try:
                    reader = pdf.PdfReader(p)
                    writer = pdf.PdfWriter()
                except pderrors.EmptyFileError:
                    logging.debug("Empty file error")
                    continue

                for page in reader.pages:
                    writer.add_page(page)

                writer.encrypt("1234")

                with open(p, "wb") as o:
                    writer.write(o)


if __name__ == "__main__":
    main()

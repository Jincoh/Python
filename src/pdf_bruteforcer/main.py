import PyPDF2
import PyPDF2.errors as pdferr

from pathlib import Path

import logging
logging.basicConfig(level = logging.CRITICAL, format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    path = Path("./enc.pdf")
    dictionary = Path("./dictionary")
    reader = PyPDF2.PdfReader(path)
    

    with open(dictionary) as f:
        lines = f.readlines()
        logging.debug(lines)

        for line in lines:
            line = line.strip("\n")
            if reader.decrypt(line) != 2:
                continue

            print(f"pass = {line}")
            logging.debug(line)
            logging.debug(reader.pages)


if __name__ == "__main__":
    main()

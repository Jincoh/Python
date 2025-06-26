import time, threading
import requests, bs4
import pyinputplus as pyip

import logging
logging.basicConfig(level=logging.CRITICAL, format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    start = pyip.inputNum("input a num to start at: ")
    end = pyip.inputNum("input a num to end at: ")

    if start <= 0:
        print("positive nums only")
        return
    print("working...")

    dthreads = []

    for i in range(start, end, 10):
        x = i + 9
        if x > end:
            x = end

        print(f"from {i} to {x}")

        throbj = threading.Thread(target=xkcd, args=(i, x))
        dthreads.append(throbj)
        throbj.start()

    num = 0
    for thread in dthreads:
        thread.join()
        num += 1
        print(f"thread num {num} is done")

    print("all done")


def xkcd(start: int, stop: int):
    current = start
    while(current <= stop):
        res = requests.get(f"https://xkcd.com/{current}")
        res.raise_for_status()

        bs = bs4.BeautifulSoup(res.text, "html.parser")
        img = bs.select("#comic > img")
        logging.info(img[0])
        link = f"https:{img[0].get("src")}"
        logging.info(link)
        res = requests.get(link)
        res.raise_for_status()

        with open(f"outfiles/image{current}.jpg", "wb") as f:
            for chunk in res.iter_content(100000):
                f.write(chunk)

        current += 1



if __name__ == "__main__":
    main()

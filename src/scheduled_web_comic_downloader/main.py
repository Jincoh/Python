#can be run througn cron, this approach is better as you don't have to manually restart it every day
from os import path
import requests
import bs4

from pathlib import Path
def main():
    lastname = Path("lastname")
    outdir = Path("outfiles")

    res = requests.get("https://xkcd.com")
    res.raise_for_status()

    bs = bs4.BeautifulSoup(res.text, "html.parser")
    img = bs.select_one("#comic > img")

    if img == None:
        print("an unexpected error has occured")
        return

    title = img.get("title")
    print(title)
    src = img.get("src")
    print(src)

    if title == None or src == None:
        print("either title or src was none")
        return

    with open(lastname) as f:
        #print(f.readlines()[0])
        if f.readlines()[0] == title:
            print("nothing new")
            return

    with open(lastname, "w") as f:
        print("new post downloading...")
        f.write(str(title))

    ifile = requests.get(f"https:{src}")
    with open(outdir / "latestcommic.png", "wb") as f:
        for chunk in ifile.iter_content(100000):
            f.write(chunk)
        


if __name__ == "__main__":
    main()

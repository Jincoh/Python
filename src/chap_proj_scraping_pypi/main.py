import bs4, time, logging
import logging

from sys import argv
from selenium import webdriver
from os import system

logging.basicConfig(filename="logfile.txt", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
def main():
    if(len(argv) > 1):
        keywords = "+".join(argv[1:])
        logging.debug(keywords)
    else:
        print("""Usage
%s
 + py main.py [keywords] eg.
  - py main.py pyperclip""" % ("-" * 45))
        return

    print("loading...")
    logging.debug("https://pypi.org/search/?q=" + keywords)
    options = webdriver.FirefoxOptions()
    browser = webdriver.Firefox(options=options)
    browser.get("https://pypi.org/search/?q=" + keywords)
    time.sleep(2)
    res = browser.page_source
    resSoup = bs4.BeautifulSoup(res, "html.parser")
    element = resSoup.select(".package-snippet")
    browser.quit()
    logging.debug(element[0].get("href"))
    print()
    for i in range(min(5,len(element))):
        result = "https://pypi.org%s" % element[i].get("href")
        print("Opening %s" % result)
        system("opera " + result)
        #webbrowser.open(result, new=2) #swapped for system hardcode bc it opened two tabs for some reason

if __name__ == "__main__":
    main()

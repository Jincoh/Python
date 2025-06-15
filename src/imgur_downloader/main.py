"""disclaimer: I don't have a clue how to use imgur so I'm making the assumption it's normal to
search by tag there since I can't figure out how to search by title

also imgur seems to not like people scraping images. this app only kinda works, 
it gets webps and depends on curl"""


import requests, bs4
import pyinputplus
import subprocess
import time

from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from sys import argv

def main():
    if len(argv) < 2:
        print("""
Usage:
%s
 + py main.py [search tag]
  - py main.py cats

Note:
  Requires curl""" % ("-" * 45))



    else:
        functionality(argv[1])
    
def functionality(stag: str):
    options = webdriver.FirefoxOptions()
    options.add_argument("-headless")
    driver = webdriver.Firefox(options=options)
    driver.get(f"https://imgur.com/t/{stag}")
#cookies
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".fc-cta-consent"))).click()
    time.sleep(2)

    elements = driver.find_elements(By.CSS_SELECTOR, "div[class=imageContainer] img")
    num = 1
    for element in elements:

        link = element.get_attribute("src")
        if link != None:
            subprocess.call(["curl", link, "-o", f"filedir/imgur{num}.webp"])

        num += 1

    driver.close()

if __name__ == "__main__":
    main()

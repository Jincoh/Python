"""Im not downloading all results bc I value my storage, minor adjustments required to change this
also disclaimer: I don't have a clue how to use imgur so I'm making the assumption it's normal to
search by tag there since I can't figure out how to search by title"""


import requests, bs4
import pyinputplus
import subprocess
import time

from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def main():
    options = webdriver.FirefoxOptions()
    #options.add_argument("-headless")
    driver = webdriver.Firefox(options=options)
    driver.get("https://imgur.com/t/cats")
#cookies
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".fc-cta-consent"))).click()
    time.sleep(2)

    elements = driver.find_elements(By.CSS_SELECTOR, "div[class=imageContainer] img")
    print(elements)
    num = 1
    for element in elements:

        link = element.get_attribute("src")
        if link != None:
            subprocess.call(["curl", link, "-o", f"filedir/imgur{num}.webp"])

        num += 1

if __name__ == "__main__":
    main()

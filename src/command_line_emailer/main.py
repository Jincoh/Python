import time
import pyinputplus as pyin

from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from sys import argv
from pathlib import Path

SUBDEFAULT = "I told my bot to say hi, be nice to my child"

def main():

    if len(argv) > 2 and argv[2] == "file":
        infilepath = Path(argv[3])
        f = open(infilepath)
        mailcontents = f.read()
    elif len(argv) > 2 and argv[2] == "string":
        mailcontents = argv[3]
    elif len(argv) > 1 and argv[2] == "default":
        mailcontents = """HELLO DEAR RECPIENT 
    You're in luck

you've won an all expenses paid trip to sawcon, you also get to bring 3 more friends with our wonderful friends and family pass, this can be redeemed at our website sawcon.com using the code d33znut2"""
    else:
        print("Usage: py main.py [gmail], Note to programmer, update error message to be acurate")
        return

    mainlogic(mailcontents)

def mainlogic( body: str, subject:str = SUBDEFAULT, gmail:str = argv[1]):

    passw = pyin.inputPassword("please input your email password:\n")

    print("Working...")

    options = webdriver.FirefoxOptions()
    options.add_argument("-headless")
    browser = webdriver.Firefox(options=options)

    browser.get("https://mail.google.com/mail/u/5/#inbox")
#username
    inputs = browser.find_element(By.CSS_SELECTOR, "#identifierId")
    inputs.send_keys("autotheautomaton@gmail.com")
    browser.find_element(By.CSS_SELECTOR, ".VfPpkd-LgbsSe-OWXEXe-k8QpJ > span:nth-child(4)").click()
#password
    WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='password']"))).send_keys(passw)
    browser.find_element(By.CSS_SELECTOR, ".VfPpkd-LgbsSe-OWXEXe-k8QpJ").click()
#compose
    WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".T-I-KE"))).click()
#To
    WebDriverWait(browser,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[class='agP aFw']"))).send_keys(gmail)
#subject
    WebDriverWait(browser,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='subjectbox']"))).send_keys(subject)
#body
    WebDriverWait(browser,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class='Am aiL Al editable LW-avf tS-tW']"))).send_keys(body)
#send
    WebDriverWait(browser,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[role='button'][data-tooltip='Send ‪(Ctrl-Enter)‬']"))).click()

    time.sleep(2)

    browser.close()
    print("done")

if __name__ == "__main__":
    main()

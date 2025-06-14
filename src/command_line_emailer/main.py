import bs4

from selenium import webdriver
from selenium.webdriver.common.by import By

def main():
    options = webdriver.FirefoxOptions()
    browser = webdriver.Firefox(options=options)
    browser.get("https://mail.google.com/mail/u/5/#inbox")
    inputs = browser.find_element(By.CSS_SELECTOR, "#identifierId")
    inputs.send_keys("autotheautomaton@gmail.com")
    browser.find_element(By.CSS_SELECTOR, ".VfPpkd-LgbsSe-OWXEXe-k8QpJ > span:nth-child(4)").click()


if __name__ == "__main__":
    main()

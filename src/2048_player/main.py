from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time
import random

def main():
    driver = webdriver.Firefox()
    
    driver.get("https://play2048.co")

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#ez-accept-necessary"))).click()
    print("starting...")
    while (True):
        x = random.randint(1,4)
        elements = driver.find_elements(By.CSS_SELECTOR, "button[class='white flex items-center justify-center whitespace-nowrap rounded-lg text-base disabled:opacity-50 border-tan border-2 px-4 h-12 ']")
        if elements:
            print("Finished")
            time.sleep(10)
            driver.close()
            return

        match x:
            case 1:
                WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body"))).send_keys(Keys.ARROW_UP)
            case 2:
                WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body"))).send_keys(Keys.ARROW_DOWN)
            case 3:
                WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body"))).send_keys(Keys.ARROW_LEFT)
            case 4:
                WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body"))).send_keys(Keys.ARROW_RIGHT)

if __name__ == "__main__":
    main()

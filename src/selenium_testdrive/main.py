from selenium import webdriver

def main():
    options = webdriver.FirefoxOptions()
    browser = webdriver.Firefox(options=options)
    browser.get("http://www.google.com")
    browser.execute_script("return document.cookie")
    browser.execute_script("return navigator.userAgent")
    print(browser.title)
    browser.quit()

if __name__ == "__main__":
    main()

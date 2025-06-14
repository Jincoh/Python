import requests, logging, bs4, time

from selenium import webdriver

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
def main():
    URL = "https://xkcd.com"
    opt = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(options=opt)
    urlend = ""

    count = 0
    while(count < 10):
        driver.get(URL + urlend)
        res = driver.page_source

        soup = bs4.BeautifulSoup(res, "html.parser")
        element = soup.select("#middleContainer > ul:nth-child(2) > li:nth-child(2) > a")
        href = element[0].get("href")

        logging.info(f"Element = {element}")
        logging.info(f"href = {href}")
        logging.info(f"full link = {URL}{href}")
        urlend = str(href) 

        imagecode = soup.select("#comic > img")
        logging.info(f"imagecode = {imagecode}")
        image =  imagecode[0].get("src")
        logging.info(f"full image link = https:{image}")

        res2 = requests.get(f"https:{image}")
        res2.raise_for_status()

        with open(f"./imagefile{count}.png", "wb") as f:
            for chunk in res2.iter_content(100000):
                f.write(chunk)
            f.close()
        count += 1
    
    
    driver.close()
    

    driver.close

if __name__ == "__main__":
    main()

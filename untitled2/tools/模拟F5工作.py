import time
from selenium import webdriver

def refresh(url,num):
    driver = webdriver.Chrome("../tools/chromedriver.exe")
    driver.get(url)
    for i in range(num):
        time.sleep(0.01)
        driver.refresh()
    driver.close()

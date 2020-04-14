import time
from selenium import webdriver

driver=webdriver.Chrome("../tools/chromedriver.exe")
driver.maximize_window()
driver.get("https://www.baidu.com")
element = driver.find_element_by_name("wd")
element.send_keys("百度新闻")
element = driver.find_element_by_id("su").click()
time.sleep(3)
driver.back()
time.sleep(3)
driver.forward()
driver.close()




from selenium import webdriver
import time

driver=webdriver.Chrome("../tools/chromedriver.exe")
driver.maximize_window()
driver.get("file:///G:/Google%20Chrome/selenium_pages-master/alert.html")
time.sleep(5)
element = driver.find_element_by_id('b1').click()
print(driver.switch_to.alert.text)
time.sleep(3)
driver.switch_to.alert.accept()
time.sleep(3)
driver.close()
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

driver=webdriver.Chrome("../tools/chromedriver.exe")
driver.maximize_window()
driver.get("file:///G:/Google%20Chrome/selenium_pages-master/form_web_element.html")
time.sleep(5)
elements = driver.find_elements_by_css_selector('#ss_multi option[selected="selected"]')
for element in elements:
    element.click()
time.sleep(5)
select_teacher = Select(driver.find_element_by_id("ss_multi"))
select_teacher.select_by_visible_text("小雷老师")

time.sleep(5)
driver.close()
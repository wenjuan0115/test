from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

driver=webdriver.Chrome("../tools/chromedriver.exe")
driver.maximize_window()
driver.get("file:///G:/Google%20Chrome/selenium_pages-master/form_web_element.html")
select_num = Select(driver.find_element_by_id("ss_single"))
assert len(select_num.options) == 3
if (len(select_num.options) == 3):
    print("此下拉选项等于3....")
else:
    print("此下拉选项不等于3...")

time.sleep(5)
driver.close()
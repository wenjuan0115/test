from selenium import webdriver
import time

driver=webdriver.Chrome("../tools/chromedriver.exe")
driver.maximize_window()
driver.get("file:///G:/Google%20Chrome/selenium_pages-master/form_web_element.html")
elements = driver.find_elements_by_css_selector('#s_checkbox input[checked="checked"]')
for element in elements:
    element.click()
time.sleep(5)
driver.find_element_by_css_selector("#s_checkbox input[value='小雷老师']").click()
time.sleep(5)
driver.close()
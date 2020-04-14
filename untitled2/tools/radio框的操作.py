from selenium import webdriver
import time

driver=webdriver.Chrome("../tools/chromedriver.exe")
driver.maximize_window()
driver.get("file:///G:/Google%20Chrome/selenium_pages-master/form_web_element.html")
element = driver.find_element_by_css_selector('#s_radio input[checked=checked]')
print('当前选中的老师是: ' + element.get_attribute('value'))
time.sleep(5)
driver.find_element_by_css_selector('#s_radio input[value="小雷老师"]').click()
time.sleep(5)
driver.close()




from selenium import webdriver
driver=webdriver.Chrome("../tools/chromedriver.exe")
driver.maximize_window()
driver.get("file:///G:/Google%20Chrome/selenium_pages-master/form_web_element.html")
element = driver.find_element_by_css_selector('#s_radio input[checked=checked]')
print('选中是: ' + element.get_attribute('value'))
driver.find_element_by_css_selector('#s_radio input[value="小雷老师"]').click()
driver.close()
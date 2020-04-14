from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver=webdriver.Chrome("../tools/chromedriver.exe")
driver.get("https://www.baidu.com")
driver.maximize_window()
ac = ActionChains(driver)
ac.move_to_element(driver.find_element_by_css_selector('[name="tj_briicon"]')).perform()

time.sleep(5)
driver.close()

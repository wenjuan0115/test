from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("../tools/chromedriver.exe")
ac = ActionChains(driver)
driver.maximize_window()
driver.get("https://www.baidu.com")
time.sleep(3)
element = driver.find_element_by_css_selector("#lg img")
ac.context_click(element).perform()
ac.send_keys(Keys.PAGE_DOWN).perform()
ac.send_keys(Keys.ENTER).perform()
win = driver.window_handles[1]
driver.switch_to.window(win)
assert '今日新鲜事' in driver.title

time.sleep(3)
driver.quit()

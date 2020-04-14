from selenium import webdriver
import time

driver = webdriver.Chrome("../tools/chromedriver.exe")
driver.maximize_window()
driver.get("file:///G:/Google%20Chrome/selenium_pages-master/alert.html")
time.sleep(5)
ele = driver.find_element_by_id('b2').click()
print("第一次点击confirm按钮....")
print(driver.switch_to.alert.text)
driver.switch_to.alert.accept()
print("点击了确定按钮....")
time.sleep(5)
ele2 = driver.find_element_by_id('b2').click()
print("第二次点击confirm按钮....")
driver.switch_to.alert.dismiss()
print("点击了取消按钮....")
time.sleep(3)
driver.close()

from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("https://tieba.baidu.com/")
sleep(2)
element = driver.find_element_by_css_selector(".title>a[title='小说']")
driver.execute_script("arguments[0].scrollIntoView();", element)
sleep(5)
driver.quit()
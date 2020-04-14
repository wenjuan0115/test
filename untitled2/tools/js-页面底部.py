from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("https://tieba.baidu.com/")
sleep(2)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
sleep(5)
driver.quit()
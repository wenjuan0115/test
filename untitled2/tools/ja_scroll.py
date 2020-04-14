from selenium import webdriver
from time import sleep

browser = webdriver.Chrome()
browser.get("https://tieba.baidu.com/")
sleep(2)
# 开始控制滚动条滚动到小说指定位置
elment = browser.find_element_by_css_selector(".title>a[title='小说']")
browser.execute_script("arguments[0].scrollIntoView();", elment)
sleep(5)
browser.quit()

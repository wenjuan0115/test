from selenium import webdriver
import time

driver=webdriver.Chrome("../tools/chromedriver.exe")
driver.maximize_window()
driver.get("https://book.douban.com")
element = driver.find_element_by_xpath("//div[@class='nav-items']/ul/li[3]").click()
time.sleep(3)
elements = driver.find_elements_by_xpath("//div[@class='book-brief']/h3")
for element in elements:
    print(element.text)


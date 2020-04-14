from selenium import webdriver

driver = webdriver.Chrome("d:/webdrivers/chromedriver.exe")
driver.get("http://www.baidu.com")
driver.implicitly_wait(5)
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
ele=driver.find_element_by_xpath("//div [@id=1] /h3/a").get_attribute("text")
print(ele)
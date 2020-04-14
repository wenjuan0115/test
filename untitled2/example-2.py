# 输出链接信息
# from selenium import webdriver
# driver = webdriver.Chrome("d:/webdrivers/chromedriver.exe")
# driver.get(" https://www.baidu.com")
# elements = driver.find_elements_by_tag_name("a")
# for element in elements:
#     print(element.text)

# # 摘取邮箱信息
from selenium import webdriver
import re
driver = webdriver.Chrome("d:/webdrivers/chromedriver.exe")
driver.get(" http://home.baidu.com/contact.html")
emails = re.findall(r'[\w]+@[\w\.-]+', driver.page_source)
for email in emails:
    print(email)

# 验证网页图片是否正确
# from selenium import webdriver
# driver = webdriver.Chrome("d:/webdrivers/chromedriver.exe")
# driver.get("http://v3.alphacoding.cn/login")
# URLS = driver.find_elements_by_tag_name("img")
# for URL in URLS:
#     print(URL.get_attribute('class'))
# # driver.close()





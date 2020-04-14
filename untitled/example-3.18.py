# from selenium import webdriver
#
# # 请在今日头条中使用xpath
# driver = webdriver.Chrome("d:/webdrivers/chromedriver.exe")
# driver.get("https://www.toutiao.com/ch/news_tech/")
# assert "Python" in driver.title


# 获取科技栏目的所有新闻标题
# from selenium import webdriver
#
# driver = webdriver.Chrome("d:/webdrivers/chromedriver.exe")
# driver.get("https://www.toutiao.com/ch/news_tech/")
# elements = driver.find_elements_by_xpath("//a[@class ='link title']")
# for element in elements:
#     print(element.text)

# 手工用例脚本化
# from selenium import webdriver
# driver = webdriver.Chrome("d:/webdrivers/chromedriver.exe")
# driver.get("https://www.baidu.com")

# 登录案例
# from selenium import webdriver
# driver = webdriver.Chrome("d:/webdrivers/chromedriver.exe")
# driver.get("https：//github.com/login")
#


# 请在今日头条中使用xpath
# from selenium import webdriver
#
# driver = webdriver.Chrome("d:/webdrivers/chromedriver.exe")
# driver.get("https://www.toutiao.com/ch/news_tech/")
# elements = driver.find_elements_by_xpath("//a[@class='link title']")
# for element in elements:
#     print(element.text)


# 手工用例脚本化
# from selenium import webdriver
#
# driver = webdriver.Chrome("d:/webdrivers/chromedriver.exe")
# driver.get("https://www.baidu.com")
# element = driver.find_element_by_name("wd")
# element.send_keys("selenium")
# element = driver.find_element_by_id("su").click()
# elements = driver.find_elements_by_tag_name("a")
# for element in elements:
#     print(element)

# 登录案例
# from selenium import webdriver
# driver = webdriver.Chrome("d:/webdrivers/chromedriver.exe")
# driver.get("https://github.com/login")
# elementname=driver.find_element_by_id("login_field")
# elementname.send_keys("admin")
# elementpwd=driver.find_element_by_id("password")
# elementpwd.send_keys("admin123")
# element=driver.find_element_by_name("commit").click()
# a=driver.find_element_by_xpath('//div[@class="auth-form px-3"]/p')
# print(a.text)
# driver.back()
# driver.close()


# 验证首页核心元素

# from selenium import webdriver
# from selenium.webdriver.support.ui import Select
# driver = webdriver.Chrome("d:/webdrivers/chromedriver.exe")
# driver.get("http://v3.alphacoding.cn/login")
# elementname=driver.find_element_by_id("input-13")
# elementname.send_keys("20171404146")
# elementpwd=driver.find_element_by_id("input-14")
# elementpwd.send_keys("123456")
# driver.find_element_by_class_name("v-select__selection v-select__selection- -comma").click()
# driver.find_element_by_id("山西省财政税务专科学校-list-item-21").click()
# element=driver.find_element_by_tag_name("botton").click()
#
#


# 登录

# from selenium import webdriver
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
#
# import time
#
# driver = webdriver.Chrome("d:/webdrivers/chromedriver.exe")
# driver.get("https://github.com/login")
# driver.maximize_window()
#
# loadfrom="//from/div[4]/input[9]"
# loadSrc="/html/body/div[1]/header/div[7]/details/summary/img"
# print("等待相应中.....")
# WebDriverWait(driver,30,1).until(EC.element_to_be_clickable((By.XPATH, loadfrom)))
#
# driver.find_elements_by_id("login_field").send_keys("1071266236@qq.com")
# driver.find_elements_by_id("password").send_keys("123456")
#
# driver.find_elements_by_xpath(loadfrom).click()
#
# print("登录中...")
# WebDriverWait(driver,30,1).until(EC.element_to_be_clickable((By.XPATH, loadSrc)))
# if(driver.find_elements_by_xpath(loadSrc).alt!='@test123456'):
#     print("登录错误..")


# 手工测试
# from selenium import webdriver
# import time
# driver = webdriver.Chrome("d:/webdrivers/chromedriver.exe")
# driver.get("https://www.baidu.com")
# str1=driver.find_element_by_id('kw').send_keys("selenium")
# button=driver.find_element_by_id('su').click()
# time.sleep(3)
# # 竞价排名
# guanggao=driver.find_elements_by_xpath('//*[@id="3002"]/div[3]/font[2]/a/span')
# lenn=str(len(guanggao))
# print(lenn)
# for a in guanggao:
#     print(a.text)
# # 竞价排名后的第一个链接是否为官网
# first=driver.find_element_by_xpath('//div[@id='+lenn+']/h3/a').get_attribute('text')
# print(first)
# if  (first == "Selenium automates browsers. That's it!"):
#     print("竞价排名后的第一个链接是selenium官网")
# else:
#     print('不是')


# 平台首页
# from selenium import webdriver
# import time
# driver = webdriver.Chrome("d:/webdrivers/chromedriver.exe")
# driver.get("http://v3.alphacoding.cn/login")
#
# ele1=driver.find_element_by_id("input-13").is_enabled()
# ele2=driver.find_element_by_id("input-14").is_enabled()
# ele3=driver.find_element_by_class_name("v-btn").is_enabled()
# ele4=driver.find_element_by_tag_name("img").is_enabled()
# try:
#     if (ele1 == True and ele2 == True and ele3 == True and ele4 == True):
#         print("页面核心元素正确")
# except:
#     print("代码有错")
# finally:
#     time.sleep(5)
#     driver.close()
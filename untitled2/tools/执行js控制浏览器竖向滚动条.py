from selenium import webdriver

driver=webdriver.Chrome("../tools/chromedriver.exe")
driver.maximize_window()
driver.get("https://tieba.baidu.com")
element = driver.find_element_by_link_text("地区")
if element.is_enabled():
    print("滚动条可用....")
driver.execute_script("return arguments[0].scrollIntoView();",element)
# driver.close()
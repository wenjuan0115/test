from selenium import webdriver

driver=webdriver.Chrome("../tools/chromedriver.exe")
driver.maximize_window()
driver.get("file:///G:/Google%20Chrome/selenium_pages-master/swtich_window_sample.html")
driver.find_element_by_tag_name("a").click()
windows=driver.window_handles
driver.switch_to_window(windows[1])
bing=driver.title
print(bing)
if (bing=="微软 Bing 搜索 - 国内版"):
    print("测试成功，成功打开bing网站...")
else:
    print("测试失败...")
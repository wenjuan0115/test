from selenium import webdriver

driver=webdriver.Chrome("../tools/chromedriver.exe")
driver.maximize_window()
driver.get("file:///G:/Google%20Chrome/selenium_pages-master/iframe_sample.html")

driver.switch_to_frame('innerFrame')
elements = driver.find_elements_by_class_name('plant')
for element in elements:
    print(element.text)
from selenium import webdriver

# 请在Chrome方法中，传入驱动的字符串路径
driver = webdriver.Chrome("d:/webdrivers/chromedriver.exe")
driver.get("https://www.python.org")
assert "Python" in driver.title


from selenium import webdriver

# 请在firefox方法中，传入驱动的字符串路径
driver = webdriver.Firefox("d:\webdrivers\geckodriver.exe")
driver.get("https://www.selenium.dev")
assert "Python" in driver.title

from selenium import webdriver

# 请在Edge 方法中，传入驱动的字符串路径
driver = webdriver.Edge("d:\webdrivers\msedgedriver.exe")
driver.get("https://www.selenium.dev")
assert "Python" in driver.title
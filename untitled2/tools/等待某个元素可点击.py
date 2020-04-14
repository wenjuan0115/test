from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome("../tools/chromedriver.exe")
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")
driver.maximize_window()
try:
    element = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.mnav:nth-child(2)')))
    print("等待中......")
    element.click()
    print("当前页面标题是:",driver.title)
except:
    print("页面显示错误.....")
finally:
    time.sleep(5)
    driver.close()


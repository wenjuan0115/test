import pytest
from selenium import webdriver
import os
from selenium.webdriver.chrome.options import Options as CH_Options
from selenium.webdriver.firefox.options import Options as FF_Options





BASE_DIR=os.path.dirname(os.path.abspath(__file__))
REPORT_DIR=BASE_DIR+"/report/"
driver=None


driver_type="chrome"

url="https://www.baidu.com"



cases_path="./testcases/"


@pytest.fixture(scope="function")
def base_url():
    global url
    return url


@pytest.fixture(scope='session',autouse=True)
def browser():
    global driver
    global driver_type

    if driver_type=="chrome":
        driver=webdriver.Chrome()
        driver.set_window_size(1920,1080)


    elif driver_type=="firefox":
        driver=webdriver.Firefox()
        driver.set_window_size(1920, 1080)


    elif driver_type=="chrome-headless":
        chrome_options=CH_Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disanle-gpu")
        chrome_options.add_argument("--windows-size=1920x1080")
        driver=webdriver.Chrome(options=chrome_options)


    elif driver_type == "firefox-headless":
        firefox_options=FF_Options
        firefox_options.headless=True
        driver = webdriver.Firefox(firefox_options=firefox_options)
    else:
        raise NameError("driver驱动类型定义错误！")

    return driver

@pytest.fixture(scope='session',autouse=True)
def browser_close():
    yield driver
    driver.quit()
    print("test end!")
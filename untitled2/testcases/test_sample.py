import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

class TestBaiduSearch:

    @pytest.fixture(scope="class")
    def init_driver(self):
        driver = webdriver.Chrome()
        yield driver
        driver.quit()


    @pytest.mark.usefixtures('init_drver')
    def test_search(self,init_driver):
        init_driver.get("https://www.baidu.com")
        ele = init_driver.find_element_by_id("kw")
        ele.send_keys("selenium" +Keys.RETURN)
        time.sleep(10)

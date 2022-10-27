import unittest
import time
from selenium import webdriver
import selenium
from Pages.PageIndex import *
from Pages.PageLogin import *
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

class Mistest(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        self.driver = webdriver.Chrome(options=options, executable_path=r'chromedriver.exe')
        self.driver.get('http://the-internet.herokuapp.com/')
        self.page_index = Pageindex(self.driver)
        self.page_log = PageLogin(self.driver)
        self.driver.implicitly_wait(5)
    def test_drop(self):
        self.page_index.test_dropdown()
    def test_log(self):
        self.page_log.test_login()
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
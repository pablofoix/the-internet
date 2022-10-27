import unittest
import time
from selenium import webdriver
import selenium
from selenium.webdriver.common import by
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

class PageLogin():
    def __init__(self,myDriver):
        self.driver = myDriver
        self.form_authentication = (By.LINK_TEXT,"Form Authentication")
        self.user_box = (By.NAME,"username")
        self.pass_box = (By.NAME,"password")
        self.login = (By.ID,"login")
        self.logout = (By.LINK_TEXT,"Elemental Selenium")
    def test_login(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(*self.form_authentication).click()
        self.driver.find_element(*self.user_box).send_keys("tomsmith")
        self.driver.find_element(*self.pass_box).send_keys("SuperSecretPassword!")
        try:
         boton = WebDriverWait(self.driver,5).until(expected_conditions.element_to_be_clickable(self.login))
        except:
            print("error")
        self.driver.find_element(*self.login).submit()
        tc = unittest.TestCase('__init__')
        tc.assertEqual((self.driver.find_element(*self.logout)).text,"Elemental Selenium")
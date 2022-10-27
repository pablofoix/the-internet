import unittest
import time
from selenium import webdriver
import selenium
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

class Pageindex():
   def __init__(self,myDriver):
      self.driver = myDriver
      self.drop_in = (By.LINK_TEXT,"Dropdown")
      self.dropdown = (By.ID,"dropdown")
   def test_dropdown(self):
      self.driver.implicitly_wait(5)
      self.driver.find_element(*self.drop_in).click()
      Select(self.driver.find_element(*self.dropdown)).select_by_value("1")
      tc = unittest.TestCase('__init__')
      tc.assertTrue(Select(self.driver.find_element(*self.dropdown)).first_selected_option.text.strip()=="Option 1")
import time
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options, executable_path=r'chromedriver.exe')
driver.get('http://the-internet.herokuapp.com/')
time.sleep(2)
form_authentication = driver.find_element_by_link_text("Form Authentication")
form_authentication.click()
user_box = driver.find_element_by_name("username")
pass_box = driver.find_element_by_name("password")
user_box.send_keys("tomsmith")
pass_box.send_keys("SuperSecretPassword!")
#login_button = driver.find_element_by_class_name("radius")
#login_button.click()
login = driver.find_element_by_id("login")
login.submit()
time.sleep(2)
logout = driver.find_element_by_link_text("Elemental Selenium")
assert logout.text == "Elemental Selenium"
print ("pase por aqui")
driver.quit()
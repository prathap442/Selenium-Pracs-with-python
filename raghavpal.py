from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest
import pdb
import time

driver = webdriver.Chrome()
driver.set_page_load_timeout(10)
driver.maximize_window()
driver.refresh()
print("Hello")
a = 10
b = 20
c = a + b
print(c)
driver.get("http://google.com")
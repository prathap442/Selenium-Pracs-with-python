from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
#The Keys class provide keys in the keyboard like RETURN, F1, ALT etc.
'''
 The attributes that are available for a By Class are 
 ID = "id"
    XPATH = "xpath"
    LINK_TEXT = "link text"
    PARTIAL_LINK_TEXT = "partial link text"
    NAME = "name"
    TAG_NAME = "tag name"
    CLASS_NAME = "class name"
    CSS_SELECTOR = "css selector"
'''
import pdb

pdb.set_trace()
driver = webdriver.Chrome()
# This is used to get the webdriver that is chrome
driver.get("http://www.python.org")
# this is used to input the www.python.org in the url of the window
assert "Welcome" in driver.title
driver.getElement('ByName')
# Check weather there is a word by name Welcome in the Tab title
elem = driver.find_element_by_name("q")
# Find all the eelements by name attribute q

elem.clear()
#clear any prepopulated text if it exists
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()
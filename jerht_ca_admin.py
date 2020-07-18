from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest
import pdb

class JerhtCaAdmin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    
    def test_login_works(self):
        driver = self.driver
        # To go to the sight where we have one session here
        driver.get('http://ec2-34-226-191-16.compute-1.amazonaws.com/login')
        email_handler = driver.find_element_by_name('email')
        email_handler.clear()
        email_handler.send_keys('vinney@yopmail.com')
        email_handler.send_keys(Keys.TAB)
        password_handler = driver.find_element_by_name('password')
        password_handler.clear()
        password_handler.send_keys('password@123')
        password_handler.send_keys(Keys.RETURN)
        pdb.set_trace()
        assert "CERTIFICATES" in driver.page_source

    def test_employee_fileupload(self):
        
    
    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
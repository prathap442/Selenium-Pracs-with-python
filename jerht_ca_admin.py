from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest
import pdb
import time

BASE_URL = "http://ec2-34-226-191-16.compute-1.amazonaws.com"
class JerhtCaAdmin(unittest.TestCase):
    #setUp methods will be made to run before every test case .
    def setUp(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        # To go to the sight where we have one session here
        driver.get(BASE_URL + "/login")
        driver.get(BASE_URL+"/login")
        email_handler = driver.find_element_by_name('email')
        email_handler.clear()
        email_handler.send_keys('vinney@yopmail.com')
        email_handler.send_keys(Keys.TAB)
        password_handler = driver.find_element_by_name('password')
        password_handler.clear()
        password_handler.send_keys('password@123')
        password_handler.send_keys(Keys.RETURN)

    def tearDown(self):
        driver = self.driver
        #driver.close()    
    
    # def test_login_works(self):
    #     driver = self.driver
        
    def test_employee_fileupload(self):
        driver = self.driver
        print(driver.current_url)
        assert driver.page_source.find("CERTIFICATES")
        driver.get(BASE_URL+"/organization")
        pdb.set_trace()
        driver.findElement(By.xpath('//*[@id="root"]/div/div/div[1]/div/div[1]/div[2]/ul/a[2]')).click()



if __name__ == "__main__":
    unittest.main()
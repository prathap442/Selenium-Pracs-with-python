from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest
import pdb
import time
import os
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

BASE_URL = "http://ec2-34-226-191-16.compute-1.amazonaws.com"
class JerhtCaAdmin(unittest.TestCase):
    #setUp methods will be made to run before every test case .
    def setUp(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        # To go to the sight where we have one session here
        driver.get(BASE_URL + "/login")
        time.sleep(1)
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
        driver.close()
    
    # def test_create_role(self):
    #     time.sleep(4)
    #     driver.get("http://ec2-34-226-191-16.compute-1.amazonaws.com/organization/work-roles")
    #     buttonHandle = driver.find
    # def test_login_works(self):
    #     driver = self.driver
        
    def test_employee_fileupload(self):
        driver = self.driver
        print(driver.current_url)
        assert driver.page_source.find("CERTIFICATES")
        time.sleep(5)
        driver.get(BASE_URL+"/organization/work-roles")
        time.sleep(4)
        uploadButtonHandler = driver.find_element_by_class_name('upload_icon')
        uploadButtonHandler.click()
        time.sleep(5)
        uploadFileButtonHandler = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div/div/button[1]')
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div/div/button[1]'))).click()
        uploadFileButtonHandler.send_keys("role_9.xlsx")
        #pdb.set_trace()
        # driver.findElement(By.xpath('//*[@id="root"]/div/div/div[1]/div/div[1]/div[2]/ul/a[2]')).click()



if __name__ == "__main__":
    unittest.main()
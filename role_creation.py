from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest
import pdb
import time

BASE_URL = "http://ec2-34-226-191-16.compute-1.amazonaws.com"
driver = webdriver.Chrome()
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
time.sleep(3)
driver.get(BASE_URL+"/organization/work-roles")
time.sleep(2)
NewRoleHandler = driver.find_element_by_xpath('//*[@id="root"]/div/div/div[3]/div[2]/div/div[1]/div[1]/div[2]')
NewRoleHandler.click()
time.sleep(2)
#form creation starts
role_id_text_handler = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div/form/div[2]/div[1]/div/div[2]/input')
role_id_text_handler.send_keys("ROLE-32323")
role_name_handler = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div/form/div[3]/div[1]/div/div[2]/input')
role_name_handler.send_keys("ROLE ABHI")
role_submit_handler = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div/form/div[4]/button[2]')
role_submit_handler.click()
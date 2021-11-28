import os
import time
import pytest
from selenium import webdriver
import unittest
from Pages.loginPage import loginPage



class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver
        driver.get("https://www.carlist.my/")
        select_page = loginPage(driver)
        time.sleep(5)
        select_page.carlist_dropdown()
        time.sleep(5)
        select_page.carlist_searchButton()
        time.sleep(5)
        select_page.carlist_firstCarPrice()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("test complete")








#        login_page.login("yw.tan2006@gmail.com", "mxpxpx")
#        time.sleep(10)



#if __name__ == 'main':
#    unittest.main()


from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import re

class loginPage():

    def __init__(self, driver: webdriver):
        self.driver = driver

        self.SearchButton = "/html/body/main/div[2]/div[2]/div[1]/div/div/div[2]/form/div[7]/button"
        self.AllConditionCheckBox = "//body/main[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/label[1]"
        self.UsedCheckBox = "//body/main[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/form[1]/div[1]/div[2]/label[1]"
        self.ClickDropdown = "/html/body/main/div[2]/div[2]/div[1]/div/div/div[2]/form/div[1]/div/div[1]/input"
        self.CarPrice = "/html/body/main/div[2]/div/div/div/div/section/article[1]/div/div/div[3]/div[1]/div/div/div/div[2]/span"
                        
        #self.FirstCar = "/html/body/main/article/section/section[3]/section[7]/div/section[2]/div/div/div/div[1]/div/div[2]/div[1]"

    def carlist_ucb(self):
        self.driver.find_element_by_xpath(self.UsedCheckBox).select()
        #select.select_by_value('Used')

    def carlist_searchButton(self):
        self.driver.find_element_by_xpath(self.SearchButton).click()

    def carlist_dropdown(self):
        self.driver.find_element_by_xpath(self.ClickDropdown).send_keys("Used")
        self.driver.find_element_by_xpath(self.ClickDropdown).send_keys(Keys.RETURN)

    def carlist_firstCarPrice(self):

        self.driver.find_element_by_xpath(self.CarPrice).text
        #re.search(@"[^\d.]", ""),price)















#    def login(self, user_email, user_password):
#        self.send_keys(self.driver.find_element_by_id(self.login_gmail_id), user_email)
#        self.send_keys(self.driver.find_element_by_name(self.pass_gmail_name), user_password)

#    def send_keys(self, ele, key):
#        ele.clear()
#        ele.send_keys(key)
#        ele.send_keys(Keys.ENTER)
import os
import time
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')
driver.get("https://www.carlist.my/")

#chromedriver = "/usr/local/bin/chromedriver"
#os.environ["webdriver.chrome.driver"] = chromedriver
#driver = webdriver.Chrome(chromedriver)
#driver.get("https://www.carlist.my/")
#time.sleep(10)

def test_login():
    print("start test")
    selectUsed = Select(driver.find_element_by_xpath("/body/main/div[2]/div[2]/div[1]/div/div/div[2]/form/div[1]/div/div[1]/div"))
    selectUsed.select_by_value("Used")






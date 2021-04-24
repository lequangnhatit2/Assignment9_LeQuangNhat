from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time
# mở bằng chrome
chrome_driver_path = "E:\Kemthu\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)

driver.get("http://practice.automationtesting.in/")
elementaccount = driver.find_element_by_id("menu-item-50")
elementaccount.click()
email = driver.find_element_by_name("email")
email.send_keys("nhatle211100@gmail.com")
time.sleep(2)
password = driver.find_element_by_id("reg_password")
password.send_keys("nhatly1006")
time.sleep(2)
register = driver.find_element_by_name("register")
register.click()
time.sleep(3)
driver.close()
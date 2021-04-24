from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os, time
# mở bằng chrome
chrome_driver_path = "E:\Kemthu\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)

driver.get("http://practice.automationtesting.in/")
time.sleep(5)
driver.close()

# mở bằng firefox

# driver = webdriver.Firefox(executable_path="E:\Kemthu\geckodriver-v0.29.1-win64\geckodriver.exe")

# driver.get("http://practice.automationtesting.in/")
# driver.quit()
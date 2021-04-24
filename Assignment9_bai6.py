from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time
# mở bằng chrome
chrome_driver_path = "E:\Kemthu\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)

driver.get("http://practice.automationtesting.in/")
driver.set_window_size(500, 500)
driversource = driver.page_source
print(driversource)
time.sleep(7)
driver.close()
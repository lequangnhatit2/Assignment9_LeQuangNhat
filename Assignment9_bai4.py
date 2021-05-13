from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time
# mở bằng chrome
chrome_driver_path = "E:\Kemthu\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)

driver.get("http://practice.automationtesting.in/")
driver.maximize_window()
try:
	assert "Automation Practice Site" in driver.title
	print(driver.title)
	print('OK')
	time.sleep(2)
	driver.close()

except Exception as e:
	print(e)

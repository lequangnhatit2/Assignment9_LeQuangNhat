from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time
# mở bằng chrome
chrome_driver_path = "E:\Kemthu\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)

driver.get("https://the-internet.herokuapp.com")

form = driver.find_element_by_css_selector("li:nth-child(21) > a")
form.click()

user = driver.find_element_by_id("username")
user.send_keys(" tomsmith")

time.sleep(2)

password = driver.find_element_by_id("password")
password.send_keys("SuperSecretPassword!")

time.sleep(2)

button = driver.find_element_by_xpath("//form[@id='login']/button/i")
button.click()

time.sleep(2)

title1 = driver.find_elements_by_id("flash")
print(title1)
assert "The Internet" in driver.title
print(driver.title)

time.sleep(2)
driver.close()

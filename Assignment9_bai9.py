from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
# mở bằng chrome
chrome_driver_path = "E:\Kemthu\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)

driver.get("https://itmscoaching.herokuapp.com/form")
time.sleep(2)
firstname = driver.find_element_by_id("first-name")
firstname.send_keys("Binh")
time.sleep(2)
lastname = driver.find_element_by_id("last-name")
lastname.send_keys("Nguyen")
time.sleep(2)
jobtitle = driver.find_element_by_id("job-title")
jobtitle.send_keys("Tester")
time.sleep(2)
higheastlevel = driver.find_element_by_id("radio-button-3")
higheastlevel.click()
time.sleep(2)
Sex = driver.find_element_by_id("checkbox-2")
Sex.click()
time.sleep(2)
Yearofexpperience = driver.find_element_by_id("select-menu")
time.sleep(2)
select = Select(Yearofexpperience)
select.select_by_visible_text("5-9")
time.sleep(2)
datepicker = driver.find_element_by_id("datepicker")
datepicker.click()
datepicker.send_keys("07/27/2011")
time.sleep(2)
Ok = driver.find_elements_by_link_text("Submit")
if len(Ok) > 0 :
    Ok[0].click()

time.sleep(2)
driver.close()




from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.techlistic.com/p/selenium-practice-form.html")
firstname=driver.find_element(By.XPATH,"(//input[@type='text'])[1]")
firstname.clear()
firstname.send_keys("vimal")
time.sleep(2)

secname=driver.find_element(By.XPATH,"(//input[@type='text'])[2]")
secname.clear()
secname.send_keys("raj")
time.sleep(3)

driver.quit()
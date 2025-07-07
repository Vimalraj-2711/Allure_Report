import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@allure.title("Techlistic Form Input Test")
@allure.description("Fill in first name and last name fields on selenium-practice-form.html")
def test_fill_names():
    driver = webdriver.Chrome()
    driver.get("https://www.techlistic.com/p/selenium-practice-form.html")

    with allure.step("Fill First Name"):
        firstname = driver.find_element(By.XPATH, "(//input[@type='text'])[1]")
        firstname.clear()
        firstname.send_keys("vimal")
        time.sleep(2)

    with allure.step("Fill Last Name"):
        secname = driver.find_element(By.XPATH, "(//input[@type='text'])[2]")
        secname.clear()
        secname.send_keys("raj")
        time.sleep(3)

    driver.quit()

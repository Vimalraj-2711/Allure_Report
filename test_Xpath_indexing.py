import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@allure.title("DemoQA Form Fill Test")
@allure.description("Fill the basic information fields in the DemoQA automation practice form.")
def test_demoqa_form():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/automation-practice-form")

    with allure.step("Fill First Name"):
        firstname = driver.find_element(By.XPATH, "(//input[@type='text'])[1]")
        firstname.send_keys("Vimal")
        time.sleep(2)

    with allure.step("Fill Last Name"):
        driver.find_element(By.XPATH, "(//input[@type='text'])[2]").send_keys("raj")
        time.sleep(2)

    with allure.step("Fill Email"):
        driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("sjfniouef@fowi.com")

    with allure.step("Fill Mobile Number"):
        driver.find_element(By.XPATH, "(//input[@type='text'])[4]").send_keys("6494987")

    with allure.step("Select Gender"):
        driver.find_element(By.XPATH, "//label[text()='Male']").click()
        time.sleep(2)

    driver.quit()

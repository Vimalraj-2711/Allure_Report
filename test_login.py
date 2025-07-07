import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@allure.title("Login Test")
@allure.description("Test login functionality with valid credentials.")
def test_login_success():
    driver = webdriver.Chrome()
    driver.get("https://practicetestautomation.com/practice-test-login/")

    with allure.step("Enter username"):
        username = driver.find_element(By.ID, "username")
        username.send_keys("student")

    with allure.step("Enter password"):
        password = driver.find_element(By.ID, "password")
        password.send_keys("Password123")

    with allure.step("Click submit button"):
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

    time.sleep(2)

    with allure.step("Verify login success message"):
        msd = driver.find_element(By.TAG_NAME, "h1").text
        if "Logged In Successfully" in msd:
            print("Successfully")
        else:
            pytest.fail("Login failed: success message not found")

    driver.quit()

import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@allure.title("JavaScript Alerts Test")
@allure.description("Test JS Alert, Confirm and Prompt on the-internet.herokuapp.com")
def test_js_alerts():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    with allure.step("Click 'Click for JS Alert' and accept alert"):
        menu = driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']")
        menu.click()
        time.sleep(3)
        alert = driver.switch_to.alert
        print("Alert Text:", alert.text)
        alert.accept()

        result = driver.find_element(By.XPATH, "//p[@id='result']").text
        print("Result message:", result)

    with allure.step("Click 'Click for JS Confirm' and dismiss alert"):
        driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
        time.sleep(3)
        alert = driver.switch_to.alert
        print("Alert:", alert.text)
        alert.dismiss()
        time.sleep(5)

        result = driver.find_element(By.XPATH, "//p[@id='result']").text
        print("Result message:", result)

    with allure.step("Click 'Click for JS Prompt', send keys and accept alert"):
        driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()
        time.sleep(3)

        alert = driver.switch_to.alert
        print("Alert:", alert.text)
        alert.send_keys("Vimal")
        time.sleep(3)
        alert.accept()
        time.sleep(3)

        result = driver.find_element(By.XPATH, "//p[@id='result']").text
        print("Result message:", result)

    driver.quit()

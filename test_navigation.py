import pytest
import allure
from selenium import webdriver
import time

@allure.title("Browser Navigation Test")
@allure.description("Test browser navigation: open, back, forward, refresh, and get URL.")
def test_browser_navigation():
    driver = webdriver.Chrome()
    driver.maximize_window()

    with allure.step("Open Google"):
        driver.get("https://www.google.com")
        print("Opened:", driver.title)
        time.sleep(2)

    with allure.step("Navigate to Wikipedia"):
        driver.get("https://www.wikipedia.org")
        print("Opened:", driver.title)
        time.sleep(2)

    with allure.step("Go back to Google"):
        driver.back()
        print("Back to:", driver.title)
        time.sleep(2)

    with allure.step("Go forward to Wikipedia"):
        driver.forward()
        print("Forward to:", driver.title)
        time.sleep(2)

    with allure.step("Refresh Wikipedia"):
        driver.refresh()
        print("Page refreshed:", driver.title)
        time.sleep(2)

    with allure.step("Print current URL"):
        print("Current URL:", driver.current_url)

    driver.quit()

import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@allure.title("Test Navigation Menu Links")
@allure.description("Verify each main menu link opens the expected page.")
def test_menu_links():
    driver = webdriver.Chrome()
    driver.get("https://practicetestautomation.com")

    menu_links = {
        "PRACTICE": "practice",
        "BLOG": "blog",
        "COURSES": "courses",
        "CONTACT": "contact"
    }

    for link_text, expected_url in menu_links.items():
        with allure.step(f"Click on menu link: {link_text}"):
            menu_link = driver.find_element(By.LINK_TEXT, link_text)
            menu_link.click()
            time.sleep(2)
            current_url = driver.current_url

        with allure.step(f"Verify URL contains '{expected_url}'"):
            if expected_url in current_url:
                print(f"Opened {expected_url} successfully")
            else:
                pytest.fail(f"Failed to open {expected_url} page. Current URL: {current_url}")

        with allure.step("Navigate back to homepage"):
            driver.get("https://practicetestautomation.com")
            time.sleep(1)

    driver.quit()

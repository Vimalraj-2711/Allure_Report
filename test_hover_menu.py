import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@allure.title("Hover Menu Interaction Test")
@allure.description("Verify multi-level menu hover functionality on demoqa.com/menu.")
def test_hover_menu():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://demoqa.com/menu")

    wait = WebDriverWait(driver, 10)
    actions = ActionChains(driver)

    with allure.step("Hover over 'Main Item 2'"):
        main_item2 = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text()='Main Item 2']")))
        driver.execute_script("arguments[0].scrollIntoView(true)", main_item2)
        actions.move_to_element(main_item2).perform()
        time.sleep(1)

    with allure.step("Hover over 'SUB SUB LIST »'"):
        sub_sub_list = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text()='SUB SUB LIST »']")))
        actions.move_to_element(sub_sub_list).perform()
        time.sleep(1)

    with allure.step("Hover over 'Sub Sub Item 2'"):
        sub_sub_item2 = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text()='Sub Sub Item 2']")))
        actions.move_to_element(sub_sub_item2).perform()
        time.sleep(1)

    with allure.step("Log hover success"):
        print("Hovering completed successfully")

    driver.quit()

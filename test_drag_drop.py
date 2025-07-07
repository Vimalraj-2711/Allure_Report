import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

@allure.title("Drag and Drop Test")
@allure.description("Verify drag and drop functionality on jQuery UI droppable demo.")
def test_drag_and_drop():
    driver = webdriver.Chrome()
    driver.maximize_window()

    with allure.step("Open jQuery UI Droppable demo page"):
        driver.get("https://jqueryui.com/droppable/")

    with allure.step("Switch to demo iframe"):
        iframe = driver.find_element(By.CLASS_NAME, "demo-frame")
        driver.switch_to.frame(iframe)

    with allure.step("Perform drag and drop"):
        source = driver.find_element(By.ID, "draggable")
        target = driver.find_element(By.ID, "droppable")
        actions = ActionChains(driver)
        actions.drag_and_drop(source, target).perform()
        time.sleep(5)

    with allure.step("Verify drop was successful"):
        dropped_text = target.text
        if "Dropped" in dropped_text:
            print("Drag and drop successful")
        else:
            pytest.fail("Drag and drop failed")

    driver.quit()

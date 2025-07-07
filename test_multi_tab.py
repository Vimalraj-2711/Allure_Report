import pytest
import allure
from selenium import webdriver
import time

@allure.title("Test Multi-Tab Handling")
@allure.description("Open Google, open Wikipedia in new tab, verify title, and close tabs.")
def test_multi_tab_handling():
    driver = webdriver.Chrome()
    
    with allure.step("Open Google homepage"):
        driver.get("https://www.google.com")
    
    with allure.step("Open Wikipedia in a new tab"):
        driver.execute_script("window.open('https://www.wikipedia.org', '_blank');")
        time.sleep(2)  # wait for tab to open
    
    with allure.step("Switch to Wikipedia tab and verify title"):
        tabs = driver.window_handles
        driver.switch_to.window(tabs[1])
        print("Title:", driver.title)
    
    with allure.step("Close Wikipedia tab"):
        driver.close()
    
    with allure.step("Switch back to Google tab"):
        driver.switch_to.window(tabs[0])
    
    driver.quit()

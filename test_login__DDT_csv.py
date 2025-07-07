import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time

@allure.title("DemoQA Login Test - Data Driven")
@allure.description("Attempt login on DemoQA with multiple credentials from CSV.")
def test_login_with_csv():
    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    driver.get("https://demoqa.com/login")

    with open(r"C:\Users\Administrator\Desktop\python\week2\data.csv", 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            username = row['username']
            password = row['password']

            with allure.step(f"Attempt login with username: {username}"):
                user_input = wait.until(EC.visibility_of_element_located((By.ID, "userName")))
                driver.execute_script("arguments[0].scrollIntoView(true);", user_input)
                ActionChains(driver).move_to_element(user_input).perform()
                user_input.clear()
                user_input.send_keys(username)

                pass_input = wait.until(EC.visibility_of_element_located((By.ID, "password")))
                driver.execute_script("arguments[0].scrollIntoView(true);", pass_input)
                ActionChains(driver).move_to_element(pass_input).perform()
                pass_input.clear()
                pass_input.send_keys(password)

                login_button = wait.until(EC.visibility_of_element_located((By.ID, "login")))
                driver.execute_script("arguments[0].scrollIntoView(true);", login_button)
                login_button.click()

                time.sleep(2)  # wait for page to respond

                if "Invalid" in driver.page_source:
                    print(f" Login failed for user: {username}")
                    allure.attach(body=f"Login failed for user: {username}", name="Login Result", attachment_type=allure.attachment_type.TEXT)
                else:
                    print(f"Login succeeded for user: {username}")
                    allure.attach(body=f"Login succeeded for user: {username}", name="Login Result", attachment_type=allure.attachment_type.TEXT)

                driver.get("https://demoqa.com/login")

    driver.quit()

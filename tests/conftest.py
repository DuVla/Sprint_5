import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data_generators import generate_login, generate_password
from locators import (REGISTER_EMAIL_INPUT,
                      REGISTER_NAME_INPUT,
                      LOGIN_BUTTON,
                      LOGIN_PASSWORD_INPUT)

BASE_URL = "https://stellarburgers.education-services.ru"

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def user_credentials():
    return {
        "email": generate_login(),
        "password": generate_password()
    }

# Регистрация нового пользователя, вход пользователя
@pytest.fixture
def logged_in_user(driver, user_credentials):
    driver.get(f"{BASE_URL}/register")
    driver.find_element(*REGISTER_NAME_INPUT).send_keys("Тест Тестов")
    driver.find_element(*REGISTER_EMAIL_INPUT).send_keys(user_credentials["email"])
    driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(user_credentials["password"])
    driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']").click()
    WebDriverWait(driver, 5).until(expected_conditions.url_to_be(f"{BASE_URL}/login"))

    driver.find_element(By.NAME, "name").send_keys(user_credentials["email"])
    driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(user_credentials["password"])
    driver.find_element(*LOGIN_BUTTON).click()
    WebDriverWait(driver, 5).until(expected_conditions.url_to_be(f"{BASE_URL}/"))

    return driver
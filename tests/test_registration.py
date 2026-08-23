from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import (REGISTER_NAME_INPUT,
                      REGISTER_EMAIL_INPUT,
                      LOGIN_PASSWORD_INPUT,
                      PASSWORD_ERROR)

BASE_URL = "https://stellarburgers.education-services.ru"
# Регистрация
def test_successful_registration(driver, user_credentials):
    driver.get(f"{BASE_URL}/register")

    driver.find_element(*REGISTER_NAME_INPUT).send_keys("Тест Тестов")
    driver.find_element(*REGISTER_EMAIL_INPUT).send_keys(user_credentials["email"])
    driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(user_credentials["password"])

    driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']").click()

    WebDriverWait(driver, 5).until(
        expected_conditions.url_to_be(f"{BASE_URL}/login")
    )
    assert driver.current_url == f"{BASE_URL}/login"

# Некорректный пароль
def test_registration_with_incorrect_passwort(driver, user_credentials):
    driver.get(f"{BASE_URL}/register")

    driver.find_element(*REGISTER_NAME_INPUT).send_keys("Тест Тестов")
    driver.find_element(*REGISTER_EMAIL_INPUT).send_keys(user_credentials["email"])
    driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys("1234")

    driver.find_element(By.XPATH, "//h2[text()='Регистрация']").click()

    error_message = driver.find_element(*PASSWORD_ERROR)
    assert error_message.text == 'Некорректный пароль'
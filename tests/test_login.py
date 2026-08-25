from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import (LOGIN_ACCOUNT_BUTTON,
                      PERSONAL_ACCOUNT_LINK,
                      LOGIN_LINK)

from config import BASE_URL


# вход по кнопке «Войти в аккаунт» на главной
class TestLogin:
    def test_login_main_page_button(self, driver):
        driver.get(BASE_URL)

        driver.find_element(*LOGIN_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.url_to_be(f"{BASE_URL}/login"))
        assert driver.current_url == f"{BASE_URL}/login"

    # вход через кнопку «Личный кабинет»
    def test_login_personal_account_link(self, driver):
        driver.get(BASE_URL)

        driver.find_element(*PERSONAL_ACCOUNT_LINK).click()
        WebDriverWait(driver, 5).until(expected_conditions.url_to_be(f"{BASE_URL}/login"))
        assert driver.current_url == f"{BASE_URL}/login"

    # вход через кнопку в форме регистрации
    def test_login_register_form(self, driver):
        driver.get(f"{BASE_URL}/register")

        driver.find_element(*LOGIN_LINK).click()
        WebDriverWait(driver, 5).until(expected_conditions.url_to_be(f"{BASE_URL}/login"))

        assert driver.current_url == f"{BASE_URL}/login"

    # вход через кнопку в форме восстановления пароля
    def test_login_forgot_password(self, driver):
        driver.get(f"{BASE_URL}/forgot-password")

        driver.find_element(*LOGIN_LINK).click()
        WebDriverWait(driver, 5).until(expected_conditions.url_to_be(f"{BASE_URL}/login"))

        assert driver.current_url == f"{BASE_URL}/login"
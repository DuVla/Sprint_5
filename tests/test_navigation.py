from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import (PERSONAL_ACCOUNT_LINK,
                      CONSTRUCTOR_LINK,
                      LOGO,
                      LOGOUT_BUTTON)

from config import BASE_URL


# переход в личный кабинет
class TestNavigation:
    def test_navigate_personal_account(self, logged_in_user):
        logged_in_user.find_element(*PERSONAL_ACCOUNT_LINK).click()
        WebDriverWait(logged_in_user, 10).until(expected_conditions.url_to_be(f"{BASE_URL}/account"))
        assert logged_in_user.current_url == f"{BASE_URL}/account"

# переход обратно в конструктор
    def test_navigate_back_constructor(self, logged_in_user):
        logged_in_user.find_element(*PERSONAL_ACCOUNT_LINK).click()
        WebDriverWait(logged_in_user, 10).until(expected_conditions.url_to_be(f"{BASE_URL}/account"))

        logged_in_user.find_element(*CONSTRUCTOR_LINK).click()
        WebDriverWait(logged_in_user, 5).until(expected_conditions.url_to_be(f"{BASE_URL}/"))
        assert logged_in_user.current_url == f"{BASE_URL}/"

# переход обратно в конструктор через лого в хедере
    def test_navigate_back_constructor_to_logo(self, logged_in_user):
        logged_in_user.find_element(*PERSONAL_ACCOUNT_LINK).click()
        WebDriverWait(logged_in_user, 10).until(expected_conditions.url_to_be(f"{BASE_URL}/account"))

        logged_in_user.find_element(*LOGO).click()
        WebDriverWait(logged_in_user, 5).until(expected_conditions.url_to_be(f"{BASE_URL}/"))
        assert logged_in_user.current_url == f"{BASE_URL}/"

# выход из личного кабинета
    def test_logout(self, logged_in_user):
        logged_in_user.find_element(*PERSONAL_ACCOUNT_LINK).click()
        WebDriverWait(logged_in_user, 10).until(expected_conditions.url_to_be(f"{BASE_URL}/account"))

        logout_button = WebDriverWait(logged_in_user, 10).until(
            expected_conditions.visibility_of_element_located(LOGOUT_BUTTON)
        )
        logout_button.click()

        WebDriverWait(logged_in_user, 5).until(expected_conditions.url_to_be(f"{BASE_URL}/login"))
        assert logged_in_user.current_url == f"{BASE_URL}/login"


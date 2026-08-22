import pytest
from selenium import webdriver
from data_generators import generate_login, generate_password

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

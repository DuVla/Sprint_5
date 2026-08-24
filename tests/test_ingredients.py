from selenium.webdriver.common.by import By

from locators import (BUNS,
                      SAUCES,
                      FILLINGS)

from conftest import BASE_URL


#булки
def test_buns(driver):
    driver.get(BASE_URL)

    tab_container = driver.find_element(By.XPATH, "//span[text()='Булки']/..")
    assert "tab_type_current" in tab_container.get_attribute("class")

#соусы
def test_sauces(driver):
    driver.get(BASE_URL)

    driver.find_element(*SAUCES).click()

    tab_container = driver.find_element(By.XPATH, "//span[text()='Соусы']/..")
    assert "tab_type_current" in tab_container.get_attribute("class")

#начинки
def test_fillings(driver):
    driver.get(BASE_URL)

    driver.find_element(*FILLINGS).click()

    tab_container = driver.find_element(By.XPATH, "//span[text()='Начинки']/..")
    assert "tab_type_current" in tab_container.get_attribute("class")



from locators import (SAUCES,
                      FILLINGS,
                      BUNS_CONTAINER,
                      SAUCES_CONTAINER,
                      FILLINGS_CONTAINER)

from config import BASE_URL



#булки
class TestIngredients:
    def test_buns(self, driver):
        driver.get(BASE_URL)

        tab_container = driver.find_element(*BUNS_CONTAINER)
        assert "tab_type_current" in tab_container.get_attribute("class")

    #соусы
    def test_sauces(self, driver):
        driver.get(BASE_URL)

        driver.find_element(*SAUCES).click()

        tab_container = driver.find_element(*SAUCES_CONTAINER)
        assert "tab_type_current" in tab_container.get_attribute("class")

    #начинки
    def test_fillings(self, driver):
        driver.get(BASE_URL)

        driver.find_element(*FILLINGS).click()

        tab_container = driver.find_element(*FILLINGS_CONTAINER)
        assert "tab_type_current" in tab_container.get_attribute("class")



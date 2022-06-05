import pytest
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class Test_Oscar_Sandbox():

    def test_Add_to_basket_button(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        browser.get(link)
        time.sleep(5)
        result = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
        assert result != [], "The \"Add to basket\" button does not exist"
        

if __name__ == "__main__":
    pytest.main()

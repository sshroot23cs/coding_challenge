from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.common_page_elements import CommonPageElements
from src.helper import Helper


class HomePage(CommonPageElements, Helper):
    LOCATOR_FILE = "home_page.yaml"

    def __init__(self, driver):
        super().__init__(driver)
        Helper().__init__()
        self.page_locators = self.get_locators(self.LOCATOR_FILE)

    def check_search_element(self):
        ele = self.get_page_element(self.page_locators["search-box"])
        return ele if ele else False

    def enter_stock_to_search(self, text):
        self.enter_text_to_element(self.page_locators["search-box"], text, is_enter=True)
        WebDriverWait(self.driver, 10).until(EC.title_contains(text))
        return True

    def navigate_to_most_active_page(self, page_title):
        self.click_element(self.page_locators["most-active"])
        WebDriverWait(self.driver, 10).until(EC.title_is(page_title))

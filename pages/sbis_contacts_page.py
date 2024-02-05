from selenium.webdriver.firefox.webdriver import WebDriver

from pages.base_page import BasePage
from pages.tensor_root_page import TensorRootPage


class SbisContactsPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.url = 'https://sbis.ru'

    def go_to_tensor_root_page(self) -> TensorRootPage:
        return TensorRootPage(self.driver)

from selenium.webdriver.chrome.webdriver import WebDriver

from pages.base_page import BasePage
from pages.tensor_about_page import TensorAboutPage


class TensorRootPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.url = 'https://tensor.ru'

    def go_to_tensor_about_page(self) -> TensorAboutPage:
        return TensorAboutPage(self.driver)

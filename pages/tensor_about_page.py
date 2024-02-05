from selenium.webdriver.firefox.webdriver import WebDriver

from pages.base_page import BasePage


class TensorAboutPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.url = 'https://tensor.ru/about'

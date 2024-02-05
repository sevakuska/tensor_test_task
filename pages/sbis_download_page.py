from selenium.webdriver.chrome.webdriver import WebDriver

from pages.base_page import BasePage


class SbisDownloadPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.url = 'https://sbis.ru/download'

from selenium.webdriver.firefox.webdriver import WebDriver

from pages.base_page import BasePage
from pages.sbis_contacts_page import SbisContactsPage


class SbisRootPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.url = 'https://sbis.ru'

    def go_to_sbis_contacts_page(self) -> SbisContactsPage:
        return SbisContactsPage(self.driver)

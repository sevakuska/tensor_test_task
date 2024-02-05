from selenium.webdriver.chrome.webdriver import WebDriver

from pages.base_page import BasePage
from pages.sbis_contacts_page import SbisContactsPage
from pages.sbis_download_page import SbisDownloadPage


class SbisRootPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.url = 'https://sbis.ru'

    def go_to_sbis_contacts_page(self) -> SbisContactsPage:
        return SbisContactsPage(self.driver)

    def go_to_sbis_download_page(self) -> SbisDownloadPage:
        return SbisDownloadPage(self.driver)

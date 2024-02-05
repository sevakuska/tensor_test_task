from selenium.webdriver import Chrome
from pages.sbis_root_page import SbisRootPage


def test_third_scenario(browser: Chrome) -> None:
    sbis_root_page = SbisRootPage(browser)
    sbis_root_page.open_site()

from pages.sbis_root_page import SbisRootPage


def test_3rd(browser):
    sbis_root_page = SbisRootPage(browser)
    sbis_root_page.open_site()

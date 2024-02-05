from time import sleep
from os import stat
from os import getcwd
from os import remove

from selenium.webdriver import Chrome
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.sbis_root_page import SbisRootPage
from locators.sbis_root_page_locators import SbisRootPageLocators
from locators.sbis_download_page_locators import SbisDownloadPageLocators


def test_third_scenario(browser: Chrome) -> None:
    sbis_root_page = SbisRootPage(browser)
    sbis_root_page.open_site()

    sbis_download = WebDriverWait(sbis_root_page.driver, 30).until(
        EC.visibility_of_element_located(SbisRootPageLocators.SBIS_DOWNLOAD_A)
    )

    assert sbis_download.text == 'Скачать СБИС'

    sbis_root_page.driver.execute_script(
        'arguments[0].click();',
        sbis_download
    )

    sbis_download_page = sbis_root_page.go_to_sbis_download_page()

    sbis_plugin = WebDriverWait(sbis_download_page.driver, 30).until(
        EC.visibility_of_element_located(
            SbisDownloadPageLocators.SBIS_PLUGIN_DIV
        )
    )

    assert sbis_plugin.text == 'СБИС Плагин'

    sbis_download_page.driver.get(
        'https://sbis.ru/download?tab=plugin&innerTab=default'
    )

    sbis_web_setup = WebDriverWait(sbis_download_page.driver, 30).until(
        EC.element_to_be_clickable(
            SbisDownloadPageLocators.SBIS_WEB_SETUP_A
        )
    )
    sbis_download_page.driver.execute_script(
        'arguments[0].click();',
        sbis_web_setup
    )

    sleep(5)

    filename = f'{getcwd()}/sbisplugin-setup-web.exe'
    stats = stat(filename)
    assert str(round(stats.st_size / (1024 * 1024), 2)) in sbis_web_setup.text

    remove(filename)

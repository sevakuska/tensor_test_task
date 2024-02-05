
from os import getcwd
from typing import Generator

from pytest import fixture
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions


@fixture(scope='session')
def browser() -> Generator[Chrome, None, None]:
    options = ChromeOptions()
    options.add_experimental_option(
        'prefs',
        {'download.default_directory': getcwd()}
    )

    driver = Chrome(options=options)
    driver.maximize_window()

    yield driver

    driver.quit()

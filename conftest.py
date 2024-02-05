from typing import Generator

from pytest import fixture
from selenium.webdriver import Chrome


@fixture(scope='session')
def browser() -> Generator[Chrome, None, None]:
    driver = Chrome()
    driver.maximize_window()

    yield driver

    driver.quit()

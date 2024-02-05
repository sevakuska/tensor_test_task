from pytest import fixture
from selenium.webdriver import Chrome


@fixture(scope='session')
def browser():
    driver = Chrome()
    driver.maximize_window()

    yield driver

    driver.quit()

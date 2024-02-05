from selenium.webdriver.firefox.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.url = None

    def open_site(self):
        if self.url is None:
            raise ValueError('URL is not set.')

        return self.driver.get(self.url)

    def find_element(self, locator: tuple[str, str]):
        return self.driver.find_element(*locator)

    @property
    def title(self):
        return self.driver.title

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class BasePage:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.url: str | None = None

    def open_site(self) -> None:
        if self.url is None:
            raise ValueError('URL is not set.')

        self.driver.get(self.url)

    def find_element(self, locator: tuple[str, str]) -> WebElement:
        return self.driver.find_element(*locator)

    @property
    def title(self) -> str:
        return self.driver.title

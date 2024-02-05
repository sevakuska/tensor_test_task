from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.webdriver import WebDriver


def wait_for_url_to_change(
    driver: WebDriver,
    old_url: str,
    timeout: int = 30
) -> None:
    def url_has_changed(driver: WebDriver) -> bool:
        return driver.current_url != old_url

    WebDriverWait(driver, timeout).until(url_has_changed)

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

from pages.sbis_root_page import SbisRootPage
from locators.sbis_root_page_locators import SbisRootPageLocators
from locators.sbis_contacts_page_locators import SbisContactsPageLocators
from locators.tensor_root_page_locators import TensorRootPageLocators
from locators.tensor_about_page_locators import TensorAboutPageLocators


def test_1st(browser):
    sbis_root_page = SbisRootPage(browser)
    sbis_root_page.open_site()

    sbis_contacts = sbis_root_page.find_element(
        SbisRootPageLocators.CONTACTS_A
    )
    WebDriverWait(sbis_root_page.driver, 30).until(
        EC.element_to_be_clickable(sbis_contacts)
    )

    assert sbis_contacts.text == 'Контакты'

    sbis_contacts.click()
    sbis_contacts_page = sbis_root_page.go_to_sbis_contacts_page()
    tensor = sbis_contacts_page.find_element(
        SbisContactsPageLocators.TENSOR_A
    )

    assert tensor.get_attribute('href') == 'https://tensor.ru/'

    sbis_contacts_page.driver.execute_script(
        'arguments[0].click();',
        tensor
    )
    sbis_contacts_page.driver.switch_to.window(
        sbis_contacts_page.driver.window_handles[1]
    )
    tensor_root_page = sbis_contacts_page.go_to_tensor_root_page()

    tensor_power_in_people = WebDriverWait(tensor_root_page.driver, 30).until(
        EC.visibility_of_element_located(
            TensorRootPageLocators.POWER_IN_PEOPLA_P
        )
    )

    try:
        assert tensor_power_in_people.text == 'Сила в людях'
    except StaleElementReferenceException:
        tensor_power_in_people = WebDriverWait(
            tensor_root_page.driver,
            30
        ).until(
            EC.visibility_of_element_located(
                TensorRootPageLocators.POWER_IN_PEOPLA_P
            )
        )
        assert tensor_power_in_people.text == 'Сила в людях'

    tensor_about_a = WebDriverWait(
        tensor_root_page.driver,
        30,
        ignored_exceptions=StaleElementReferenceException
    ).until(
        lambda x: x.find_element(*TensorRootPageLocators.ABOUT_A)
    )

    assert tensor_about_a.get_attribute('href') == 'https://tensor.ru/about'

    tensor_root_page.driver.execute_script(
        'arguments[0].click();',
        tensor_about_a
    )

    # ----------------------------------------------------------------------- #

    tensor_about_page = tensor_root_page.go_to_tensor_about_page()
    photos_locators = (
        TensorAboutPageLocators.PHOTO_1,
        TensorAboutPageLocators.PHOTO_2,
        TensorAboutPageLocators.PHOTO_3,
        TensorAboutPageLocators.PHOTO_4,
    )
    photos = (
        WebDriverWait(tensor_about_page.driver, 15).until(
            EC.visibility_of_element_located(photo_locator)
        )
        for photo_locator in photos_locators
    )
    photos_resolution = (
        (photo.get_attribute('width'), photo.get_attribute('height'))
        for photo in photos
    )

    assert len(set(photos_resolution)) == 1

from selenium.webdriver import Chrome
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.sbis_root_page import SbisRootPage
from locators.sbis_root_page_locators import SbisRootPageLocators
from locators.sbis_contacts_page_locators import SbisContactsPageLocators
from utils.url import wait_for_url_to_change


def test_second_scenario(browser: Chrome) -> None:
    sbis_root_page = SbisRootPage(browser)
    sbis_root_page.open_site()
    s_title = 'СБИС — экосистема для бизнеса: учет, управление и коммуникации'

    assert sbis_root_page.title == s_title

    sbis_contacts = WebDriverWait(sbis_root_page.driver, 30).until(
        EC.element_to_be_clickable(SbisRootPageLocators.CONTACTS_A)
    )

    assert sbis_contacts.tag_name == 'a'
    assert sbis_contacts.text == 'Контакты'

    sbis_contacts.click()
    sbis_contacts_page = sbis_root_page.go_to_sbis_contacts_page()

    selected_region = WebDriverWait(sbis_contacts_page.driver, 30).until(
        EC.element_to_be_clickable(
            SbisContactsPageLocators.SELECTED_REGION_SPAN
        )
    )

    assert selected_region.text == 'Свердловская обл.'

    selected_region.click()
    select_region = WebDriverWait(sbis_contacts_page.driver, 30).until(
        EC.element_to_be_clickable(
            SbisContactsPageLocators.SELECT_KAMCHATKA_SPAN
        )
    )
    select_region.click()

    wait_for_url_to_change(
        sbis_contacts_page.driver,
        'https://sbis.ru/contacts/66-sverdlovskaya-oblast?tab=clients'
    )

    url = 'https://sbis.ru/contacts/41-kamchatskij-kraj?tab=clients'
    city = WebDriverWait(sbis_contacts_page.driver, 30).until(
        EC.visibility_of_element_located(
            SbisContactsPageLocators.CITY
        )
    )
    office_name = WebDriverWait(sbis_contacts_page.driver, 30).until(
        EC.visibility_of_element_located(
            SbisContactsPageLocators.SBIS_KAMCHATKA
        )
    )
    office_address = WebDriverWait(sbis_contacts_page.driver, 30).until(
        EC.visibility_of_element_located(
            SbisContactsPageLocators.SBIS_KAMCHATKA_ADRESS
        )
    )

    assert sbis_contacts_page.driver.current_url == url
    assert city.text == 'Петропавловск-Камчатский'
    assert office_name.text == 'СБИС - Камчатка'
    assert office_address.text == 'ул.Ленинская, 59, оф.202, 205'

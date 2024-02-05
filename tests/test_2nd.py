from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.sbis_root_page import SbisRootPage
from locators.sbis_root_page_locators import SbisRootPageLocators
from locators.sbis_contacts_page_locators import SbisContactsPageLocators


def test_2nd(browser):
    sbis_root_page = SbisRootPage(browser)
    sbis_root_page.open_site()
    s_title = 'СБИС — экосистема для бизнеса: учет, управление и коммуникации'

    assert sbis_root_page.title == s_title

    sbis_contacts = sbis_root_page.find_element(
        SbisRootPageLocators.CONTACTS_A
    )
    WebDriverWait(sbis_root_page.driver, 30).until(
        EC.element_to_be_clickable(sbis_contacts)
    )

    assert sbis_contacts.tag_name == 'a'
    assert sbis_contacts.text == 'Контакты'

    sbis_root_page.driver.execute_script(
        'arguments[0].click();',
        sbis_contacts
    )
    sbis_contacts_page = sbis_root_page.go_to_sbis_contacts_page()

    selected_region = WebDriverWait(sbis_contacts_page.driver, 30).until(
        EC.element_to_be_clickable(
            SbisContactsPageLocators.SELECTED_REGION_SPAN
        )
    )

    assert selected_region.text == 'Свердловская обл.'
    sbis_contacts_page.driver.execute_script(
        'arguments[0].click();',
        selected_region
    )
    sbis_contacts_page.driver.execute_script(
        'arguments[0].click();',
        sbis_contacts_page.find_element(
            SbisContactsPageLocators.SELECT_KAMCHATKA_SPAN
        )
    )

    r = WebDriverWait(sbis_contacts_page.driver, 30).until(
        EC.visibility_of_element_located(
            SbisContactsPageLocators.A
        )
    )
    s = WebDriverWait(sbis_contacts_page.driver, 30).until(
        EC.visibility_of_element_located(
            SbisContactsPageLocators.SBIS_KAMCHATKA
        )
    )
    a = WebDriverWait(sbis_contacts_page.driver, 30).until(
        EC.visibility_of_element_located(
            SbisContactsPageLocators.SBIS_KAMCHATKA_ADRESS
        )
    )
    url = 'https://sbis.ru/contacts/41-kamchatskij-kraj?tab=clients'

    assert sbis_contacts_page.driver.current_url == url
    assert r.text == 'Петропавловск-Камчатский'
    assert s.text == 'СБИС - Камчатка'
    assert a.text == 'ул.Ленинская, 59, оф.202, 205'

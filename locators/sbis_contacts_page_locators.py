from selenium.webdriver.common.by import By


class SbisContactsPageLocators:
    TENSOR_A = (
        By.XPATH,
        ('/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]'
         '/div/div[4]/div[1]/div/div/div[2]/div/a')
    )
    SELECTED_REGION_SPAN = (
        By.XPATH,
        ('/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]'
         '/div/div[3]/div[2]/div[1]/div/div[2]/span/span')
    )
    SELECT_KAMCHATKA_SPAN = (
        By.XPATH,
        ('/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div[2]/div/u'
         'l/li[43]/span')
    )
    CITY = (
        By.XPATH,
        ('/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]'
         '/div/div[4]/div[3]/div/div[2]/div[2]/div/div[2]/div[1]/div[3]/div[1]'
         '/div/div')
    )
    SBIS_KAMCHATKA = (
        By.XPATH,
        ('/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]'
         '/div/div[4]/div[3]/div/div[2]/div[2]/div/div[2]/div[1]/div[3]/div[2]'
         '/div/div/div[1]/div[1]')
    )
    SBIS_KAMCHATKA_ADRESS = (
        By.XPATH,
        ('/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]'
         '/div/div[4]/div[3]/div/div[2]/div[2]/div/div[2]/div[1]/div[3]/div[2]'
         '/div/div/div[1]/div[2]/div[2]')
    )

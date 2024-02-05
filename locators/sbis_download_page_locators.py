from selenium.webdriver.common.by import By


class SbisDownloadPageLocators:
    SBIS_PLUGIN_DIV = (
        By.XPATH,
        ('/html/body/div[1]/div[2]/div[1]/div/div[1]/div/div/div/div[1]/div/di'
         'v/div/div[3]/div[2]/div[1]')
    )
    SBIS_WEB_SETUP_A = (
        By.XPATH,
        ('/html/body/div[1]/div[2]/div[1]/div/div[1]/div/div/div/div[2]/div/di'
         'v[2]/div/div/div[2]/div[1]/div[2]/div[2]/div/a')
    )

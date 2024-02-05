from selenium.webdriver.common.by import By


class SbisRootPageLocators:
    CONTACTS_A = (
        By.XPATH,
        ('/html/body/div[1]/div/div/div[2]/div[1]/div[1]/div[1]/div[2]/ul/''li'
         '[2]/a')
    )
    SBIS_DOWNLOAD_A = (
        By.XPATH,
        ('/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[2]'
         '/div[1]/div[3]/div[10]/ul/li[6]/a')
    )

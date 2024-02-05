from selenium.webdriver.common.by import By


class TensorRootPageLocators:
    POWER_IN_PEOPLA_P = (
        By.XPATH,
        ('/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]'
         '/div/div[5]/div/div/div[1]/div/p[1]')
    )
    ABOUT_A = (
        By.XPATH,
        ('/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]'
         '/div/div[5]/div/div/div[1]/div/p[4]/a')
    )

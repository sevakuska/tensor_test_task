from selenium.webdriver.common.by import By


class TensorAboutPageLocators:
    PHOTO_1 = (
        By.XPATH,
        ('/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]'
         '/div/div[4]/div[2]/div[1]/a/div[1]/img')
    )
    PHOTO_2 = (
        By.XPATH,
        ('/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]'
         '/div/div[4]/div[2]/div[2]/a/div[1]/img')
    )
    PHOTO_3 = (
        By.XPATH,
        ('/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]'
         '/div/div[4]/div[2]/div[3]/a/div[1]/img')
    )
    PHOTO_4 = (
        By.XPATH,
        ('/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]'
         '/div/div[4]/div[2]/div[4]/a/div[1]/img')
    )

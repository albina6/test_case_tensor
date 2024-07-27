from selenium.webdriver.common.by import By


class BaseLocatorsSBIS():
    CONTACTS_LINK = (By.CSS_SELECTOR, ".sbisru-Header__menu li:nth-child(2)")

class ContactsLocatorsSBIS():
    TENSOR_LOGO = (By.CSS_SELECTOR, "#contacts_clients a.sbisru-Contacts__logo-tensor")
    CONTAINER_REGION = (By.CSS_SELECTOR,\
        ".sbis_ru-container.sbisru-Contacts__relative span.sbis_ru-Region-Chooser__text")
    COUNTRY_FROM_REGION = (By.CSS_SELECTOR, "div[id='city-id-2']")
    DIALOG_REGION_ELEMENTS = (By.CSS_SELECTOR, "ul.sbis_ru-Region-Panel__list-l li > span")
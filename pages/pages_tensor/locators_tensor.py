from selenium.webdriver.common.by import By


class BaseLocatorsTensor():
    CARDS_DIV = (By.CSS_SELECTOR, "div.tensor_ru-Index__card")
    TITLE_IN_CARDS = (By.CSS_SELECTOR, "p:nth-child(1)")


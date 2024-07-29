from selenium.webdriver.common.by import By


class MainLocatorsTensor:
    CARDS_DIV = (By.CSS_SELECTOR, "div.tensor_ru-Index__card")
    TITLE_IN_CARDS = (By.CSS_SELECTOR, "p.tensor_ru-Index__card-title")
    REF_IN_CARDS = (By.CSS_SELECTOR, ".tensor_ru-link")


class AboutLocatorsTensor:
    BLOCK_WORKS = (By.CSS_SELECTOR, ".tensor_ru-container.tensor_ru-About__block3")
    IMG_IN_BLOCKS = (By.TAG_NAME, "img")

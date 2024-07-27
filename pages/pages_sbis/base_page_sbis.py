from ..base_page import BasePage
from .locators_sbis import BaseLocatorsSBIS

from selenium.common.exceptions import (NoSuchElementException)


class BasePageSBIS(BasePage):
    def go_to_contacts_page(self):
        contacts = self.browser.find_element(*BaseLocatorsSBIS.CONTACTS_LINK)
        contacts.click()

from .base_page_sbis import BasePageSBIS
from .locators_sbis import ContactsLocatorsSBIS
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ContactsPageSBIS(BasePageSBIS):
    def go_to_tensor(self):
        tensor_logo = self.browser.find_element(*ContactsLocatorsSBIS.TENSOR_LOGO)
        tensor_logo.click()

    def should_be_equal_enter_region_country(self, enter_region, enter_country):
        self.should_be_equal_check_region(enter_region)
        self.should_be_equal_check_country_region(enter_country)

    def should_be_equal_check_region(self, enter_region):
        region = self.browser.find_element(*ContactsLocatorsSBIS.CONTAINER_REGION)
        assert region.text == enter_region,\
            f"Region in page don't equal enter region\n {region.text} != {enter_region}"

    def should_be_equal_check_country_region(self, enter_country):
        country = self.browser.find_element(*ContactsLocatorsSBIS.COUNTRY_FROM_REGION)
        assert country.text == enter_country, \
            f"Country in page don't equal enter country\n {country.text} != {enter_country}"

    def should_be_enter_region_in_url(self, enter_region_url, timeout=5):
        try:
            WebDriverWait(self.browser, timeout).until(EC.url_contains(enter_region_url))
        except TimeoutException:
            assert False, \
                f"Current url don't have enter region url {enter_region_url} not in {self.browser.current_url}"

    def should_be_enter_region_in_title(self, enter_region, timeout=5):
        try:
            WebDriverWait(self.browser, timeout).until(EC.title_contains(enter_region))
        except TimeoutException:
            assert False, f"Current title don't have enter region {enter_region} not in {self.browser.title}"

    def change_to_enter_region_in_dialog(self, enter_region):
        '''
        In this function we use title ul.li elements, BUT
        visible text can be not equal this title( and text in top container and browser.title.)

        If you need check top container and browser.title after this function first use
        should_be_enter_region_in_title() or should_be_enter_region_in_url()
        this function use WebDriverWait
        and after should_be_equal_enter_region_country()
        '''
        region = self.browser.find_element(*ContactsLocatorsSBIS.CONTAINER_REGION)
        region.click()
        region_list = self.browser.find_elements(*ContactsLocatorsSBIS.DIALOG_REGION_ELEMENTS)
        flag_found = False
        for li_region in region_list:
            if enter_region == li_region.get_attribute("title"):
                flag_found = True
                li_region.click()
                break
        assert flag_found, f"Enter region ({enter_region}) don't found"


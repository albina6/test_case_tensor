import pytest
from .pages.pages_sbis.base_page_sbis import BasePageSBIS
from .pages.pages_sbis.contacts_page_sbis import ContactsPageSBIS

from .pages.pages_tensor.main_page_tensor import MainPageTensor
from .pages.pages_tensor.about_page import AboutPageTensor


class TestSBISGoToContact:
    @pytest.fixture()
    def base_page(self, browser):
        link = 'https://sbis.ru/'

        page = BasePageSBIS(browser, link)
        page.open()
        yield page

    def test_sbis_tensor_equal_size_imgs(self, base_page):
        #        This is First Script (question)
        enter_url = "https://tensor.ru/about"

        base_page.go_to_contacts_page()
        contacts_page = ContactsPageSBIS(base_page.browser, base_page.browser.current_url)
        contacts_page.go_to_tensor()

        contacts_page.browser.switch_to.window(contacts_page.browser.window_handles[1])
        main_page_tensor = MainPageTensor(contacts_page.browser, contacts_page.browser.current_url)
        main_page_tensor.should_be_present_cadre_power_in_people()
        main_page_tensor.go_to_details_in_cadre_power()

        about_page = AboutPageTensor(main_page_tensor.browser, main_page_tensor.browser.current_url)
        about_page.check_current_url_equal_enter_url(enter_url)
        about_page.should_be_equal_size_img_in_works_block()


    def test_sbis_contact_change_region(self, base_page):
        #        This Second Script (question)

        region_current = "Республика Башкортостан"
        country_current = "Уфа"
        # text title and container maybe isn't equal visible text ul/li
        # ("Респ. Кабардино-Балкария" != "Кабардино-Балкарская Республика")
        # That's why we use attribute title() in change_to_enter_region_in_dialog()
        # Value this attribute is visible when cursor on a li element
        region_final = "Камчатский край"
        country_final = "Петропавловск-Камчатский"
        part_url_final = "kamchatskij-kraj"

        base_page.go_to_contacts_page()
        contacts_page = ContactsPageSBIS(base_page.browser, base_page.browser.current_url)
        contacts_page.should_be_equal_enter_region_country(region_current, country_current)
        contacts_page.change_to_enter_region_in_dialog(region_final)

        contacts_page.should_be_enter_region_in_url(part_url_final)
        contacts_page.should_be_enter_region_in_title(region_final)
        contacts_page.should_be_equal_enter_region_country(region_final, country_final)


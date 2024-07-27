from pages.pages_sbis.base_page_sbis import BasePageSBIS
from pages.pages_sbis.contacts_page_sbis import ContactsPageSBIS

# from .pages.pages_tensor import Base


def test_sbis_tenzor_equal_imgs(browser):
    link = 'https://sbis.ru/'
    region_current = "Республика Башкортостан"
    country_current = "Уфа"
    # text title and container maybe isn't equal visible text ul/li
    # ("Респ. Кабардино-Балкария" != "Кабардино-Балкарская Республика")
    # That's why we use attribute title() in change_to_enter_region_in_dialog()
    # This attribute
    region_final = "Камчатский край"
    country_final = "Петропавловск-Камчатский"
    part_url_final = "kamchatskij-kraj"

    page = BasePageSBIS(browser, link)
    page.open()
    page.go_to_contacts_page()
    contacts_page = ContactsPageSBIS(page.browser, page.browser.current_url)
    contacts_page.should_be_equal_enter_region_country(region_current, country_current)
    contacts_page.change_to_enter_region_in_dialog(region_final)

    contacts_page.should_be_enter_region_in_url(part_url_final)
    contacts_page.should_be_enter_region_in_title(region_final)
    contacts_page.should_be_equal_enter_region_country(region_final, country_final)

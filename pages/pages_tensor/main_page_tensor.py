from .base_page_tensor import BasePageTensor
from .locators_tensor import BaseLocatorsTensor


class MainPageTensor(BasePageTensor):
    def cadr_power_in_people(self):
        cards_list = self.browser.find_elements(*BaseLocatorsTensor.CARDS_DIV)
        flag = False
        for card in cards_list:
            title = card.find_element(*BaseLocatorsTensor.TITLE_IN_CARDS)
            if title.text == "Сила в людях":
                flag = card
                break

        return flag

    def is_present_cadr_power_in_people(self):
        card_power = self.cadr_power_in_people()
        return bool(card_power)

    def go_to_details_in_card_power(self):
        card_power = self.cadr_power_in_people()
        


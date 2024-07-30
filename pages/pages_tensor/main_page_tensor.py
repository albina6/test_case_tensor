from .base_page_tensor import BasePageTensor
from .locators_tensor import MainLocatorsTensor


class MainPageTensor(BasePageTensor):
    def cadre_power_in_people(self):
        cards_list = self.browser.find_elements(*MainLocatorsTensor.CARDS_DIV)
        flag = False
        for card in cards_list:
            title = card.find_element(*MainLocatorsTensor.TITLE_IN_CARDS)
            if title.text == "Сила в людях":
                flag = card
                break

        return flag

    def should_be_present_cadre_power_in_people(self):
        card_power = self.cadre_power_in_people()
        assert bool(card_power), "Div 'Сила в людях' is not presented"

    def go_to_details_in_cadre_power(self):
        card_power = self.cadre_power_in_people()
        more_card_power = card_power.find_element(*MainLocatorsTensor.REF_IN_CARDS)
        self.click_element(more_card_power)

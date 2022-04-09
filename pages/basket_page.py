from .base_page import BasePage
from .locators import BasePageLocators, BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.should_be_basket_url()
        self.should_be_go_to_shopping_link()
        self.should_not_be_view_basket_button()

    def should_be_basket_url(self):
        assert self.browser.current_url.endswith("basket/") or \
            self.browser.current_url.endswith("basket"), \
                "Basket URL is not presented"

    def should_be_go_to_shopping_link(self):
        assert self.is_element_present(*BasketPageLocators.GO_TO_SHOPPING_LINK),\
            "Continue Shopping Link is not presented"

    def should_not_be_view_basket_button(self):
        assert self.is_not_element_present(*BasePageLocators.BASKET_LINK),\
            "'View Basket' button is presented, but should not be"

    def is_basket_empty(self):
        """
        Check if basket is empty or not
        """
        assert self.is_not_element_present(*BasketPageLocators.FORM_FOR_ITEMS),\
            "Form with items data is presented, basket is not empty"
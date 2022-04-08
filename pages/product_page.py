import math
from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException


class ProductPage(BasePage):
    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "Should be 'Add To Basket' button"

    def should_be_success_alert_with_prod_title(self):
        success_alerts = self.browser.find_elements(*ProductPageLocators.SUCCESS_ALERT)
        product_title = self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE)
        assert any(product_title.text == alert.text for alert in success_alerts), "Should be Success Alert with product title"

    def should_be_info_alert_with_busket_price(self):
        info_alerts = self.browser.find_elements(*ProductPageLocators.INFO_ALERT)
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        assert any(product_price.text == alert.text for alert in info_alerts), "Should be Info Alert with updated basket price"

    def add_product_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
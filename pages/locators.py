from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "form[id='login_form']")
    REGISTER_FORM = (By.CSS_SELECTOR, "form[id='register_form']")

class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket[type='submit']")
    PRODUCT_TITLE = (By.CSS_SELECTOR, "div.product_main > h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main > p.price_color")
    SUCCESS_ALERT = (By.CSS_SELECTOR, "div.alert-success > div.alertinner strong")
    INFO_ALERT = (By.CSS_SELECTOR, "div.alert-info > div.alertinner strong")
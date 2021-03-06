from selenium.webdriver.common.by import By


class BasePageLocators:
    BASKET_LINK = (By.XPATH, "//a[@class='btn btn-default' and contains(@href, 'basket')]")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inv")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators:
    ...

class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "form[id='login_form']")
    REGISTER_FORM = (By.CSS_SELECTOR, "form[id='register_form']")
    REG_EMAIL = (By.ID, "id_registration-email")
    REG_PASS = (By.ID, "id_registration-password1")
    REG_PASS_CONFIRM = (By.ID, "id_registration-password2")
    SUBMIT_REGISTRATION = (By.CSS_SELECTOR, "button.btn[name='registration_submit']")
    LOGIN_EMAIL = (By.ID, "id_login-username")
    LOGIN_PASS = (By.ID, "id_login-password")
    SUBMIT_LOGIN = (By.CSS_SELECTOR, "button.btn[name='login_submit']")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket[type='submit']")
    PRODUCT_TITLE = (By.CSS_SELECTOR, "div.product_main > h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main > p.price_color")
    SUCCESS_ALERT = (By.CSS_SELECTOR, "div.alert-success > div.alertinner strong")
    INFO_ALERT = (By.CSS_SELECTOR, "div.alert-info > div.alertinner strong")

class BasketPageLocators(BasePageLocators):
    NO_PRODUCTS_INFO = (By.CSS_SELECTOR, "div#content_inner > p")
    GO_TO_SHOPPING_LINK = (By.CSS_SELECTOR, "div#content_inner > p > a")
    FORM_FOR_ITEMS = (By.CSS_SELECTOR, "form.basket_summary[id='basket_formset']")
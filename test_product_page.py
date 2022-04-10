from .pages import MainPage, ProductPage, LoginPage, BasketPage
import time
import pytest
from selenium.webdriver.remote.webdriver import WebDriver


@pytest.mark.product_page_user
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser: WebDriver):
        self.browser = browser
        self.link = "http://selenium1py.pythonanywhere.com/"
        self.product_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        self.page = MainPage(self.browser, self.link)
        self.page.open()
        self.page.should_be_login_link()
        self.page.go_to_login_page()
        self.login_page = LoginPage(self.browser, self.browser.current_url)
        self.login_page.should_be_login_page()
        self.login_page.register_new_user(str(time.time()) + "@fakemail.org", "AjYtj7d9GQuM7QJ")
        # self.login_page.authorize_user("prog420@mail.ru", "AjYtj7d9GQuM7QJ")
        self.login_page.should_be_authorized_user()
        self.product_page = ProductPage(self.browser, self.product_link)
        yield

    def test_user_cant_see_success_message(self):
        self.product_page.open()
        self.product_page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self):
        self.product_page.open()
        self.product_page.should_be_add_to_basket_button()
        self.product_page.add_product_to_basket()
        self.product_page.should_be_success_alert_with_prod_title()
        self.product_page.should_be_info_alert_with_busket_price()


@pytest.mark.product_page_guest
class TestGuestAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser: WebDriver):
        self.browser = browser
        self.product_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        self.product_page = ProductPage(self.browser, self.product_link)
        self.product_page.open()
        yield

    def test_guest_cant_see_success_message(self):
        self.product_page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_guest_can_add_product_to_basket(self):
        self.product_page.should_be_add_to_basket_button()
        self.product_page.add_product_to_basket()
        self.product_page.should_be_success_alert_with_prod_title()
        self.product_page.should_be_info_alert_with_busket_price()

    @pytest.mark.xfail
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self):
        self.product_page.add_product_to_basket()
        self.product_page.should_not_be_success_message()

    @pytest.mark.xfail
    def test_message_disappeared_after_adding_product_to_basket(self):
        self.product_page.add_product_to_basket()
        self.product_page.is_success_message_disappeared()

    def test_guest_should_see_login_link_on_product_page(self):
        self.product_page.should_be_login_link()

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self):
        self.product_page.should_be_login_link()
        self.product_page.go_to_login_page()
        login_page = LoginPage(self.browser, self.browser.current_url)
        login_page.should_be_login_page()

    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self):
        self.product_page.should_be_basket_link()
        self.product_page.go_to_basket_page()
        basket_page = BasketPage(self.browser, self.browser.current_url)
        basket_page.should_be_basket_page()
        basket_page.is_basket_empty()

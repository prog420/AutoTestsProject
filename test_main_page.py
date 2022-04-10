from .pages import LoginPage, MainPage, BasketPage
import pytest
from selenium.webdriver.remote.webdriver import WebDriver


@pytest.mark.login_guest
class TestLoginFromMainPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser: WebDriver):
        self.browser = browser
        self.link = "http://selenium1py.pythonanywhere.com/"
        self.page = MainPage(browser, self.link)
        self.page.open()
        yield

    def test_guest_can_go_to_login_page(self):
        self.page.should_be_login_link()
        self.page.go_to_login_page()
        login_page = LoginPage(self.browser, self.browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self):
        self.page.open()
        self.page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser: WebDriver):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_basket_link()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, link)
    basket_page.should_be_basket_page()
    basket_page.is_basket_empty()
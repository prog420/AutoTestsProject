import pytest
from .pages import LoginPage, MainPage, BasketPage
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


@pytest.mark.skip
def test_guest_can_go_to_login_page(browser: WebDriver):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser: WebDriver):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_basket_link()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, link)
    basket_page.should_be_basket_page()
    basket_page.is_basket_empty()

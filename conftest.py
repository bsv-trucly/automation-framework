import pytest
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage

BASE_URL = "https://www.saucedemo.com"

@pytest.fixture
def login_page(page):
    lp = LoginPage(page)
    lp.navigate(BASE_URL)
    return lp

@pytest.fixture
def logged_in_page(page):
    lp = LoginPage(page)
    lp.navigate(BASE_URL)
    lp.login("standard_user", "secret_sauce")
    page.wait_for_url("**/inventory.html")
    return ProductPage(page)

@pytest.fixture
def cart_page(logged_in_page, page):
    return CartPage(page)
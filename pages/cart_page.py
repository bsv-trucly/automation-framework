from playwright.sync_api import Page
from pages.base_page import BasePage
class CartPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.cart_link = page.locator("[data-test='shopping-cart-link']")
        self.cart_item = page.locator("[data-test='inventory-item']")
        self.remove_button = page.locator("[id^='remove']")

    def go_to_cart(self):
        self.cart_link.click()

    def get_cart_item_count(self):
        return self.cart_item.count()
    
    def remove_first_item(self):
        self.remove_button.first.click()
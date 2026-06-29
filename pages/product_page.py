from playwright.sync_api import Page
from pages.base_page import BasePage
class ProductPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.product_list = page.locator("[data-test='inventory-item']")
        self.product_name = page.locator("[data-test='inventory-item-name']")
        self.add_to_cart_button = page.locator("[id^='add-to-cart']")

    def get_product_count(self):
        return self.product_list.count()
    
    def click_first_product(self):
        self.product_name.first.click()
        
    def add_first_product_to_cart(self):
        self.add_to_cart_button.first.click()
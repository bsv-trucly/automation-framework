from playwright.sync_api import expect

# TC01 - Add product vào cart
def test_add_product_to_cart(logged_in_page, cart_page):
    logged_in_page.add_first_product_to_cart()
    cart_page.go_to_cart()
    count = cart_page.get_cart_item_count()
    assert count == 1

# TC02 - Remove product khỏi cart
def test_remove_product_from_cart(logged_in_page, cart_page):
    logged_in_page.add_first_product_to_cart()
    cart_page.go_to_cart()
    cart_page.remove_first_item()
    count = cart_page.get_cart_item_count()
    assert count == 0
from playwright.sync_api import expect

# TC01 - Hiển thị danh sách sản phẩm
def test_product_list_display(logged_in_page):
    count = logged_in_page.get_product_count()
    assert count == 6

# TC02 - Xem chi tiết sản phẩm
def test_view_product_detail(logged_in_page):
    logged_in_page.click_first_product()
    logged_in_page.page.wait_for_url("**/inventory-item.html**")
    expect(logged_in_page.page.locator("[data-test='inventory-item-name']")).to_be_visible()
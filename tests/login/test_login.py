from playwright.sync_api import expect
from utils.data_reader import load_json
from utils.message import Message

#TC01
def test_login_success(login_page):
    users = load_json("users.json")
    u = users["valid_user"]
    login_page.login(u["username"], u["password"])
    expect(login_page.page).to_have_url("https://www.saucedemo.com/inventory.html")

#TC02
def test_login_fail_invalid_password(login_page):
    users = load_json("users.json")
    u = users["invalid_password"]
    login_page.login(u["username"], u["password"])
    error = login_page.get_error_message()
    assert Message.WRONG_CREDENTIALS in error

#TC03
def test_login_fail_invalid_username(login_page):
    users = load_json("users.json")
    u = users["invalid_username"]
    login_page.login(u["username"], u["password"])
    error = login_page.get_error_message()
    assert Message.WRONG_CREDENTIALS in error

#TC04
def test_login_fail_empty_user(login_page):
    users = load_json("users.json")
    u = users["empty_user"]
    login_page.login(u["username"], u["password"])
    error = login_page.get_error_message()
    assert Message.USERNAME_REQUIRED in error

#TC05
def test_login_fail_empty_password(login_page):
    users = load_json("users.json")
    u = users["empty_password"]
    login_page.login(u["username"], u["password"])
    error = login_page.get_error_message()
    assert Message.PASSWORD_REQUIRED in error
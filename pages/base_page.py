from playwright.sync_api import Page
class BasePage:
    def __init__(seft, page: Page):
        seft.page = page
    def navigate(seft, url: str):
        seft.page.goto(url)
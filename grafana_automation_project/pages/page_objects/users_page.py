from pages.utilities.base_page import BasePage
from selenium.webdriver.common.by import By


class UsersPage(BasePage):

    # Buttons
    new_user_btn = (By.CSS_SELECTOR, ".css-td06pi-button")

    # Text
    users_txt = (By.CSS_SELECTOR, ".css-bk8b94-title-info-container > div > h1")

    def verify_users_title(self):
        return self.get_text(self.users_txt)

import time
import allure
from pages.utilities.base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):

    # Text
    welcome_title_txt = (By.CSS_SELECTOR, ".css-17tm80")

    # Buttons
    avatar_btn = (By.CSS_SELECTOR, ".css-f77mr1-toolbar-button")
    logout_btn = (By.CSS_SELECTOR, ".css-yuemeu > a:nth-child(5)")

    def get_main_title_text(self):
        return self.get_text(self.welcome_title_txt)

    def verify_title_text(self, expected):
        self.verify_text_in_element(self.welcome_title_txt, expected)

    def press_on_user_avatar(self):
        time.sleep(1)
        self.press(self.avatar_btn)

    def logout(self):
        time.sleep(1)
        self.press(self.logout_btn)

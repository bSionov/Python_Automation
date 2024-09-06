import allure
from selenium.webdriver.common.by import By
from pages.utilities.base_page import BasePage


class LoginPage(BasePage):

    # Text
    welcome_title_txt = (By.CSS_SELECTOR, ".css-1gmqqtf")
    username_txt = (By.ID, ":r0:")
    password_txt = (By.ID, ":r1:")

    # Buttons
    login_btn = (By.CSS_SELECTOR, ".css-1b7vft8-button")
    forgot_password_btn = (By.CSS_SELECTOR, ".css-xrqx0q-button")
    skip_btn = (By.CSS_SELECTOR, ".css-bhnz0e-button")  # css-bhnz0e-button

    @allure.step("Fill in Username and Password")
    def fill_login_info(self, user, password):
        self.fill_text(self.username_txt, user)
        self.fill_text(self.password_txt, password)
        self.press(self.login_btn)
        self.press(self.skip_btn)

    def get_title_text(self):
        return self.get_text(self.welcome_title_txt)

    def press_on_skip_button(self):
        self.press(self.skip_btn)

    def verify_welcome_title_text(self, expected):
        self.verify_text_in_element(self.welcome_title_txt, expected)

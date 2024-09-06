from pages.utilities.base_page import BasePage
from selenium.webdriver.common.by import By


class SideMenuMainPage(BasePage):

    # Buttons
    admin_btn = (By.CSS_SELECTOR, ".css-1bqnmih > ul > div:nth-child(7) > li > div > div.css-1vx4yny")
    users_and_access_btn = (By.CSS_SELECTOR, ".css-1bqnmih  "
                                             "div:nth-child(7) > li > ul > li:nth-child(3) div.css-1vx4yny")
    users_btn = (By.CSS_SELECTOR, ".css-1bqnmih > ul > div:nth-child(7) > "
                                  "li > ul > li:nth-child(3) > ul > li:nth-child(1)")
    side_menu_buttons = (By.CSS_SELECTOR, ".css-762eyb")  # Elements
    admin_section = (By.CSS_SELECTOR, ".css-i0m3xi")  # Elements
    users_and_access_section = (By.CSS_SELECTOR, ".css-i0m3xi")  # Elements

    # Text
    users_txt = (By.CSS_SELECTOR, ".css-bk8b94-title-info-container > div > h1")

    def press_on_administration_btn(self):
        buttons = self.get_texts(self.side_menu_buttons, "Red")
        for button in buttons:
            if button.text == "Administration":
                button.click()
                break

    def press_on_users_and_access_btn(self):
        buttons = self.get_texts(self.admin_section, "Red")
        for button in buttons:
            if button.text == "Users and access":
                button.click()
                break

    def press_on_users_btn(self):
        buttons = self.get_texts(self.users_and_access_section, "Red")
        for button in buttons:
            if button.text == "Users":
                button.click()
                break

from pages.page_objects.login_page import LoginPage
from pages.page_objects.main_grafane_page import MainPage
from pages.page_objects.side_menu_main_page import SideMenuMainPage
from pages.page_objects.users_page import UsersPage


class PageFactory:
    def __init__(self, driver):
        self.driver = driver
        self.grafanaOnboardingPage = None  # First web page before user login
        self.grafanaMainPage = None  # First web page after user login
        self.grafanaSideMenuMainPage = None
        self.grafanaUsersPage = None

    def init_pages(self):
        self.grafanaOnboardingPage = LoginPage(self.driver)
        self.grafanaMainPage = MainPage(self.driver)
        self.grafanaSideMenuMainPage = SideMenuMainPage(self.driver)
        self.grafanaUsersPage = UsersPage(self.driver)
        # Initialize other pages here
        return self

    # Optionally, add methods to get pages by name
    def get_page(self, page_name):
        return getattr(self, page_name, None)

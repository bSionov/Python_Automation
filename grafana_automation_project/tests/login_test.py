import time
import os
import allure
import pytest


@pytest.mark.usefixtures()
class TestLoginPage:

    @allure.description("Test 01 - This test is verify that the correct title appears when open the tested website")
    def test_01_open(self, setup):
        with allure.step("Step 01 - This step is to verify if the title"
                         " {Welcome to Grafana} of the web site is correct"):
            self.grafanaOnboardingPage.verify_welcome_title_text(" Welcome to Grafana")
            print(f"Grafana title is: {self.grafanaOnboardingPage.get_title_text()}")

    @allure.description("Test 02 - This test is login to testing account")
    def test_02_login(self):
        user_name = os.getenv("USERNAME")
        password = os.getenv("PASSWORD")
        with allure.step("Step 01 - This step is to login to the website with user: {admin} and password: {admin}"):
            self.grafanaOnboardingPage.fill_login_info(user_name, password)
        with allure.step("Step 02 - This step is to verify if the title 'Welcome to Grafana' of the website is correct"):
            self.grafanaMainPage.verify_title_text("Welcome to Grafana ")
            title_text = self.grafanaMainPage.get_main_title_text()
            print(f"Grafana after login tite is: {title_text}")

    @allure.description("Test 03 - This test in navigating to Users page")
    def test_03_users_page(self, setup):
        self.grafanaSideMenuMainPage.press_on_administration_btn()
        self.grafanaSideMenuMainPage.press_on_users_and_access_btn()
        self.grafanaSideMenuMainPage.press_on_users_btn()
        print_text = self.grafanaUsersPage.verify_users_title()
        print(f"Page title is: {self.grafanaUsersPage.verify_users_title()}")
        self.grafanaUsersPage.verify_text_in_element(self.grafanaSideMenuMainPage.users_txt, print_text)

    @allure.description("Test Last - This test Loging out from the user")
    def test_100_logout(self, setup):
        self.grafanaMainPage.press_on_user_avatar()
        self.grafanaMainPage.logout()
        self.grafanaOnboardingPage.verify_text_in_element(
            self.grafanaOnboardingPage.welcome_title_txt, "Welcome to Grafana")
        print("\nLogout successfully")

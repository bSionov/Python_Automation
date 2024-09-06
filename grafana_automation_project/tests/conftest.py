import pytest
from dotenv import load_dotenv
import os
from pages.utilities.browser_init import BrowserInit
from pages.utilities.page_factory import PageFactory

# Load environment variables from .env file
dotenv_path = '../configuration/config.env'  # Adjust path if necessary
load_dotenv(dotenv_path)


def get_browser(browser_type):
    browser_type = browser_type.lower()
    if browser_type == "chrome":
        return BrowserInit.init_chrome()
    elif browser_type == "firefox":
        return BrowserInit.init_firefox()
    elif browser_type == "edge":
        return BrowserInit.init_edge()
    elif browser_type == "safari":
        return BrowserInit.init_safari()


@pytest.fixture(scope="class", autouse=True)
def setup(request):
    # Get browser type from config
    browser_type = os.getenv("BROWSER").capitalize()
    if browser_type not in ["Chrome", "Firefox", "Edge", "Safari"]:
        print(f"Invalid or empty browser type: '{browser_type}'. Defaulting to Chrome.")
        browser_type = "Chrome"
    driver = get_browser(browser_type)
    request.cls.driver = driver
    print(f"Using browser: {browser_type}")

    # Navigate to test site
    test_site_url = os.getenv("URL")
    driver.get(test_site_url)
    driver.maximize_window()

    # Initialize PageFactory and make pages available to tests
    page_factory = PageFactory(driver).init_pages()
    for page_name in dir(page_factory):
        if not page_name.startswith('_'):
            setattr(request.cls, page_name, getattr(page_factory, page_name))

    yield

    # Clean up
    driver.quit()

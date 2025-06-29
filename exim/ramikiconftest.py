import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from exim.Src.ramkilogin import *
@pytest.fixture(scope="function")
def driver():
    options = Options()

    # Disable Chrome's password manager and autofill services
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.default_content_setting_values.notifications": 2,
        "profile.default_content_setting_values.automatic_downloads": 1,  # Optional
        "autofill.profile_enabled": False,  # NEW
        "autofill.credit_card_enabled": False  # NEW
    }

    options.add_experimental_option("prefs", prefs)
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--no-default-browser-check")  # NEW
    options.add_argument("--disable-infobars")  # NEW
    options.add_argument("--incognito")  # NEW - Incognito disables password saving entirely

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.maximize_window()

    login(driver)  # Your custom login logic

    yield driver

    driver.quit()
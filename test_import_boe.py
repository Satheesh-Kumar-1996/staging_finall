import time

import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from Src.config import *
from Src.login import *

@pytest.fixture(scope="session")
def driver():
    options = Options()
    prefs = {
        "profile.password_manager_enabled": False,
        "credentials_enable_service": False,
        "profile.default_content_setting_values.notifications": 2
    }
    options.add_experimental_option("prefs", prefs)
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument("--disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    login(driver)
    #documents(driver)
    yield driver
    driver.quit()


def add_boe(driver):
    safe_click(driver, "//label[@for='checkbox']")
    safe_click(driver, "(//a[normalize-space()='Documents'])[1]")
    safe_click(driver, "(//h6[normalize-space()='BOE'])[1]")


def add_new_boe(driver, file_path="/home/sathish/Satheesh/satz/2025/stagingsample/samplePDFFile.pdf"):
    safe_click(driver, "(//button[normalize-space()='ADD NEW'])[1]")
    # Select the pi/po number
    safe_click(driver, "(//input[@type='checkbox'])[2]")

    safe_click(driver, "(//div[@class='dz-wrapper dropzone dz-multiple dz-clickable'])[1]")
    time.sleep(2)
    file_input_locator = (By.CSS_SELECTOR, "input[type='file']")
    upload_file_linux(driver, file_input_locator, file_path)

def fill_boe_form(driver):
    safe_click(driver, "(//input[@type='date'])[3]")
    time.sleep(1)
    # Enter the date
    safe_send_keys(driver, (By.XPATH, "(//input[@type='date'])[3]"), "10/04/2025")
    actions = ActionChains(driver)
    actions.send_keys(Keys.TAB).perform()
    actions.send_keys("2025").perform()
    time.sleep(1)
    # click & enter the BOE no
    #safe_click(driver, "(//input[@type='text'])[3]")
    safe_send_keys(driver, (By.XPATH, "((//input[@type='text'])[3]"), "BOE100")
    # Enter the BOE Amount
    safe_click(driver, "(//input[@type='textbox'])[1]")
    safe_send_keys(driver, (By.XPATH, "(//input[@type='textbox'])[1]"), "5000")
    # CLick and enter the port code
    safe_click(driver, "(//input[@type='text'])[4]")
    safe_send_keys(driver, (By.XPATH, "(//input[@type='text'])[4]"), "port")
    # CLick and enter the AWB no
    safe_click(driver, "(//input[@type='text'])[5]")
    safe_send_keys(driver, (By.XPATH, "(//input[@type='text'])[5]"), "SWA8474")
    # Click and enter the origin
    safe_click(driver, "(//input[@type='text'])[6]")
    safe_send_keys(driver, (By.XPATH, "(//input[@type='text'])[6]"), "Chennai")
    # Click and enter ethe portof loading
    safe_click(driver, "(//input[@type='text'])[7]")
    safe_send_keys(driver, (By.XPATH, "(//input[@type='text'])[7]"), "Delhi")
    # click and enter Adcode
    safe_click(driver, "(//input[@type='text'])[8]")
    safe_send_keys(driver, (By.XPATH, "(//input[@type='text'])[8]"), "AD8544")
    # Click and enter the freight value
    safe_click(driver, "(//input[@type='textbox'])[2]")
    safe_send_keys(driver, (By.XPATH, "(//input[@type='textbox'])[2]"), "500")
    # click and enter the miscellenous amount
    safe_click(driver, "(//input[@type='text'])[9]")
    safe_send_keys(driver, (By.XPATH, "(//input[@type='text'])[9]"), "2000")
    # CLick the TYpe dropdown
    safe_click(driver, "(//span[@class='ng-arrow-wrapper'])[1]")
    # Select the Type
    safe_click(driver, "(//span[normalize-space()='Direct Imports(Payment Against Bill of entry)'])[1]")

    safe_click(driver, "(//button[@id='BILL_OF_ENTRY'])[1]")
    time.sleep(1)

def test_pass(driver):
    add_boe(driver)
    add_new_boe(driver)
    fill_boe_form(driver)

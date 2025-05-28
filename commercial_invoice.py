import time

import pytest
from selenium import webdriver
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
def test_comercialinvoice(driver, file_path="/home/sathish/Satheesh/satz/2025/stagingsample/samplePDFFile.pdf"):
    #safe_click(driver, "//label[@for='checkbox']")
    safe_click(driver, "//a[normalize-space()='Documents']")
#comercial invoice
    safe_click(driver, "(//h6[normalize-space()='Commercial Invoices'])[1]")
#Add new button
    safe_click(driver, "//button[@class='upload-button btn btn-success ng-star-inserted']")
# selecting the check box
    safe_click(driver, "(//input[@type='checkbox'])[1]")
#add file
    time.sleep(2)
    safe_click(driver, "(//div[@class='dz-wrapper dropzone dz-multiple dz-clickable'])[1]")
    file_input_locator = (By.CSS_SELECTOR, "input[type='file']")
    upload_file_linux(driver, file_input_locator, file_path)
    time.sleep(3)
#Commercial in number
    safe_send_keys(driver, (By.XPATH, "(//input[@type='text'])[3]"), "123Wers@12")
#Currency
    #safe_click()
#Amount
    safe_send_keys(driver, (By.XPATH, "(//input[@type='textbox'])[1]"), "12000")
#invoice data
    safe_send_keys(driver, (By.XPATH, "(//input[@type='date'])[3]"), "12/05/2025")
#commadity amount
    safe_send_keys(driver, (By.XPATH, "(//input[@type='textbox'])[2]"), "123000")
#Freight Amount
    safe_send_keys(driver, (By.XPATH, "(//input[@type='textbox'])[3]"), "21300")
#Insurance Amount
    safe_send_keys(driver, (By.XPATH, "(//input[@type='textbox'])[4]"), "200")
#Misc Charges
    safe_send_keys(driver, (By.XPATH, "(//input[@type='textbox'])[5]"), "3000")
    time.sleep(1)
#submit
    safe_click(driver, "(//button[@id='ImportCommerical'])[1]")

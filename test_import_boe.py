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


def test_boe(driver, file_path="/home/sathish/Satheesh/satz/2025/stagingsample/samplePDFFile.pdf"):
    #safe_click(driver, "//label[@for='checkbox']")
    safe_click(driver, "(//a[normalize-space()='Documents'])[1]")
# click BOE
    safe_click(driver, "(//h6[normalize-space()='BOE'])[1]")
#Add new
    safe_click(driver, "(//button[normalize-space()='ADD NEW'])[1]")
# Select the pi/po number
    safe_click(driver, "(//input[@type='checkbox'])[2]")
#
    safe_click(driver, "(//div[@class='dz-wrapper dropzone dz-multiple dz-clickable'])[1]")
    time.sleep(2)
    file_input_locator = (By.CSS_SELECTOR, "input[type='file']")
    upload_file_linux(driver, file_input_locator, file_path)
#BOE date
    safe_send_keys(driver, (By.XPATH, "(//input[@type='date'])[3]"), "10/04/2025")
#BOE No
    safe_send_keys(driver, (By.XPATH, "(//input[@type='text'])[3]"), "ACC")
#BOE Amount
    safe_send_keys(driver, (By.XPATH, "(//input[@class='form-control ng-pristine ng-valid ng-touched'])[1]"), "20000")
#Port code
    safe_send_keys(driver, (By.XPATH, "(//input[@type='text'])[4]"), "WE123")
#AWB NO
    safe_send_keys(driver, (By.XPATH, "(//input[@type='text'])[5]"), "qwe1098")
#Orgin
    safe_send_keys(driver, (By.XPATH, "(//input[@type='text'])[6]"), "Chennai")
#Port Loading
    safe_send_keys(driver, (By.XPATH, "(//input[@type='text'])[7]"), "PORT OF FINAL DESTINATIONAIR")
#AD code
    safe_send_keys(driver, (By.XPATH, "(//input[@type='text'])[8]"), "MEIS")
#FREIGHT Value
    safe_send_keys(driver, (By.XPATH, "(//input[@class='form-control ng-valid ng-dirty ng-touched'])[1]"),  "Opt5646577")
#MISCELLANEOUS
    safe_send_keys(driver, (By.XPATH, "(//input[@type='text'])[9]"), "120000")
#


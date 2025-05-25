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

def open_pi_po_summary(driver):
    safe_click(driver, "//label[@for='checkbox']")
    safe_click(driver, "//a[normalize-space()='Documents']")
    safe_click(driver, "//h6[normalize-space()='PI/PO Summary']")

def add_new_pipo(driver, file_path="/home/sathish/Satheesh/satz/2025/stagingsample/samplePDFFile.pdf"):
    safe_click(driver, "//button[@class='upload-button btn btn-success ng-star-inserted']")
    time.sleep(2)
    file_input_locator = (By.CSS_SELECTOR, "input[type='file']")
    upload_file_linux(driver, file_input_locator, file_path)

def fill_pipo_form(driver):
    safe_send_keys(driver, (By.XPATH, "(//input[@class='form-control col-11 pr-4'])[1]"), "12345we")
    safe_click(driver, "(//input[@aria-autocomplete='list'])[1]")
    safe_click(driver, "(//span[@class='ng-option-label ng-star-inserted'])[2]")
    safe_click(driver, "//label[normalize-space()='Raw Material']//div[@class='checkbox-border']")
    safe_send_keys(driver, (By.XPATH, "//div[@class='form-group mb-0 ng-star-inserted']//input[@type='text']"), "test123test")
    safe_send_keys(driver, (By.XPATH, "(//input[@class='form-control ng-untouched ng-pristine ng-valid'])[2]"), "12/05/2025")

    safe_click(driver, "(//div[contains(@class, 'ng-select-container')])[2]")
    safe_click(driver, "(//span[@class='ng-arrow-wrapper'])[2]")
    safe_click(driver,xpath="(//div[@id='a2b201693f99-48'])[1]")
    safe_send_keys(driver, (By.XPATH, "(//input[contains(@class, 'form-control')])[7]"), "20000")

    safe_click(driver, "(//div[@class='ng-input'])[4]")
    safe_click(driver, "//span[text()='FCA | Free to Carrier']")

    safe_click(driver, "(//span[@class='ng-arrow-wrapper'])[5]")
    safe_click(driver, "(//span[@class='ng-option-label ng-star-inserted'])[1]")

    safe_click(driver, "(//div[@class='checkbox-border'])[5]")
    safe_click(driver, "(//span[@class='mat-checkbox-inner-container'])[1]")

    safe_click(driver, xpath="(//span[@class='ng-arrow-wrapper'])[6]")
    safe_click(driver, xpath="(//span[normalize-space()='Letter of Credit'])[1]")
    safe_send_keys(driver, (By.XPATH, "//div[@class='input-container']//input[@type='date']"), "19/05/2025")
    safe_send_keys(driver, (By.XPATH, "//ng-input-number[@type='textbox']//input[@type='textbox']"), "20000")

def submit_pipo(driver):
    safe_click(driver, "//button[@id='PIPO_IMPORT']")
    time.sleep(5)

def test_pass(driver):
    open_pi_po_summary(driver)
    add_new_pipo(driver)
    fill_pipo_form(driver)
    submit_pipo(driver)
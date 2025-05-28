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

def test_pi_po(driver, file_path="/home/sathish/Satheesh/satz/2025/stagingsample/samplePDFFile.pdf"):
    #safe_click(driver, "//label[@for='checkbox']")
    safe_click(driver, "//a[normalize-space()='Documents']")
    safe_click(driver, "//h6[normalize-space()='PI/PO Summary']")
#file upload
    safe_click(driver, "//button[@class='upload-button btn btn-success ng-star-inserted']")
    time.sleep(2)
    file_input_locator = (By.CSS_SELECTOR, "input[type='file']")
    upload_file_linux(driver, file_input_locator, file_path)

#beneficery name
    safe_send_keys(driver, (By.XPATH, "(//input[@class='form-control col-11 pr-4'])[1]"), "ABC INC" + Keys.ENTER)
#document type
    safe_click(driver, "(//input[@aria-autocomplete='list'])[1]")
    safe_click(driver, "(//span[@class='ng-option-label ng-star-inserted'])[2]")
#Type of goods *
    safe_click(driver, "//label[normalize-space()='Raw Material']//div[@class='checkbox-border']")
#PI/PO number *
    safe_send_keys(driver, (By.XPATH, "(//input[@type='text'])[4]"), "AWKWER123ITE")
#PI/PO Date *
    safe_send_keys(driver, (By.XPATH, "(//input[@class='form-control ng-untouched ng-pristine ng-valid'])[2]"), "12/05/2025")
#currency
    safe_send_keys(driver, (By.XPATH, "(//input[@type='text'])[5]"), "INR" + Keys.ENTER)
#PI/PO Amount *
    safe_send_keys(driver, (By.XPATH, "(//input[contains(@class, 'form-control')])[7]"), "20000")
#commodity
    safe_send_keys(driver, (By.XPATH, "(//input[@type='text'])[6]"), "Garments" + Keys.ENTER)
#incorterm
    safe_send_keys(driver, (By.XPATH, "(//input[@type='text'])[7]"), "FCA" + Keys.ENTER)
#Branch
    safe_send_keys(driver, (By.XPATH, "(//input[@type='text'])[8]"), "KOCHI" + Keys.ENTER)
#Mode of transport
    safe_click(driver, "(//div[@class='checkbox-border'])[5]")
#sub menu
    safe_click(driver, "(//span[@class='mat-checkbox-inner-container'])[1]")

#Payment terms
    safe_send_keys(driver, (By.XPATH, "(//input[@type='text'])[10]"), "Advance" + Keys.ENTER)


#last date of shipment
    safe_send_keys(driver, (By.XPATH, "(//input[@type='date'])[2]"), "30/05/2025")

    #Amount
    safe_send_keys(driver, (By.XPATH, "(//input[@type='textbox'])[2]"), "20000")

#Submit
    safe_click(driver, "(//button[@id='PIPO_IMPORT'])[1]")
    toast_message = get_toast_alert_text(driver)
    print("message:" + toast_message)
    time.sleep(2)
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
def test_insurence(driver, file_path="/home/sathish/Satheesh/satz/2025/stagingsample/samplePDFFile.pdf"):
    # safe_click(driver, "//label[@for='checkbox']")
    safe_click(driver, "//a[normalize-space()='Documents']")
#insurence policy
    safe_click(driver, "(//h6[normalize-space()='Insurance Policy'])[1]")
#Add new
    safe_click(driver, "//button[@class='upload-button btn btn-success ng-star-inserted']")
#check box
    safe_click(driver, "(//input[@type='checkbox'])[1]")
#Add new documents
    safe_click(driver, "(//div[@class='dz-wrapper dropzone dz-multiple dz-clickable'])[1]")
    file_input_locator = (By.CSS_SELECTOR, "input[type='file']")
    upload_file_linux(driver, file_input_locator, file_path)
    time.sleep(3)
#Insurence po date
    safe_send_keys(driver, (By.XPATH, "(//input[@type='date'])[3]"), "12/05/2025")
#insurence po Number
    safe_send_keys(driver, (By.XPATH, "(//input[@type='text'])[3]"), "CWCAYNK123KPAB")
#Curency
    # Step 1: Expand the Currency dropdown
    safe_send_keys(driver, (By.XPATH, "(//input[@aria-autocomplete='list'])[1]"), "INR" + Keys.ENTER)

#start date
    safe_send_keys(driver, (By.XPATH, "(//input[@type='date'])[4]"), "12/05/2024")
#Expire date
    safe_send_keys(driver, (By.XPATH, "(//input[@type='date'])[5]"), "12/05/2045")
#Insurence policy amount
    safe_send_keys(driver, (By.XPATH, "(//input[@type='textbox'])[1]"), "120000")
#submit
    safe_click(driver, "(//button[@id='ImportInsurancedocuments'])[1]")

    toast_message = get_toast_alert_text(driver)
    print("message:" +  toast_message)
    time.sleep(2)



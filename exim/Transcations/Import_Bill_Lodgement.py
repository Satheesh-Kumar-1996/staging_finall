import time

from exim.conftest import *
from exim.Src.config import *
from selenium.webdriver import Keys


def test_Ibl(driver):
    try:
        safe_click(driver, "(//a[normalize-space()='Transactions'])[1]")
        safe_click(driver, "(//h6[normalize-space()='Import Bill Lodgement'])[1]")
        safe_send_keys(driver, (By.XPATH, "(//input[@aria-autocomplete='list'])[1]"), "ABC" + Keys.ENTER)
        safe_click(driver, "(//label)[5]")
        safe_click(driver, "(//button[normalize-space()='Next'])[1]")
        safe_click(driver, "(//label[contains(@class, 'completed-container')])[1]")
        safe_click(driver, "(//button[normalize-space()='Next'])[1]")
        #select bank
        safe_click(driver, "(//input[@id='myDropdown'])[1]")
        safe_click(driver, "(//li[normalize-space()='Axis Bank Ltd'])[1]")
        #AC type
        safe_click(driver, "(//span[@class='mat-checkbox-inner-container'])[1]")
        #Ac type 2
        safe_click(driver, "(//span[@class='mat-checkbox-inner-container'])[2]")
        #payment type
        safe_click(driver, "//span[contains(@class, 'mat-radio-label-content') and contains(text(), 'ACCEPTANCE ADVISE?')]")
        #Advance remittance
        safe_click(driver, "//label[contains(., 'No')]/..")
        #Under LC
        safe_click(driver, "(//mat-radio-button)[5]")
        #FWC
        # safe_click(driver, "//button[normalize-space()='Select FWC']")
        # safe_click(driver, "(//input[@type='checkbox'])[9]")
        # safe_click(driver, "(//button[@type='button'][normalize-space()='Done'])[1]")
        #letter Head no
        safe_send_keys(driver, (By.XPATH, "(//input[@class='form-control ng-untouched ng-pristine ng-valid'])[1]"), "WELCOME")
        #Amount
        safe_send_keys(driver, (By.XPATH, "(//input[@type='text'])[34]"), "120")
        #Fill PDF
        safe_click(driver, "(//button[normalize-space()='Fill PDF'])[1]")
        preview_locator = (By.XPATH, "(//button[normalize-space()='Preview'])[1]")
        preview_button = WebDriverWait(driver, 45).until(EC.element_to_be_clickable(preview_locator))
        preview_button.click()
        time.sleep(5)
        safe_click(driver, "(//button[normalize-space()='Send for Approval'])[1]")
        safe_send_keys(driver, (By.XPATH, "(//input[@placeholder='remarks...'])[1]"), "Test123")
        safe_click(driver, "(//button[@type='button'][normalize-space()='Send'])[1]")
        time.sleep(3)
        toast_message = get_toast_alert_text(driver)
        print("message:" + toast_message)
    finally:
        print("Test success")

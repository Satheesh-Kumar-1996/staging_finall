import time

from selenium.webdriver import Keys
from exim.conftest import driver
from exim.Src.config import *
from exim.Src.login import *



def test_ICIS(driver):
    try:
        #safe_click(driver, "(//div[@class='dot'])[1]")
        safe_click(driver, "(//a[normalize-space()='Transactions'])[1]")
        safe_click(driver, "(//h6[normalize-space()='LC-Issuance'])[1]")
        safe_send_keys(driver, (By.XPATH, "(//input[@aria-autocomplete='list'])[1]"), "ABC" + Keys.ENTER)
        safe_click(driver, "(//label[contains(@class, 'completed-container')])[2]")
        safe_click(driver, "(//button[normalize-space()='Next'])[1]")
        #Bank
        safe_click(driver, "(//input[@id='myDropdown'])[2]")
        safe_click(driver, "(//li[normalize-space()='HDFC Bank Ltd'])[1]")
        #Account type
        safe_click(driver, "(//span[@class='mat-checkbox-inner-container'])[1]")
        #cover letter
        safe_click(driver, "(//button[@name='SingleMultiple'][normalize-space()='Yes'])[1]")
        #Ammount
        safe_send_keys(driver, (By.XPATH, "(//input[@type='text'])[13]"), "120")
        #Auto fill
        safe_click(driver, "(//button[@class='btn btn-primary PopupOpen'])[1]")
        #Document credit number
        safe_send_keys(driver, (By.XPATH, "(//textarea[@type='text'])[3]"), "test")
        #date
        safe_send_keys(driver, (By.XPATH, "(//input[@type='date'])[1]"),"20/05/2025")
        #date and palce of expiry
        safe_send_keys(driver, (By.XPATH, "(//textarea[@type='text'])[6]"), "20/06/2025" +Keys.ENTER  +"Chennai")
        #Currency code
        safe_send_keys(driver, (By.XPATH, "(//textarea[@type='text'])[10]"), "32BC")
        #Available
        # Fill textarea
        safe_send_keys(driver, (By.XPATH, "(//textarea[@type='text'])[13]"), "Test")
        # Click Done
        safe_click(driver, "(//button[@type='button'][normalize-space()='Done'])[1]")
        time.sleep(2)
        # Click Fill PDF
        safe_click(driver, "(//button[normalize-space()='Fill PDF'])[1]")
        # Wait until Preview button is enabled
        preview_locator = (By.XPATH, "(//button[normalize-space()='Preview'])[1]")
        preview_button = WebDriverWait(driver, 45).until(EC.element_to_be_clickable(preview_locator))
        preview_button.click()
        time.sleep(8)
        safe_click(driver, "//button[normalize-space()='Save a Draft']")
    finally:
        print("test success")


import inspect
import os
import time
from datetime import datetime

from threading import Thread, Event

from selenium.webdriver import Keys

from exim.Screenrecord import record_screen
from exim.Src.config import *
from exim.conftest import *
from selenium.common.exceptions import NoSuchElementException



def test_Direct_bill(driver):
    # test_name = inspect.currentframe().f_code.co_name
    # timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    # output_dir = r"/"
    # output_path = os.path.join(output_dir, f"{test_name}_{timestamp}.mp4")
    #
    # stop_event = Event()
    # t = Thread(target=record_screen, args=(output_path, stop_event))
    # t.start()
    try:
        #safe_click(driver, "(//div[@class='dot'])[1]")
        safe_click(driver, "(//a[normalize-space()='Transactions'])[1]")
        safe_click(driver, "(//h6[normalize-space()='Direct Bill'])[1]")
        #Benefeciary
        safe_send_keys(driver, (By.XPATH, "(//input[@aria-autocomplete='list'])[1]"), "ABC" +Keys.ENTER)
        #checkbox
        safe_click(driver, "(//label)[5]")
        #safe_click(driver, "(//input[@type='checkbox'])[3]")
        safe_click(driver, "(//button[normalize-space()='Next'])[1]")
        safe_click(driver, "(//button[normalize-space()='Next'])[1]")
        safe_click(driver, "(//button[normalize-space()='Next'])[1]")
        #Bank
        safe_click(driver, "(//input[@id='myDropdown'])[1]")
        safe_click(driver, "(//li[normalize-space()='Axis Bank Ltd'])[1]")
        #debit
        safe_click(driver, "(//span[@class='mat-checkbox-inner-container'])[1]")
        #Debit AC type
        safe_click(driver, "(//span[@class='mat-checkbox-inner-container'])[2]")
        #Import remittance
        safe_click(driver, "(//div[@class='checkbox-border'])[1]")
        #Bank charge
        safe_click(driver, "(//div[@class='checkbox-border'])[2]")
        #Type of goods
        safe_click(driver, "(//div[@class='checkbox-border'])[5]")
        #Letter Heads no
        safe_send_keys(driver, (By.XPATH, "(//input[@class='form-control ng-untouched ng-pristine ng-valid'])[1]"), "Welcome!!!")
        #Conversion details
        safe_click(driver, "(//div[@class='checkbox-border'])[6]")
        safe_click(driver, "(//div[@class='checkbox-border'])[7]")
        #Information
        safe_click(driver, "(//div[@class='checkbox-border'])[9]")
        #Bill of entry
        #remittanc information
        safe_send_keys(driver, (By.XPATH, "(//textarea[@class='form-control ng-untouched ng-pristine ng-valid'])[1]"), "Thank You!!!")
        #BOE 1
        safe_send_keys(driver, (By.XPATH, "(//input[@type='text'])[49]"), "7304596"+Keys.ENTER)
        #remittance amount
        safe_send_keys(driver, (By.XPATH, "(//input[@type='text'])[53]"), "160")
        #Fill PDF
        safe_click(driver, "(//button[normalize-space()='Fill PDF'])[1]")
        #preview button
        preview_locator = (By.XPATH, "(//button[normalize-space()='Preview'])[1]")
        preview_button = WebDriverWait(driver, 45).until(EC.element_to_be_clickable(preview_locator))
        preview_button.click()
        time.sleep(6)
        safe_click(driver, "(//button[normalize-space()='Send for Approval'])[1]")
        safe_send_keys(driver, (By.XPATH, "(//input[@placeholder='remarks...'])[1]"), "Test123")
        safe_click(driver, "(//button[@type='button'][normalize-space()='Send'])[1]")
        time.sleep(3)
        toast_message = get_toast_alert_text(driver)
        print("message:" + toast_message)
    finally:
         # stop_event.set()
         # t.join(timeout=10)
         # print(f"✅ Screen recording saved to: {output_path}")
         print("Test success")













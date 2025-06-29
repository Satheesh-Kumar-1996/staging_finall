import time

from exim.conftest import *
from exim.Src.config import *
from selenium.webdriver import Keys

def test_AOR(driver):
    try:
        #safe_click(driver, "(//div[@class='dot'])[1]")
        safe_click(driver, "(//a[normalize-space()='Transactions'])[1]")
        safe_click(driver, "(//h6[@class='nav-link p-0'][normalize-space()='Advance Outward Remittance'])[1]")
        safe_send_keys(driver, (By.XPATH, "(//input[@aria-autocomplete='list'])[1]"), "ABC" +Keys.ENTER)
        safe_click(driver, "(//label)[7]")
        safe_click(driver, "(//button[normalize-space()='Next'])[1]")
        safe_click(driver, "//tbody//div[2]//tr[1]//td[1]//label[1]")
        safe_click(driver, "(//button[normalize-space()='Next'])[1]")
        safe_send_keys(driver, (By.XPATH, "(//input[@type='TextValiadtion'])[1]"),"120")
        safe_click(driver, "(//button[normalize-space()='Next'])[1]")
        #Bank
        safe_click(driver, "(//input[@id='myDropdown'])[1]")
        safe_click(driver, "(//li[normalize-space()='Axis Bank Ltd'])[1]")
        #Acount type
        safe_click(driver, "(//span[@class='mat-checkbox-inner-container'])[1]")
        #Debet Ac type
        safe_click(driver, "(//span[@class='mat-checkbox-inner-container'])[2]")
        #Letter Head No
        safe_send_keys(driver, (By.XPATH, "(//input[@type='text'])[36]"), "Welcome!!")
        #Remittance
        safe_click(driver, "(//div[@class='checkbox-border'])[2]")
        #Foregine Bank Exchange
        safe_click(driver, "(//div[@class='checkbox-border'])[2]")
        #Port of Loading
        safe_send_keys(driver, (By.XPATH, "(//input[@type='text'])[37]"), "Chennai")
        #Port of Discharge
        safe_send_keys(driver, (By.XPATH, "(//input[@type='text'])[38]"), "Landon")
        #If Merchanting Trade Transaction
        safe_click(driver, "(//div[@class='checkbox-border'])[4]")
        #Select Type of Goods
        safe_click(driver, "(//div[@class='checkbox-border'])[6]")
        #Declaring cum
        safe_click(driver, "(//div[@class='checkbox-border'])[6]")
        #Remittance information
        safe_send_keys(driver, (By.XPATH, "(//textarea[@class='form-control ng-untouched ng-pristine ng-valid'])[1]"), "Thank You!!!")
        #Reittance amount
        safe_send_keys(driver, (By.XPATH, "(//input[@type='text'])[41]"), "120")

        #Fill PDF
        safe_click(driver, "(//button[normalize-space()='Fill PDF'])[1]")
        #Wait until Preview button is enabled
        preview_locator = (By.XPATH, "(//button[normalize-space()='Preview'])[1]")
        preview_button = WebDriverWait(driver, 45).until(EC.element_to_be_clickable(preview_locator))
        preview_button.click()
        time.sleep(6)
        safe_click(driver, "(//button[normalize-space()='Send for Approval'])[1]")
        time.sleep(2)
        safe_send_keys(driver, (By.XPATH, "(//input[@placeholder='remarks...'])[1]"), "Test123")
        safe_click(driver, "(//button[@type='button'][normalize-space()='Send'])[1]")
        # toast_message = get_toast_alert_text(driver)
        # print("message:" + toast_message)
    finally:
        print("Test success")

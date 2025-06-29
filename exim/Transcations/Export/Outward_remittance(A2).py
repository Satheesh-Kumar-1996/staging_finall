import time

from exim.conftest import *
from exim.Src.config import *
from selenium.webdriver import Keys

def test_Ora2(driver):
    try:
        safe_click(driver, "(//a[normalize-space()='Transactions'])[1]")
        safe_click(driver, "(//h6[@class='nav-link p-0'][normalize-space()='Outward Remittance (A2)'])[1]")
        safe_send_keys(driver, (By.XPATH, "(//input[@aria-autocomplete='list'])[1]"), "ABC" + Keys.ENTER)
        safe_click(driver, "(//label)[5]")
        safe_click(driver, "(//button[normalize-space()='Next'])[1]")
        safe_click(driver, "(//button[normalize-space()='Next'])[1]")
        safe_click(driver, "(//button[normalize-space()='Next'])[1]")
        # Bank
        safe_click(driver, "(//input[@id='myDropdown'])[1]")
        safe_click(driver, "(//li[normalize-space()='Axis Bank Ltd'])[1]")
        # debit
        safe_click(driver, "(//span[@class='mat-checkbox-inner-container'])[1]")
        # Debit AC type
        safe_click(driver, "(//span[@class='mat-checkbox-inner-container'])[2]")
        #AD branch
        safe_send_keys(driver, (By.XPATH, "(//input[@type='text'])[48]"), "TQNOPER123")
        #Cust id
        safe_send_keys(driver, (By.XPATH, "(//input[@type='text'])[49]"), "DDPCN123")
        #PAN
        safe_send_keys(driver, (By.XPATH, "(//input[@type='text'])[50]"), "DCPPMM897")
        #Letter Head
        safe_send_keys(driver, (By.XPATH, "(//input[@type='text'])[51]"), "Welcome!!!")
        #Bank Charge
        safe_click(driver, "(//div[@class='checkbox-border'])[1]")
        #Residental Status
        safe_click(driver, "(//div[@class='checkbox-border'])[3]")
        #Name of country providing ultimate services
        safe_send_keys(driver, (By.XPATH, "(//input[@type='text'])[52]"), "Thank You!!!!")
        #SOL ID
        safe_send_keys(driver, (By.XPATH, "(//input[@type='text'])[53]"), "TRP123")
        #Remittance
        safe_send_keys(driver, (By.XPATH, "(//textarea[@class='form-control ng-untouched ng-pristine ng-valid'])[1]"), "Be cool")
        safe_send_keys(driver, (By.XPATH, "(//input[@type='text'])[55]"), "50")
        #Select purposal code
        select = (By.XPATH, ("(//button[normalize-space()='Select'])[1]"))
        select_button = WebDriverWait(driver, 45).until(EC.element_to_be_clickable(select))
        select_button.click()
        #Check button
        Checkbox = (By.XPATH, ("//label[@for='mat-checkbox-218-input']//span[@class='mat-checkbox-inner-container mat-checkbox-inner-container-no-side-margin']"))
        check_box = WebDriverWait(driver, 45).until(EC.element_to_be_clickable(Checkbox))
        check_box.click()
        #done
        safe_click(driver, "(//button[@type='button'][normalize-space()='Done'])[8]")
      #Select 15CA
        safe_click(driver, "(//button[normalize-space()='Select 15 CA'])[1]")
        time.sleep(1)
        safe_click(driver, "(//input[@type='checkbox'])[12]")
        time.sleep(1)
        #done
        safe_click(driver, "(//button[@type='button'][normalize-space()='Done'])[1]")

        #select 15CB
        safe_click(driver, "(//button[normalize-space()='Select 15 CB'])[1]")
        time.sleep(1)
        safe_click(driver, "(//input[@type='checkbox'])[13]")
        time.sleep(1)
        safe_click(driver, "(//button[@type='button'][normalize-space()='Done'])[2]")
        #fill pdf
        safe_click(driver, "(//button[normalize-space()='Fill PDF'])[1]")
        #preview
        preview_locator = (By.XPATH, "(//button[normalize-space()='Preview'])[1]")
        preview_button = WebDriverWait(driver, 45).until(EC.element_to_be_clickable(preview_locator))
        preview_button.click()
        #send for approval
        safe_click(driver, "(//button[normalize-space()='Send for Approval'])[1]")
        safe_send_keys(driver, (By.XPATH, "(//input[@placeholder='remarks...'])[1]"), "Test123")
        safe_click(driver, "(//button[@type='button'][normalize-space()='Send'])[1]")
        time.sleep(3)
        toast_message = get_toast_alert_text(driver)
        print("message:" + toast_message)
    finally:
        print("test success")
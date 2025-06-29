from selenium.webdriver import Keys
from exim.conftest import *
from exim.Src.config import *


def  test_Buyer_Quote(driver):
    try:
        safe_click(driver, "(//a[normalize-space()='Transactions'])[1]")
        safe_click(driver, "(//h6[@class='nav-link p-0'][normalize-space()='Buyer Credit'])[1]")
        safe_click(driver, "(//span[normalize-space()='BC Quote Request'])[1]")
        #Beneficiary
        safe_click(driver, "(//input[@id='myDropdown'])[1]")
        safe_click(driver, "(//li[@class='li-dropdown ng-star-inserted'])[1]")
        #BOE
        safe_send_keys(driver, (By.XPATH, "(//input[@type='text'])[3]"), "BO66487" + Keys.ENTER)
        #LC Bank
        safe_send_keys(driver, (By.XPATH, "(//input[@type='text'])[5]"), "HDFC")
        #SUpplier name
        safe_send_keys(driver, (By.XPATH, "(//input[@type='text'])[6]"), "ABCD")
        #Swit code
        safe_send_keys(driver, (By.XPATH, "(//input[@type='text'])[7]"), "WEQTEST09876")
        #Tenor
        safe_send_keys(driver, (By.XPATH, "(//input[@type='text'])[11]"), "Test@12345")
        #Comoditty
        safe_send_keys(driver, (By.XPATH, "(//input[@type='text'])[12]"), "Garmen" + Keys.ENTER)
        #Shipment date
        safe_send_keys(driver, (By.XPATH, "(//input[@type='date'])[1]"), "12/06/2025")
        #Orgin of goods
        safe_send_keys(driver, (By.XPATH, "(//input[@type='text'])[13]"), "Vechical")
        #Port of loading
        safe_send_keys(driver, (By.XPATH, "(//input[@type='text'])[14]"), "Chennai")
        #port of Discharge
        safe_send_keys(driver, (By.XPATH, "(//input[@type='text'])[15]"), "Kochi")
        #Date
        safe_send_keys(driver, (By.XPATH, "(//input[@type='date'])[2]"), "12/05/2025")
        #Number ofshipment
        safe_send_keys(driver, (By.XPATH, "(//input[@type='text'])[16]"), "3")
        #charge
        safe_click(driver, "(//input[@id='myDropdown'])[2]")
        safe_click(driver, "(//li[normalize-space()='Beneficiary'])[1]")
        #Charge borned
        safe_click(driver, "(//input[@id='myDropdown'])[3]")
        safe_click(driver, "(//li[@class='ng-star-inserted'][normalize-space()='Beneficiary'])[2]")
        #payment
        safe_send_keys(driver, (By.XPATH, "(//input[@type='text'])[19]"), "Annual" + Keys.ENTER)
        #submit
        safe_click(driver, "(//button[@id='From_Client_Generate_15_CA'])[1]")
        toast_message = get_toast_alert_text(driver)
        print("message:" + toast_message)
    finally:
        print("toast_message")
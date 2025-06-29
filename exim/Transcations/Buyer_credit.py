from selenium.webdriver import Keys
from exim.conftest import *
from exim.Src.config import *


def  test_Buyer_credit(driver):
    try:
        safe_click(driver, "(//a[normalize-space()='Transactions'])[1]")
        safe_click(driver, "(//h6[@class='nav-link p-0'][normalize-space()='Buyer Credit'])[1]")
        #Beneficery
        safe_click(driver, "(//input[@id='myDropdown'])[1]")
        safe_click(driver, "(//li[normalize-space()='ABC INC'])[1]")
        #Bank
        safe_click(driver, "(//input[@id='myDropdown'])[2]")
        safe_click(driver, "(//li[normalize-space()='HDFC Bank Ltd'])[1]")
        #Account type
        safe_click(driver, "(//span[@class='mat-checkbox-inner-container'])[1]")
        #remittance
        safe_click(driver, "(//div[@class='checkbox-border'])[2]")
        #Bank charges
        safe_click(driver, "(//div[@class='checkbox-border'])[2]")
        #BOE
        safe_send_keys(driver, (By.XPATH, "(//input[@type='text'])[6]"), "BO66487" + Keys.ENTER)
        #remittance amount
        safe_send_keys(driver, (By.XPATH, "(//input[@type='text'])[9]"), "1500")
        #Total amount
        safe_send_keys(driver, (By.XPATH, "(//input[@type='text'])[10]"), "150")
        #Select BC Quote
        # safe_click(driver, "(//button[normalize-space()='Select BC Quote'])[1]")
        # PDF = (By.XPATH, "(//button[normalize-space()='Fill PDF'])[1]")
    finally:
        print("""""")
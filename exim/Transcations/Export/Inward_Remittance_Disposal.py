from exim.Src.config import safe_click, safe_send_keys
from exim.Src.ramkilogin import *
from exim.conftest import *
def IRD(driver):

    try:
        safe_click(driver, "(//a[normalize-space()='Transactions'])[1]")
        safe_click(driver, "(//h6[@class='nav-link p-0'][normalize-space()='Advance Outward Remittance'])[1]")
        #select beneficiary
        safe_click(driver, "(//span[@class='ng-arrow-wrapper'])[1]")
        safe_click(driver, "(//div[@id='a8157700a32f-4'])[1]")
        #check box
        safe_click(driver, "(//input[@type='checkbox'])[2]")
        #click next
        safe_click(driver, "(//button[normalize-space()='Next'])[1]")
        #Check box
        safe_click(driver, "(//input[@type='checkbox'])[2]")
        #Next
        safe_click(driver, "(//button[normalize-space()='Next'])[1]")
        #Utilised amount
        safe_send_keys(driver, (By.XPATH, "(//input[@type='TextValiadtion'])[1]"), "1200")
        #next
        safe_click(driver, "(//button[normalize-space()='Next'])[1]")
        #select bank
        safe_click(driver, "(//input[@id='myDropdown'])[1]")
        safe_click(driver, "(//li[normalize-space()='Axis Bank Ltd'])[1]")
        #Ac type
        safe_click(driver, "(//span[@class='mat-checkbox-inner-container'])[1]")
        #Ac type
        safe_click(driver, "(//span[@class='mat-checkbox-inner-container'])[2]")
        #Letter to head
        safe_send_keys(driver, (By.XPATH, "(//input[@type='text'])[36]"), "TOC12")
        #select remittance
        safe_click(driver, "(//div[@class='checkbox-border'])[2]")
        #Bank charge
        safe_click(driver, "(//div[@class='checkbox-border'])[3]")
        #Port loading
        safe_send_keys(driver, (By.XPATH, "(//input[@type='text'])[37]"), "AB")
        #Port discharge
        safe_send_keys(driver, (By.XPATH, "(//input[@type='text'])[38]"), "CD")
        #trade transction
        safe_click(driver, "(//div[@class='checkbox-border'])[6]")
        #Type of goods
        safe_click(driver, "(//div[@class='checkbox-border'])[9]")
        #Declaration under taking
        safe_click(driver, "(//div[@class='checkbox-border'])[10]")
        #remittance
        safe_send_keys(driver, (By.XPATH, "(//textarea[@class='form-control ng-untouched ng-pristine ng-valid'])[1]"), "Test")
        #remittance amount
        




import time
import pyotp
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login(driver):
    driver.get("https://staging.bharathexim.com/")
    driver.maximize_window()
    time.sleep(2)

    username(driver)
    password(driver)
    perform_login(driver)
    perform_otp(driver)
    perform_login(driver)
    time.sleep(3)

def username(driver):
    email_input = driver.find_element(By.XPATH, "(//input[@placeholder='Enter email id'])[1]")
    email_input.send_keys("palmaker@yopmail.com")

def password(driver):
    password_input = driver.find_element(By.XPATH, "(//input[@placeholder='Enter password'])[1]")
    password_input.send_keys("Test@1234")

def perform_login(driver):
    login_button = driver.find_element(By.XPATH, "(//button[normalize-space()='Login'])[1]")
    login_button.click()

def perform_otp(driver):
    totp = pyotp.TOTP("FR6WMNCCIZWU6VLU")  # Replace with actual secret
    otp = totp.now()
    wait = WebDriverWait(driver, 15)
    otp_input = wait.until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter 6 digit Google Auth OTP']"))
    )
    otp_input.send_keys(otp)


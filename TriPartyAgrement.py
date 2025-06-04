import datetime
import inspect
import os
import time
from threading import Thread, Event
import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from Screenrecord import record_screen
from Src.config import *
from Src.login import *

def test_TPA(driver, file_path="/home/sathish/Satheesh/satz/2025/stagingsample/samplePDFFile.pdf"):
    test_name = inspect.currentframe().f_code.co_name
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = r"/home/sathish/PythonProject"
    output_path = os.path.join(output_dir, f"{test_name}_{timestamp}.mp4")

    stop_event = Event()
    t = Thread(target=record_screen, args=(output_path, stop_event))
    t.start()
    time.sleep(2)

    try:
    #safe_click(driver, "//label[@for='checkbox']")
       safe_click(driver, "//a[normalize-space()='Documents']")
       safe_click(driver, "(//h6[normalize-space()='Tri party agreements'])[1]")
# Add new
       safe_click(driver, "(//button[normalize-space()='ADD NEW'])[1]")
 # check box
       safe_click(driver, "(//input[@type='checkbox'])[2]")
#file upload
       safe_click(driver, "(//div[@class='dz-text'])[1]")
       time.sleep(2)
       file_input_locator = (By.CSS_SELECTOR, "input[type='file']")
       upload_file_linux(driver, file_input_locator, file_path)
       time.sleep(3)
 #start date
       safe_send_keys(driver, (By.XPATH, "(//input[@type='date'])[3]"), "31/05/2025")
#TRi part number
       safe_send_keys(driver, (By.XPATH, "(//input[@type='text'])[3]"), "987664")
#Currency
       safe_send_keys(driver, (By.XPATH, "(//input[@type='text'])[4]"), "INR" + Keys.ENTER)
#TRi part Amount
       safe_send_keys(driver, (By.XPATH, "(//input[@type='textbox'])[1]"), "1200000")
#Party 1
       safe_send_keys(driver, (By.XPATH, "(//input[@type='text'])[5]"), "ABC" + Keys.ENTER)
#Party 2
       safe_send_keys(driver, (By.XPATH, "(//input[@type='text'])[7]"), "ABC" + Keys.ENTER)
#Party 3
       safe_send_keys(driver, (By.XPATH, "(//input[@type='text'])[9]"), "ABC" + Keys.ENTER)
#Submit
       safe_click(driver, "(//button[@id='ImportTrypartyagreements'])[1]")
       toast_message = get_toast_alert_text(driver)
       print("message:" + toast_message)
       time.sleep(4)

    finally:
        stop_event.set()
        t.join(timeout=30)
        if t.is_alive():
            print("⚠Recording thread did not stop in time.")
        else:
            print(f"Screen recording saved to: {output_path}")
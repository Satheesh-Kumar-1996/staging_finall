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


def test_packinflist(driver, file_path="/home/sathish/Satheesh/satz/2025/stagingsample/samplePDFFile.pdf"):
    test_name = inspect.currentframe().f_code.co_name
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = r"/home/sathish/PythonProject"
    output_path = os.path.join(output_dir, f"{test_name}_{timestamp}.mp4")

    stop_event = Event()
    t = Thread(target=record_screen, args=(output_path, stop_event))
    t.start()
    time.sleep(2)

    try:
       safe_click(driver, "//a[normalize-space()='Documents']")
#Packing list
       safe_click(driver, "(//h6[normalize-space()='Packing List'])[1]")
#Add new
       safe_click(driver, "//button[@class='upload-button btn btn-success ng-star-inserted']")
#check box
       safe_click(driver, "(//input[@type='checkbox'])[1]")
#Add new documents
       safe_click(driver, "(//div[@class='dz-wrapper dropzone dz-multiple dz-clickable'])[1]")
       file_input_locator = (By.CSS_SELECTOR, "input[type='file']")
       upload_file_linux(driver, file_input_locator, file_path)
       time.sleep(3)
#Packing list
       safe_send_keys(driver, (By.XPATH, "(//input[@type='text'])[3]"), "Wq123567")
#Submit
       safe_click(driver, "(//button[@id='Importpackinglist'])[1]")
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
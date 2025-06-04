import os
import time
import datetime
import inspect
from threading import Thread, Event

from selenium.webdriver import Keys

from Src.config import *
from Screenrecord import record_screen

def test_ABC(driver, file_path="/home/sathish/Satheesh/satz/2025/stagingsample/samplePDFFile.pdf"):
    test_name = inspect.currentframe().f_code.co_name
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = r"/home/sathish/PythonProject"
    output_path = os.path.join(output_dir, f"{test_name}_{timestamp}.mp4")

    stop_event = Event()
    t = Thread(target=record_screen, args=(output_path, stop_event))
    t.start()

    try:
        safe_click(driver, "//a[normalize-space()='Documents']")
        safe_click(driver, "(//h6[normalize-space()='Outward Remittance Advice'])[1]")
        safe_click(driver, "//button[@class='upload-button btn btn-success ng-star-inserted']")
        safe_click(driver, "(//input[@type='checkbox'])[1]")
        time.sleep(2)
        safe_click(driver, "(//div[@class='dz-wrapper dropzone dz-multiple dz-clickable'])[1]")
        upload_file_linux(driver, (By.CSS_SELECTOR, "input[type='file']"), file_path)
        time.sleep(3)
        #TT date
        safe_send_keys(driver, (By.XPATH, "(//input[@type='date'])[3]"), "12/05/2025")
        #Transaction type
        safe_send_keys(driver, (By.XPATH, "(//input[@type='text'])[3]"), "ADVANCE"+Keys.ENTER)
        #Bill No
        safe_send_keys(driver, (By.XPATH, "(//input[@type='text'])[4]"), "ERTNUMBER123")
        #Party name
        safe_click(driver, "(//input[@id='myDropdown'])[2]")
        safe_click(driver, "(//li[@class='li-dropdown ng-star-inserted'])[1]")
        #TT Amount
        safe_send_keys(driver, (By.XPATH, "(//input[@type='textbox'])[1]"), "16000")
        #Commision
        safe_send_keys(driver, (By.XPATH, "(//input[@type='textbox'])[2]"), "400")
        #Exchange rate
        safe_send_keys(driver, (By.XPATH, "(//input[@type='textbox'])[3]"), "3000")
        #Location
        safe_send_keys(driver, (By.XPATH, "(//input[@type='text'])[7]"), "KOCHI"+Keys.ENTER)
        #submit
        safe_click(driver, "(//button[@id='OutwardRemittanceAdvice'])[1]")
        time.sleep(4)
        toast_message = get_toast_alert_text(driver)
        print("message:" + toast_message)
        time.sleep(6)
    finally:
        stop_event.set()
        t.join(timeout=10)
        print(f"✅ Screen recording saved to: {output_path}")

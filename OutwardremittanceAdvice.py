import datetime
import inspect
import os
import time
from threading import Thread, Event
from selenium.webdriver import Keys
from Screenrecord import record_screen
from Src.config import *
from Src.login import *

def test_ora(driver, file_path="/home/sathish/Satheesh/satz/2025/stagingsample/samplePDFFile.pdf"):
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
       safe_click(driver, "(//h6[normalize-space()='Outward Remittance Advice'])[1]")
# Add new
       safe_click(driver, "(//button[normalize-space()='ADD NEW'])[1]")
 # check box
       safe_click(driver, "(//input[@type='checkbox'])[1]")
#file upload
       safe_click(driver, "(//div[@class='dz-text'])[1]")
       time.sleep(2)
       file_input_locator = (By.CSS_SELECTOR, "input[type='file']")
       upload_file_linux(driver, file_input_locator, file_path)
       time.sleep(3)

#date
       safe_send_keys(driver, (By.XPATH, "(//input[@type='date'])[3]"), "02/05/2025")
#select Trans Type
       safe_send_keys(driver, (By.XPATH, "(//input[@type='text'])[3]"), "ADVANCE" + Keys.ENTER)
#Bill NO
       safe_send_keys(driver, (By.XPATH, "(//input[@type='text'])[4]"), "SAMS123SUNG")
#Party name
       safe_click(driver, "(//input[@id='myDropdown'])[2]")
       safe_click(driver, "(//li[@class='li-dropdown ng-star-inserted'])[1]")
#TT Amount
       safe_send_keys(driver, (By.XPATH, "(//input[@type='textbox'])[1]"), "30000")
#Commission
       safe_send_keys(driver, (By.XPATH, "(//input[@type='textbox'])[2]"), "2000")
#Exchange rate
       safe_send_keys(driver, (By.XPATH, "(//input[@type='textbox'])[3]"), "1500")
#Location
       safe_send_keys(driver, (By.XPATH, "(//input[@type='text'])[7]"), "KOCHI"+Keys.ENTER)
#submit
       safe_click(driver, "(//button[@id='OutwardRemittanceAdvice'])[1]")
       time.sleep(4)
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
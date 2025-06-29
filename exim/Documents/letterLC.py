import datetime
import inspect
import os
from threading import Thread, Event
from exim.Screenrecord import record_screen
from exim.Src.config import *
from exim.Src.login import *
from exim.conftest import *

def test_LC(driver, file_path="/home/sathish/Satheesh/satz/2025/stagingsample/samplePDFFile.pdf"):
    test_name = inspect.currentframe().f_code.co_name
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = r"/"
    output_path = os.path.join(output_dir, f"{test_name}_{timestamp}.mp4")

    stop_event = Event()
    t = Thread(target=record_screen, args=(output_path, stop_event))
    t.start()
    time.sleep(2)

    try:
       #safe_click(driver, "//label[@for='checkbox']")
       safe_click(driver, "//a[normalize-space()='Documents']")
       safe_click(driver, "(//h6[normalize-space()='Letter of Credit (LC)'])[1]")
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
#LOCD
       safe_send_keys(driver, (By.XPATH, "(//input[@type='date'])[3]"), "12/05/2025")
#LOCNumber
       safe_send_keys(driver, (By.XPATH, "(//input[@type='text'])[3]"), "WCR908765")
#CURRENCY
       safe_send_keys(driver, (By.XPATH, "(//input[@aria-autocomplete='list'])[1]"), "INR" + Keys.ENTER)
#LOCAMOUNT
       safe_send_keys(driver, (By.XPATH, "(//input[@type='textbox'])[1]"), "20000")
#LOCEXPIRE DATE
       safe_send_keys(driver, (By.XPATH, "(//input[@type='date'])[4]"), "23/04/2025")
#Last date of Shipment
       safe_send_keys(driver, (By.XPATH, "(//input[@type='date'])[5]"), "23/07/2025")
#submit
       safe_click(driver, "(//button[@id='Importletterofcredit'])[1]")
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

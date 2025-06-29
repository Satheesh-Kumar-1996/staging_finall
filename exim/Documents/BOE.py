import datetime
import inspect
import os
from threading import Thread, Event
from exim.Screenrecord import record_screen
from exim.Src.config import *
from exim.Src.login import *
from exim.conftest import *

def test_boe(driver, file_path="/home/sathish/Satheesh/satz/2025/stagingsample/samplePDFFile.pdf"):
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
       safe_click(driver, "(//a[normalize-space()='Documents'])[1]")
# click BOE
       safe_click(driver, "(//h6[normalize-space()='BOE'])[1]")
#Add new
       safe_click(driver, "(//button[normalize-space()='ADD NEW'])[1]")
# Select the pi/po number
       safe_click(driver, "(//input[@type='checkbox'])[2]")
#
       safe_click(driver, "(//div[@class='dz-wrapper dropzone dz-multiple dz-clickable'])[1]")
       time.sleep(2)
       file_input_locator = (By.CSS_SELECTOR, "input[type='file']")
       upload_file_linux(driver, file_input_locator, file_path)
#BOE date
       safe_send_keys(driver, (By.XPATH, "(//input[@type='date'])[3]"), "10/04/2025")
#BOE No
       safe_send_keys(driver, (By.XPATH, "(//input[@type='text'])[3]"), "ACC")
#Boe currency
    #safe_send_keys(driver, (By.XPATH, "(//label[@class='form-label-control ng-star-inserted'])[1]"))
#BOE Amount
       safe_send_keys(driver, (By.XPATH, "(//input[@type='textbox'])[1]"), "20000")
#Port code
       safe_send_keys(driver, (By.XPATH, "(//input[@type='text'])[4]"), "WE123")
#AWB NO
       safe_send_keys(driver, (By.XPATH, "(//input[@type='text'])[5]"), "qwe1098")
#Orgin
       safe_send_keys(driver, (By.XPATH, "(//input[@type='text'])[6]"), "Chennai")
#Port Loading
       safe_send_keys(driver, (By.XPATH, "(//input[@type='text'])[7]"), "PORT OF FINAL DESTINATIONAIR")
#AD code
       safe_send_keys(driver, (By.XPATH, "(//input[@type='text'])[8]"), "MEIS")
#FREIGHT Value
       safe_send_keys(driver, (By.XPATH, "(//input[@type='textbox'])[2]"),  "Opt5646577")
#MISCELLANEOUS
       safe_send_keys(driver, (By.XPATH, "(//input[@type='text'])[9]"), "120000")
#Type
       safe_send_keys(driver, (By.XPATH, "(//input[@aria-autocomplete='list'])[1]"), "Advance" + Keys.ENTER)

 #Sumbmit
       safe_click(driver, "(//button[@id='BILL_OF_ENTRY'])[1]")
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



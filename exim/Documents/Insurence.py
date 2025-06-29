import datetime
import inspect
import os
from threading import Thread, Event
from selenium.webdriver import Keys
from exim.Screenrecord import record_screen
from exim.Src.config import *
from exim.Src.login import *
from exim.conftest import *

def test_insurence(driver, file_path="/home/sathish/Satheesh/satz/2025/stagingsample/samplePDFFile.pdf"):
    test_name = inspect.currentframe().f_code.co_name
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = r"/"
    output_path = os.path.join(output_dir, f"{test_name}_{timestamp}.mp4")

    stop_event = Event()
    t = Thread(target=record_screen, args=(output_path, stop_event))
    t.start()
    time.sleep(2)

    try:
        safe_click(driver, "//a[normalize-space()='Documents']")
        safe_click(driver, "(//h6[normalize-space()='Insurance Policy'])[1]")
        safe_click(driver, "//button[@class='upload-button btn btn-success ng-star-inserted']")
        safe_click(driver, "(//input[@type='checkbox'])[1]")
        safe_click(driver, "(//div[@class='dz-wrapper dropzone dz-multiple dz-clickable'])[1]")

        file_input_locator = (By.CSS_SELECTOR, "input[type='file']")
        upload_file_linux(driver, file_input_locator, file_path)
        time.sleep(3)

        safe_send_keys(driver, (By.XPATH, "(//input[@type='date'])[3]"), "12/05/2025")
        safe_send_keys(driver, (By.XPATH, "(//input[@type='text'])[3]"), "CWCAYNK123KPAC")
        safe_send_keys(driver, (By.XPATH, "(//input[@aria-autocomplete='list'])[1]"), "INR" + Keys.ENTER)
        safe_send_keys(driver, (By.XPATH, "(//input[@type='date'])[4]"), "12/05/2024")
        safe_send_keys(driver, (By.XPATH, "(//input[@type='date'])[5]"), "12/05/2045")
        safe_send_keys(driver, (By.XPATH, "(//input[@type='textbox'])[1]"), "120000")

        safe_click(driver, "(//button[@id='ImportInsurancedocuments'])[1]")
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




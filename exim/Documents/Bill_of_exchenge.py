import datetime
import inspect
import os
from threading import Thread, Event
from exim.Screenrecord import record_screen
from exim.Src.config import *
from exim.Src.login import *
from exim.conftest import *

def test_BOE(driver, file_path="/home/sathish/Satheesh/satz/2025/stagingsample/samplePDFFile.pdf"):
    test_name = inspect.currentframe().f_code.co_name
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = r"/"
    output_path = os.path.join(output_dir, f"{test_name}_{timestamp}.mp4")

    stop_event = Event()
    t = Thread(target=record_screen, args=(output_path, stop_event))
    t.start()

    try:
        safe_click(driver, "//a[normalize-space()='Documents']")
        safe_click(driver, "(//h6[normalize-space()='Bill Of Exchange'])[1]")
        safe_click(driver, "//button[@class='upload-button btn btn-success ng-star-inserted']")
        safe_click(driver, "(//input[@type='checkbox'])[1]")
        time.sleep(2)
        safe_click(driver, "(//div[@class='dz-wrapper dropzone dz-multiple dz-clickable'])[1]")
        upload_file_linux(driver, (By.CSS_SELECTOR, "input[type='file']"), file_path)
        time.sleep(3)
        safe_click(driver, "(//span[@class='mat-checkbox-inner-container'])[1]")
        safe_send_keys(driver, (By.XPATH, "(//input[@type='text'])[3]"), "POST908765WTE")
        safe_click(driver, "(//button[@id='ImportBillOfExchange'])[1]")
        time.sleep(3)
        toast_message = get_toast_alert_text(driver)
        print("message:", toast_message)
        time.sleep(6)
    finally:
        stop_event.set()
        t.join(timeout=10)
        print(f"✅ Screen recording saved to: {output_path}")
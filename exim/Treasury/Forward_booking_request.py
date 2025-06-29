import os
import datetime
import inspect
import time
from threading import Thread, Event

from selenium.webdriver import Keys

from exim.Src.config import *
from exim.conftest import *
from exim.Screenrecord import record_screen
def test_Fbr(driver):
    # test_name = inspect.currentframe().f_code.co_name
        # timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        # output_dir = r"/"
        # output_path = os.path.join(output_dir, f"{test_name}_{timestamp}.mp4")
        #
        # stop_event = Event()
        # t = Thread(target=record_screen, args=(output_path, stop_event))
        # t.start()

        try:
            safe_click(driver, "(//a[normalize-space()='Treasury'])[1]")
            safe_click(driver, "(//h6[normalize-space()='Forward Booking Request'])[1]")
            safe_click(driver, "(//input[@type='checkbox'])[1]")
            safe_send_keys(driver, (By.XPATH, "(//input[@type='text'])[3]"), "100")
            #next
            safe_click(driver, "(//button[normalize-space()='Next'])[1]")
            #Export CI
            safe_click(driver, "(//input[@type='checkbox'])[1]")
            safe_send_keys(driver, (By.XPATH, "(//input[@type='text'])[3]"), "150")
            safe_click(driver, "(//button[normalize-space()='Next'])[1]")
            #Import pipo
            safe_click(driver, "(//input[@type='checkbox'])[1]")
            safe_send_keys(driver, (By.XPATH, "(//input[@type='text'])[3]"), "100")
            safe_click(driver, "(//button[normalize-space()='Next'])[1]")
            #Import CI
            safe_click(driver, "(//input[@type='checkbox'])[1]")
            safe_send_keys(driver, (By.XPATH, "(//input[@type='text'])[3]"), "100")
            safe_click(driver, "(//button[normalize-space()='Next'])[1]")
            #send mail
            safe_click(driver, "(//button[normalize-space()='Send Mail'])[1]")
            time.sleep(3)
            toast_message = get_toast_alert_text(driver)
            print("message:" + toast_message)
        finally:
            print("Test_Pass")


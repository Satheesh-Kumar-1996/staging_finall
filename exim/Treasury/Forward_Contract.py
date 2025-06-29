import os
import datetime
import inspect
from threading import Thread, Event

from selenium.webdriver import Keys

from exim.Src.config import *
from exim.conftest import *
from exim.Screenrecord import record_screen

def test_Frwd_Contract(driver):
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
        safe_click(driver, "(//h6[normalize-space()='Forward Contract'])[1]")
        #Add new
        safe_click(driver, "(//button[normalize-space()='ADD NEW'])[1]")
        #Select bank
        safe_send_keys(driver, (By.XPATH, "(//input[@type='text'])[2]"), "HDFC"+Keys.ENTER)
        #FRWD Ref no
        safe_send_keys(driver, (By.XPATH, "(//input[@type='text'])[3]"), "2D89899")
        #Currency
        safe_send_keys(driver, (By.XPATH, "(//input[@type='text'])[5]"), "INR"+Keys.ENTER)
        #Utilized Amount
        safe_send_keys(driver, (By.XPATH, "(//input[@type='number'])[2]"), "12000")
        #From date
        safe_send_keys(driver, (By.XPATH, "(//input[@type='date'])[2]"), "12/05/2025")
        #Net Rate
        safe_send_keys(driver, (By.XPATH, "(//input[@type='text'])[10]"), "20000")
        #import/Export
        safe_send_keys(driver, (By.XPATH, "(//input[@type='text'])[12]"), "IMPORT")
        #Booking date
        safe_send_keys(driver, (By.XPATH, "(//input[@type='date'])[1]"), "25/03/2025")
        #buy/Sell
        safe_send_keys(driver, (By.XPATH, "(//input[@type='text'])[4]"), "Buy"+ Keys.ENTER)
        #Booking Amount
        safe_send_keys(driver, (By.XPATH, "(//input[@type='number'])[1]"), "320000")
        #Avail amount
        safe_send_keys(driver, (By.XPATH, "(//input[@type='text'])[9]"), "120000")
        #To date
        safe_send_keys(driver, (By.XPATH, "(//input[@type='date'])[3]"), "22/06/2025")
        #Booked under facility
        safe_send_keys(driver, (By.XPATH, "(//input[@type='text'])[11]"), "Test123")
        #Status
        safe_send_keys(driver, (By.XPATH, "(//input[@type='text'])[13]"), "Booking"+Keys.ENTER)
        #Submit
        safe_click(driver, "(//button[@id='ForwardContract'])[1]")

        toast_message = get_toast_alert_text(driver)
        print("message:" + toast_message)
        time.sleep(6)
    finally:
        # stop_event.set()
        # t.join(timeout=10)
        # print(f"✅ Screen recording saved to: {output_path}")
        print("test_success")

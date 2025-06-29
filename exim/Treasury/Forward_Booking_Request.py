import time

from exim.Src.config import *
from exim.conftest import *


def test_FBRS(driver):
    try:
        safe_click(driver, "(//a[normalize-space()='Treasury'])[1]")
        safe_click(driver, "(//h6[normalize-space()='Forward Booking Request Summary'])[1]")
        safe_click(driver, "(//p[normalize-space()='June 29, 2025 10:27 AM'])[1]")
        safe_click(driver, "(//i[@aria-hidden='true'])[5]")
        safe_click(driver, "(//*[name()='svg'][@class='close'])[3]")

        safe_click(driver, "(//button[normalize-space()='Export'])[1]")
    finally:
        print("Test_Success")
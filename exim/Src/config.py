import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def wait_for_loader(driver, timeout=40):
    try:
        classes = [
            "loading-overlay visible", "loading-overlay", "loading-main", "loader"
        ]
        for cls in classes:
            WebDriverWait(driver, timeout).until(
                EC.invisibility_of_element_located((By.CLASS_NAME, cls))
            )
    except TimeoutException:
        print("[Timeout] Loader did not disappear within time")

def safe_click(driver, xpath, timeout=40):
    try:
        wait_for_loader(driver)
        element = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )
        element.click()
        wait_for_loader(driver)
    except TimeoutException:
        print(f"[Timeout] Element {xpath} not clickable after {timeout}s")
    except Exception as e:
        print(f"[Error] Clicking {xpath}: {str(e)}")


def safe_send_keys(driver, locator, value, timeout=45):
    try:
        wait_for_loader(driver)
        element = WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        element.clear()

        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        time.sleep(0.5)
        WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(locator))
        element.send_keys(value)
        wait_for_loader(driver)
    except TimeoutException:
        print(f"[Timeout] Could not send keys to {locator}")
    except Exception as e:
        print(f"[Error] send_keys on {locator}: {str(e)}")

def upload_file_linux(driver, input_locator, file_path, timeout=40):
    file_input = WebDriverWait(driver, timeout=40).until(
        EC.presence_of_element_located(input_locator)
    )
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", file_input)
    ActionChains(driver).move_to_element(file_input).click().perform()
    time.sleep(2)
    driver.execute_script(
        """
        arguments[0].style.display = 'block';
        arguments[0].style.visibility = 'visible';
        arguments[0].style.height = '1px';
        arguments[0].style.width = '1px';
        """,
        file_input
    )
    file_input.send_keys(file_path)



def wait_until_enabled(driver, locator, timeout=60, poll_frequency=1):
    """Waits until the given element is enabled and returns it."""
    end_time = time.time() + timeout
    while time.time() < end_time:
        try:
            element = driver.find_element(*locator)
            if element.is_enabled():
                return element
        except Exception:
            pass
        time.sleep(poll_frequency)
    raise TimeoutError("⏰ Timed out waiting for element to become enabled")


def get_toast_alert_text(driver):
    try:
        # Wait for the toast message to be visible (max 10 seconds)
        toast = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'toast') or contains(text(),'Successfully')]"))
        )
        print("Toast message:", toast.text)
        return toast.text
    except:
        print("Toast message not found")
        return None








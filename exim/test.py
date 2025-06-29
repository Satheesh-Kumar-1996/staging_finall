import subprocess
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def start_screen_recording(output_file='screen_record.mp4', fps=25, resolution='1920x1080', display=':0.0'):
    cmd = [
        'ffmpeg',
        '-y',  # overwrite output file if exists
        '-video_size', resolution,
        '-framerate', str(fps),
        '-f', 'x11grab',
        '-i', display,
        output_file
    ]
    # Start recording as a subprocess (runs in background)
    return subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def stop_screen_recording(process):
    process.terminate()
    process.wait()

def run_selenium_test():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    service = Service('/usr/bin/chromedriver')  # Adjust path if needed

    driver = webdriver.Chrome(service=service, options=chrome_options)
    try:
        driver.get("https://www.google.com")
        time.sleep(3)
        search_box = driver.find_element("name", "q")
        search_box.send_keys("OpenAI ChatGPT")
        search_box.submit()
        time.sleep(5)  # wait to see results
    finally:
        driver.quit()

if __name__ == "__main__":
    # Start screen recording before test
    recorder = start_screen_recording(output_file='test_run.mp4', fps=25, resolution='1920x1080', display=':0.0')
    time.sleep(2)  # allow ffmpeg to start recording properly

    # Run Selenium test while recording
    run_selenium_test()

    # Stop screen recording after test
    stop_screen_recording(recorder)
    print("Screen recording saved as test_run.mp4")

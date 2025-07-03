import os
import time

screenshot_interval = 5  # seconds

def take_screenshot():
    while True:
        timestamp = int(time.time())
        filename = f"screenshot_{timestamp}.png"
        os.system(f"scrot {filename}")
        print(f"Screenshot saved as {filename}")
        time.sleep(screenshot_interval)

take_screenshot()

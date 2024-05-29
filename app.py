import pyautogui
import time
from pynput.keyboard import Listener, Key
import threading

clicking = False  # Flag to control auto clicking
delay = 0.1  # Default delay between clicks
clicks_at_once = 1  # Number of clicks to perform simultaneously

def clicker():
    global clicking, delay, clicks_at_once
    while clicking:
        for _ in range(clicks_at_once):
            pyautogui.click()
        time.sleep(delay)

def toggle_clicking():
    global clicking
    clicking = not clicking
    if clicking:
        print("Auto clicking enabled")
        threading.Thread(target=clicker).start()
    else:
        print("Auto clicking disabled")

def double_clicks():
    global clicks_at_once
    clicks_at_once *= 2
    print(f"Number of clicks at once doubled to {clicks_at_once}")

def halve_clicks():
    global clicks_at_once
    if clicks_at_once > 1:
        clicks_at_once //= 2
        print(f"Number of clicks at once halved to {clicks_at_once}")

def on_press(key):
    global delay
    if key == Key.f1:  # Toggle auto clicking on/off with F1
        toggle_clicking()
    elif key == Key.up:  # Increase clicking speed with up arrow
        delay -= 0.01
        print(f"Speed increased. Delay between clicks: {delay:.2f} seconds.")
    elif key == Key.down:  # Decrease clicking speed with down arrow
        delay += 0.01
        print(f"Speed decreased. Delay between clicks: {delay:.2f} seconds.")
    elif key == Key.right:  # Double the number of clicks at once with right arrow
        double_clicks()
    elif key == Key.left:  # Halve the number of clicks at once with left arrow
        halve_clicks()
    elif key == Key.esc:  # Stop the listener with ESC
        return False

def on_release(key):
    pass

# Start the listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
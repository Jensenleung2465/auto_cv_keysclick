"""
copyright jensenleung2465 2026.0425 14:30
"""

import threading
import time
from pynput.keyboard import Key, Controller, Listener, KeyCode

# --- Configuration ---
TOGGLE_KEY = Key.f1  # Key to start/stop
EXIT_KEY = Key.esc    # Key to close the script
DELAY = 0.1          # Delay between presses (seconds)
KEYS_TO_PRESS = ['c', 'v'] # Keys to spam
# ---------------------

keyboard = Controller()
running = False

def press_keys():
    """Function to spam the keys in a loop."""
    while True:
        if running:
            for key in KEYS_TO_PRESS:
                keyboard.press(key)
                keyboard.release(key)
                time.sleep(0.01) # Small delay between c and v
            time.sleep(DELAY) # Delay after both pressed
        else:
            time.sleep(0.1)

def on_press(key):
    """Toggle running state when TOGGLE_KEY is pressed."""
    global running
    if key == TOGGLE_KEY:
        running = not running
        print(f"Auto-presser running: {running}")
    elif key == EXIT_KEY:
        print("Exiting...")
        return False

# Start the thread
click_thread = threading.Thread(target=press_keys)
click_thread.start()

# Start listening to keyboard
with Listener(on_press=on_press) as listener:
    listener.join()

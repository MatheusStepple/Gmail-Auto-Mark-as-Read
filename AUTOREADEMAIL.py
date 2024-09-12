import pyautogui
import time
import webbrowser
from plyer import notification
import keyboard

def open_gmail():
    webbrowser.open('https://mail.google.com/')
    time.sleep(4)  

def mark_all_as_read():
    select_all_button = (320, 200) 
    mark_as_read_button = (520, 200)  
    
    pyautogui.click(select_all_button)
    time.sleep(1)  
    
    pyautogui.click(mark_as_read_button)
    time.sleep(1) 

    pyautogui.click(select_all_button)
    time.sleep(1)   
    notification.notify(
        title="Matheus Stepple",
        message="Your inbox is clean",
        timeout=10
    )

def run_task():
    open_gmail()
    mark_all_as_read()

def setup_hotkey():
    # Set up the hotkey
    keyboard.add_hotkey('F12', run_task)
    # Display message to inform the user
    notification.notify(
        title="Hotkey Set",
        message="Press F12 to clean your inbox. The application is running in the background.",
        timeout=10
    )

def main():
    setup_hotkey()
    # Keep the script running in the background
    print("Press F12 to clean your inbox. Press ESC to exit.")
    keyboard.wait('esc')  # Use 'esc' key to exit the script

if __name__ == "__main__":
    main()

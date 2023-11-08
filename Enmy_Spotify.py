import pyautogui
import psutil; import shutil
import subprocess
import Enmy_Settings
import os
import time

def pause_song():
    spotify_path = shutil.which('Spotify')
    subprocess.run(spotify_path)
    time.sleep(1)
    pyautogui.hotkey('space')

def skip_song():
    spotify_path = shutil.which('Spotify')
    subprocess.run(spotify_path)
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'right')

# using pyautogui to automate spotify commands/keyboard shortcuts



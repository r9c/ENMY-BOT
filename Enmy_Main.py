import pyttsx3; import speech_recognition as sr
import subprocess; import os; import sys
import pyautogui; import time
import shutil; import psutil
from Enmy_Spotify import pause_song, skip_song
from Enmy_Settings import find_chrome, find_discord

spotify_path = shutil.which('Spotify')
chrome_path = find_chrome()
discord_path = find_discord()
recog = sr.Recognizer()

def open_discord():
    if discord_path:
        subprocess.run(discord_path)
    else:
        print("Discord not found.")

while True:
    try:
        with sr.Microphone() as microphone:
            recog.adjust_for_ambient_noise(microphone, duration=0.1)
            inputAudio = recog.listen(microphone)

            text = recog.recognize_google(inputAudio)
            text = text.lower()

            # stop ENMY bot
            if "stop" in text.lower():
                print("ending ENMY bot... ")
                sys.exit()

            # open discord
            elif "open discord" in text.lower():
                open_discord()
                continue

            # spotify
            elif "pause song" in text.lower():
                pause_song()
                continue

            elif "play song" in text.lower():
                pause_song()
                continue
                
            elif "skip song" in text.lower():
                skip_song()
                continue

            # google / chrome stuff

            elif "open chrome" in text.lower():
                subprocess.run(chrome_path)

            print(text)
            if "search" in text:
                search_query = text.replace("search", "").strip()
                if chrome_path:
                    subprocess.run([chrome_path, f"https://www.google.com/search?q={search_query}"])

            

    except sr.UnknownValueError: 
        recog = sr.Recognizer()
        continue

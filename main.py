from gtts import gTTS
import io
import pygame
import re
import pyautogui
import pyperclip
from pynput import mouse
import time
import urllib.request

audio_playing = False
prev_copied_text = ''

def audio(text):
    global audio_playing

    # Create gTTS object
    tts = gTTS(text=text, lang='en')

    # Create a byte stream object to store the audio
    audio_file = io.BytesIO()

    # Use the write_to_fp() method to write the audio to the byte stream
    tts.write_to_fp(audio_file)

    # Set the position of the byte stream back to the beginning
    audio_file.seek(0)

    # Initialize pygame mixer
    pygame.mixer.init()

    # Load the audio from the byte stream using mixer.music.load()
    pygame.mixer.music.load(audio_file)

    # Play the audio using mixer.music.play()
    pygame.mixer.music.play()

    # Set audio_playing to True
    audio_playing = True

    # Wait for the audio to finish playing before exiting the program
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

    # Set audio_playing to False
    audio_playing = False

def clean(text):
    # Use regular expressions to remove non-alphabetic characters and spaces
    cleaned_text = re.sub('[^a-zA-Z ]+', '', text)
    return cleaned_text

def on_left_click(x, y, button, pressed):
    global audio_playing, prev_copied_text

    if pressed:
        # Left mouse button is pressed
        return
    else:
        # Left mouse button is released

        # Check if audio is currently playing
        if not audio_playing:
            try:
                urllib.request.urlopen('http://google.com')
            except:
                print("Please connect to the internet")
                return

            pyautogui.hotkey('ctrl', 'c')
            copied_text = pyperclip.paste()

            # Check if the copied text is the same as the previous one
            if clean(copied_text) == prev_copied_text:
                return

            prev_copied_text = clean(copied_text)
            audio(prev_copied_text)

with mouse.Listener(on_click=on_left_click) as listener:
    listener.join()

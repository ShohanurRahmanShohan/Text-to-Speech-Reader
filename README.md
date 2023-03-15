Read-Anything Aloud with Python 
===============================

NOTE: It's slow but more Automated [faster version here ](https://web.facebook.com/0Shohan0/)
------------


This Python script allows you to easily read any text from a website, PDF, or anywhere else on your computer out loud. It's a useful tool for people who prefer listening to reading, for those who have difficulty reading due to visual impairments, or for anyone who wants to multitask while still consuming information.
Additionally, the script allows you to read almost anything by simply pressing the left button of the text you want to read and hovering over it with your mouse. This means you can quickly and easily read any text on your computer without having to manually copy and paste it into another program.

Installation
------------

1.  Ensure that you have Python 3 installed on your computer.
2. pip install -r requirements.txt 
2. Or, You can Install the following dependencies manually :
    -   gtts
    -   pygame
    -   pyautogui
    -   pyperclip
    -   pynput
    -   urllib3

3.  Download the `read-anything-aloud.py` script from this repository and save it to your computer.

Usage
-----

1.  Open a terminal or command prompt and navigate to the directory where you saved the `read-anything-aloud.py` script.
2.  Run the script by typing `python read-anything-aloud.py` and pressing Enter.
3.  The script will run in the background and listen for when you click your left mouse button.
4.  To use the script, click and hold your left mouse button simply hover your mouse over any text you want to read aloud and The script will automatically copy     the text and read it aloud using the gTTS API.
5.  You can exit the script at any time by pressing Ctrl + C in the terminal or command prompt.

Customization
-------------

If you want to customize the script, you can modify the following variables:

-   `lang`: The language that the text should be read in (default is 'en').
-   `cleaned_text`: The regular expression used to remove non-alphabetic characters and spaces from the copied text (default is '[^a-zA-Z ]+').

You can also modify the `audio()` function to use a different text-to-speech API or to modify the way the audio is played.

Credits
-------

This script was created by [Shohan](https://web.facebook.com/0Shohan0/)



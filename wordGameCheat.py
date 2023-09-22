import pyautogui
import time
import pyperclip
import nltk
import random
from nltk.corpus import wordnet as wn
import keyboard


nltk.download('wordnet')
time.sleep(2)
wn.ensure_loaded()
screenwidth, screenheight = pyautogui.size()
x = screenwidth/2+20
y = screenheight/2+30

def copy():
    global copied_text 
    pyautogui.moveTo(x, y)
    pyautogui.click()
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'c') 
    copied_text = pyperclip.paste().upper()

def paste(word):
    pyautogui.moveTo(980,985)
    pyautogui.click()
    pyautogui.typewrite(word)
    pyautogui.press('enter')

def on_key_press(event):
    if event.name == 'esc':
        global running
        running = False

wordFile = open('C:\\Users\\Tim\\Documents\\Programming\\Word Game Cheat\\wordsJKLM.txt', "r")
running = True
copyd = False
while running:
    copy()
    copyd = True

    wordFile.seek(0)
    matching_words = [word for word in wordFile.read().split() if copied_text in word]
    try:
        wordPos = random.randint(0, len(matching_words) - 1)
        word = matching_words[wordPos]
    except:
        pass

    if pyautogui.pixelMatchesColor(980, 985, (32, 20, 20), tolerance=10) and copyd == True:
        try:
            paste(word)
            #pyautogui.hotkey('alt', 'tab') 
        except:
            pass
    copyd = False
    keyboard.on_press(on_key_press)
wordFile.close()

import pyautogui
import time
t = 60
pyautogui.sleep(5)
f = open("SPAMWORD", 'r')
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
    time.sleep(30)

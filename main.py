import time
import pyautogui


obstacle = (83, 83, 83)
white_obstacle = (255, 255, 255)

time.sleep(3)
pyautogui.press('Up')

while True:
    w = 600
    x = 350
    y = 650
    z = 530
    if pyautogui.pixelMatchesColor(x, y, obstacle):
        pyautogui.press('Up')
    if pyautogui.pixelMatchesColor(x, w, obstacle) and pyautogui.pixelMatchesColor(x, y, white_obstacle):
        pyautogui.press('Down')
    if pyautogui.pixelMatchesColor(x, z, obstacle):
        pyautogui.press('Down')


# https://elgoog.im/dinosaur-game/

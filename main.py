import time
import pyautogui


obstacle = (83, 83, 83)
time.sleep(3)
pyautogui.press('Up')

while True:
    if pyautogui.pixelMatchesColor(350, 650, obstacle) or pyautogui.pixelMatchesColor(300, 640, obstacle):
        pyautogui.press('Up')

    if pyautogui.pixelMatchesColor(350, 600, obstacle) or pyautogui.pixelMatchesColor(300, 600, obstacle):
        pyautogui.press('Up')

    if pyautogui.pixelMatchesColor(350, 530, obstacle) or pyautogui.pixelMatchesColor(330, 530, obstacle):
        pyautogui.press('Down')

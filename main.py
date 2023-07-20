import time
import pyautogui

time.sleep(3)
pyautogui.press('Up')

while True:
    if pyautogui.pixelMatchesColor(350, 650, (83, 83, 83)) or pyautogui.pixelMatchesColor(300, 640, (83, 83, 83)):
        pyautogui.press('Up')

    if pyautogui.pixelMatchesColor(350, 600, (83, 83, 83)) or pyautogui.pixelMatchesColor(300, 600, (83, 83, 83)):
        pyautogui.press('Up')

    if pyautogui.pixelMatchesColor(350, 530, (83, 83, 83)) or pyautogui.pixelMatchesColor(330, 530, (83, 83, 83)):
        pyautogui.press('Down')

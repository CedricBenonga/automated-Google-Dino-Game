import time
import pyautogui


obstacle = (83, 83, 83)
space_under_obs = (255, 255, 255)

time.sleep(3)
pyautogui.press('Up')

x = 350
y = 650
z = 590

while True:
    if pyautogui.pixelMatchesColor(x, y, obstacle):
        pyautogui.press('Up')
    if pyautogui.pixelMatchesColor(x, z, obstacle) and pyautogui.pixelMatchesColor(x, y, space_under_obs):
        pyautogui.press('Down')

# # # # # # # ## #  Link for the game  # # # # # # # # #
# https://elgoog.im/dinosaur-game/

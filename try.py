# import threading
# import pyautogui
#
#
# class Dino:
#     def __init__(self):
#         pyautogui.getActiveWindow().minimize()
#         pyautogui.press('space')
#         pyautogui.sleep(1)
#
#         dino = pyautogui.locateCenterOnScreen('dino.png')
#         print(dino)
#         self.x = int(dino[0])
#         self.y = int(dino[1])
#         self.offset = 100
#
#     def make_jump(self):
#         while True:
#
#             if pyautogui.pixelMatchesColor(self.x + int(self.offset), self.y,
#                                            (90, 90, 90), tolerance=100):
#                 pyautogui.press('space')
#                 self.offset += 0.7
#
#
#
#     def is_game_over(self):
#         while True:
#             if not pyautogui.locateCenterOnScreen('game_over.png') is None:
#                 pyautogui.press('space')
#                 self.offset = 100
#
#
# d = Dino()
#
# e = threading.Event()
#
# t1 = threading.Thread(target=d.make_jump)
# t1.start()
#
# t2 = threading.Thread(target=d.is_game_over)
# t2.start()
import time

import pyautogui


class Dinosaur:

    def __init__(self):
        self.jumps = 0

    def jump(self):
        pyautogui.keyDown('up')
        pyautogui.sleep(.2)
        pyautogui.keyUp('up')
        self.jumps += 1

    def sees_obstacle_ahead(self) -> bool:
        x = 715 + int(self.jumps * .3)
        pixel = pyautogui.pixel(x, 389)
        for color in pixel:
            if color < 100:
                return True
        return False


time.sleep(3)


def main():
    dino = Dinosaur()

    while True:
        if dino.sees_obstacle_ahead():
            dino.jump()


if __name__ == '__main__':
    main()

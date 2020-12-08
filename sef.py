# import cv2
# import pyws as m
# import numpy as np
# import winxpgui
# import win32gui
# from PIL import ImageGrab
# import datetime
# import time

# handle = win32gui.FindWindow(None, 'Spotify Premium')
# rect = winxpgui.GetWindowRect(handle)

# time.sleep(1)

# img = ImageGrab.grab(rect)
# img = np.asarray(img)
# img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
# cv2.imwrite('result.jpg', img)

from PIL import ImageGrab
import time
import pyautogui as pg
import re
import datetime as dt
import cv2

main_img = 'Gomibako.jpg'
#pg.locateCenterOnScreen('search.png',confidence=0.9)

if pg.locateCenterOnScreen(main_img,confidence=0.9):
    left, top, width, height = pg.locateOnScreen(main_img,confidence=0.9)
    # result = re.findall(r"\d+", str(val))
    # x,y = result[0], result[1]
    # print(x + " : " + y)
    print(left)
else:
    print("none")

import cv2
import pyws as m
import numpy as np
import winxpgui
import win32gui
from PIL import ImageGrab
import datetime
import time

# handle = win32gui.FindWindow(None, 'Spotify Premium')
# rect = winxpgui.GetWindowRect(handle)

# time.sleep(1)

# img = ImageGrab.grab(rect)
# img = np.asarray(img)
# img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
# cv2.imwrite('result.jpg', img)

x = 54
y = 30
# full screen
ImageGrab.grab().save("a.png")
# 指定した領域内をクリッピング
ImageGrab.grab(bbox=(x, x, y, y)).save("b.png")
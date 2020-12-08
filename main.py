from PIL import ImageGrab
import time
import pyautogui as pg
import re
import datetime as dt
import cv2

main_img = 'Gomibako.jpg'
#pg.locateCenterOnScreen('search.png',confidence=0.9)

if pg.locateCenterOnScreen(main_img,confidence=0.9):
    val = pg.locateCenterOnScreen(main_img,confidence=0.9)
    result = re.findall(r"\d+", str(val))
    x,y = result[0], result[1]
    print(x + " : " + y)
else:
    print("none")

while True:
    time.sleep(1)
    # full screen
    ImageGrab.grab().save(f"./tmp_img/{dt.datetime.now()}_full.png")

    # 指定した領域内をクリッピング
    tmp_img_name = f_date()
    ImageGrab.grab(bbox=(x, x, y, y)).save(f"./tmp_img/{tmp_img_name}.png")

    ret = cv2.compareHist(main_img, f"{tmp_img_name}.png", 0)

    if ret > 0.99:
        # 画像が変わっていないということ
        print("match!!")
    else:
        print("not match..")
        # 新しくtmp_img_nameを保存しmain_imgを更新
    break

def f_date():
    now = dt.datetime.now()
    return now.strftime("%m-%d-%H%M%S")


# スクリーンショット取得
#     pyautogui.moveTo(600, 600)
#     im = pyautogui.screenshot(region=(cBasePoint[0], cBasePoint[1], 410, 125))
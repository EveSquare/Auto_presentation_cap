from PIL import ImageGrab
import time
import pyautogui as pg
import re
import datetime as dt
import cv2
import os

main_img = os.listdir("./origin")[0]
exist_flag = True
wait_time = 10
#pg.locateCenterOnScreen('search.png',confidence=0.9)
try:
    if pg.locateCenterOnScreen(main_img,confidence=0.9):
        left, top, width, height = pg.locateOnScreen(main_img,confidence=0.9)
    else:
        print("none")
        exit(1)
except:
    print("元となるファイルが一致するところがありませんでした。")

def f_date():
    now = dt.datetime.now()
    return now.strftime("%m-%d-%H%M%S")

try:
    while True:
        # full screen
        # ImageGrab.grab().save(f"./tmp_img/{dt.datetime.now()}_full.png")

        # 指定した領域内をクリッピング
        tmp_img_name = f_date()
        ImageGrab.grab(bbox=(left, top, width, height)).save(f"./tmp_img/{tmp_img_name}.png")

        time.sleep(1)

        main = cv2.imread(main_img)
        main_hst = cv2.calcHist([main],[0],None,[256],[0,256])
        temp = cv2.imread(f'./tmp_img/{tmp_img_name}.png')
        temp_hst = cv2.calcHist([temp],[0],None,[256],[0,256])

        #画像の一致度を判定
        ret = cv2.compareHist(main_hst, temp_hst, 0)

        if not exist_flag:
            os.remove(not_changed_filename)
            not_changed_filename = f"./tmp_img/{tmp_img_name}.png"
        else:
            not_changed_filename = f"./tmp_img/{tmp_img_name}.png"
            exist_flag = False

        if ret > 0.98:
            # 画像が変わっていないということ
            print("not change")
            time.sleep(wait_time)
        else:
            print("changed")
            # 新しくtmp_img_nameを保存しmain_imgを更新
            tmp_img_name = f_date()
            ImageGrab.grab(bbox=(left, top, width, height)).save(f"./result/{tmp_img_name}.png")
            main_img = f"./result/{tmp_img_name}.png"
            time.sleep(wait_time)

except KeyboardInterrupt:
    exit(1)

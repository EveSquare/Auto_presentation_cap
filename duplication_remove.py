import os 
import cv2

# print(os.listdir("./result"))

print(len(os.listdir("./result")))

duplication_list = []
dup_tmp = ""
file_count = len(os.listdir("./result"))
dup_bool = True
skip_file_list = []

for i in range(file_count):
    if f"./result/{os.listdir('./result')[i]}" in skip_file_list:
        pass
    else:
        main = cv2.imread(f"./result/{os.listdir('./result')[i]}")
        for j in range(file_count):
            print(f"i:{i},j:{j}")
            if i != j:
                temp = cv2.imread(f"./result/{os.listdir('./result')[j]}")
                ret = cv2.matchTemplate(main, temp, cv2.TM_CCORR_NORMED)
                minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(ret)
                if maxVal > 0.99:
                    # 画像が変わっていないということ
                    skip_file_list.append(os.listdir('./result')[j])
                    if dup_bool:
                        dup_tmp = dup_tmp + os.listdir('./result')[j]
                        dup_bool = False
                    else:
                        dup_tmp = dup_tmp + "==" + os.listdir('./result')[j]
            if j == file_count-1:
                if dup_tmp:
                    duplication_list.append(f"{os.listdir('./result')[i]}->{dup_tmp}")
                    dup_tmp = ""
                    dup_bool = True
        

print(skip_file_list)
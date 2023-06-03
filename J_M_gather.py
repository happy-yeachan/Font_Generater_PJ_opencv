# 0716.py
import cv2
import numpy as np


def gather(j_or_m, tmp_list, filename):
    src = cv2.imread('./' + filename +'/'+ j_or_m +'.jpg')
    src = cv2.rotate(src, cv2.ROTATE_90_CLOCKWISE)
    gray = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)

    se = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 3)) # 가로 5, 세로 3
    kernel = np.ones((2, 2), np.uint8)
    gray = cv2.dilate(gray, kernel, iterations=3)

    gray = cv2.erode(gray, se)
    gray = cv2.erode(gray, se)
    # gray = cv2.erode(gray, se)

    ret, res = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY_INV)

    #2
    ret, labels, stats, centroids = cv2.connectedComponentsWithStats(res)

    #3
    dst   = np.zeros(src.shape, dtype=src.dtype)
    for i in range(1, int(ret)): # 분할영역 표시
        r, g, b = 255, 255, 255
        dst[labels == i] = [b, g, r]
    4    

    index = 0
    try:
        for i in range(1, len(res)):
            x, y, width, height, area = stats[i]
            if width < 20 and height < 20:
                continue
            cv2.rectangle(dst, (x,y), (x+width, y+height), (0, 0, 255), 2)
            roi = res[y:y+height, x:x+width]
            roi = cv2.rotate(roi, cv2.ROTATE_90_COUNTERCLOCKWISE)
            cv2.imwrite('./' + filename + '/' + tmp_list[index] + '.jpg', roi)
            # cx, cy = centroids[i]
            index += 1      
    except:
        print(filename + " 추출 완료")

    src = cv2.rotate(src, cv2.ROTATE_90_COUNTERCLOCKWISE)
    dst = cv2.rotate(dst, cv2.ROTATE_90_COUNTERCLOCKWISE)
    src = cv2.resize(src, (1000,500))
    dst = cv2.resize(dst, (1000,500))

    cv2.imshow('src',  src)
    cv2.imshow('dst',  dst) 
    cv2.waitKey()
    cv2.destroyAllWindows()



import cv2 as cv
import numpy as np

cap = cv.VideoCapture('VID_20210707_114628.mp4')
i = 0
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break
    cv.imwrite(f"frame_{i}.jpg", frame)
    i+=1

cap.release()
cv.destroyAllWindows()
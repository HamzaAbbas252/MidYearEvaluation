import cv2
import DectectionAlg
import numpy as np


import cv2
import numpy as np

cap = cv2.VideoCapture("FInaloutput.mp4")
ad1= cv2.imread("pepsi.jpg")
ad2= cv2.imread("coke.jpg")
ad3= cv2.imread("nurpur.jpg")
ad4= cv2.imread("tang.jpg")
ad5= cv2.imread("adv.jpeg")

img= cv2.imread("p3.jpg")
flag = 0
x=0
while True:
    success , frame = cap.read()
    print(x)
    print("flag",flag)
    if flag == 0 :
        x=x+1
        overlay1 = DectectionAlg.greencolordetectionCnn(frame, ad1)
        overlay2 = DectectionAlg.bluecolordetectionCnn(overlay1, ad2)
        SCREEN1 = cv2.resize(overlay2, (1000, 600), interpolation=cv2.INTER_LINEAR)
        # cv2.imshow("Final",FINAL)
        cv2.imshow("S", SCREEN1)
        if x== 12:
            flag=1
            x=0
        # cv2.waitKey(0)
        cv2.waitKey(1)
    elif flag==1:
        x=x+1
        overlay3 = DectectionAlg.greencolordetectionCnn(frame, ad4)
        # cv2.imshow("overaly3",overlay3)
        overlay4 = DectectionAlg.bluecolordetectionCnn(overlay3, ad3)
        SCREEN2 = cv2.resize(overlay4, (1000, 600), interpolation=cv2.INTER_LINEAR)
        # cv2.imshow("Final",FINAL)
        cv2.imshow("S", SCREEN2)
        if x== 12:
            flag=0
            x=0
        cv2.waitKey(1)

cv2.waitKey()
cv2.destroyAllWindows()
"""
# for screen 1
overlay1 = DectectionAlg.greencolordetectionCnn(frame, ad1)
overlay2 = DectectionAlg.bluecolordetectionCnn(overlay1, ad2)
SCREEN1 = cv2.resize(overlay2, (1000, 600), interpolation=cv2.INTER_LINEAR)
# cv2.imshow("Final",FINAL)
cv2.imshow("screen1", SCREEN1)
"""
"""
#for screen2
overlay3 = DectectionAlg.greencolordetectionCnn(img, ad4)
#cv2.imshow("overaly3",overlay3)
overlay4 = DectectionAlg.bluecolordetectionCnn(overlay3, ad3)
SCREEN2 = cv2.resize(overlay4, (1000, 600), interpolation=cv2.INTER_LINEAR)
# cv2.imshow("Final",FINAL)
cv2.imshow("Screen2", SCREEN2)
"""
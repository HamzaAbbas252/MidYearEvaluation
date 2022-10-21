import cv2
import DectectionAlg
import numpy as np


import cv2
import numpy as np


ad1= cv2.imread("pepsi.jpg")
ad2= cv2.imread("coke.jpg")
ad3= cv2.imread("nurpur.jpg")
ad4= cv2.imread("tang.jpg")
ad5= cv2.imread("adv.jpeg")
img= cv2.imread("p3.jpg")

i=0
while True:
    # for screen 1
    if i % 2 == 0 :

        overlay1= DectectionAlg. greencolordetectionCnn(img,ad1)
        overlay2 =  DectectionAlg.bluecolordetectionCnn(overlay1,ad2)
        SCREEN1= cv2.resize(overlay2, (1000,600),interpolation=cv2.INTER_LINEAR)
        #cv2.imshow("Final",FINAL)
        cv2.imshow("S",SCREEN1)
        #cv2.waitKey(0)

        cv2.waitKey(250)



    #for screen2
    elif i % 2 != 0  :

        overlay3 = DectectionAlg.greencolordetectionCnn(img, ad4)
        #cv2.imshow("overaly3",overlay3)
        overlay4 = DectectionAlg.bluecolordetectionCnn(overlay3, ad3)
        SCREEN2 = cv2.resize(overlay4, (1000, 600), interpolation=cv2.INTER_LINEAR)
        # cv2.imshow("Final",FINAL)
        cv2.imshow("S", SCREEN2)
        cv2.waitKey(250)


    i=i+1
cv2.waitKey()
cv2.destroyAllWindows()

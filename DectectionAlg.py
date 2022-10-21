import cv2
import numpy as np


def greencolordetectionCnn(frame,ad):
    img = frame
    ad2= ad
    blankedimg = cv2.resize(ad2, (img.shape[1], img.shape[0]), interpolation=cv2.INTER_AREA)
    blankedimg[:] = 0, 0, 0

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_range = np.array([45, 45, 70])
    upper_range = np.array([70, 255, 255])
    mask = cv2.inRange(hsv, lower_range, upper_range)

    #cv2.imshow("mask", mask)
    #contours

    cnts = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    for c in cnts:
        x, y, w, h = cv2.boundingRect(c)
        if (x + w - x) > 40 | (y + h - y) > 3:
            retAdd = ad2
            retAdd = cv2.resize(ad2, (w, h))

            blankedimg[y:y + h, x:x + w] = retAdd
            # cv2.imshow("blankedeeee",blankedimg)

    #cv2.imshow("mask", img)

    res = cv2.bitwise_and(img, img, mask=mask)
    #cv2.imshow("image2", res)
    #cv2.imshow("image", img)
    f = img - res
    f = np.where(f == 0, blankedimg, f)
    #cv2.imshow("Mask2", f)
    return f

def bluecolordetectionCnn(frame , ad):
        img = frame
        ad1 = ad

        blankedimg = cv2.resize(ad1, (img.shape[1], img.shape[0]), interpolation=cv2.INTER_AREA)
        blankedimg[:] = 0, 0, 0

        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        #old Values
        #lower_range = np.array([110, 50, 50])
        #upper_range = np.array([130, 255, 255])
        # new Values
        lower_range = np.array([118, 200, 40])
        upper_range = np.array([130, 255, 255])

        mask = cv2.inRange(hsv, lower_range, upper_range)

        #cv2.imshow("mask", mask)

        cnts = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        cnts = cnts[0] if len(cnts) == 2 else cnts[1]
        for c in cnts:
            x, y, w, h = cv2.boundingRect(c)
            if (x + w - x) > 40 | (y + h - y) > 3:
                retAdd = ad1
                retAdd = cv2.resize(ad1, (w, h))
                blankedimg[y:y + h, x:x + w] = retAdd
                #cv2.imshow("blankedeeee",blankedimg)

        #cv2.imshow("mask", img)
        res = cv2.bitwise_and(img, img, mask=mask)
        #cv2.imshow("image2", res)
        #cv2.imshow("image", img)
        f = img - res
        f = np.where(f == 0, blankedimg, f)
        #cv2.imshow("Mask2", f)

        return f

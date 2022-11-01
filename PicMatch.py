from unittest import result
import cv2
from numpy import mat


def readimg(PicPath):
    return cv2.imread(PicPath,0)

def picMatch(picmain:mat,pictemple:mat):
    result=cv2.matchTemplate(picmain,pictemple,cv2.TM_CCOEFF)
    h,w=pictemple.shape[:2]
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    return (w/2+max_loc[0],max_loc[1]+h/2)



from unittest import result
import cv2
from numpy import mat


def readimg(PicPath:'str 类型的图片路径 ')->mat:
    '''
    读取图片返回值

    参数:str 类型的图片路径

    返回值:返回mat类型的文件
    '''
    return cv2.imread(PicPath,0)



def picMatch(picmain:mat,pictemple:mat)->tuple:
    '''
    TM_CCOEFF,算法模板匹配图片

    参数:\n
    picmain->主图片mat文件 \n
    pictemple->模板图片mat文件\n

    返回值:返回模板匹配成功的中心点

    '''
    result=cv2.matchTemplate(picmain,pictemple,cv2.TM_CCOEFF)
    h,w=pictemple.shape[:2]
    
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    left_top = max_loc
    right_bottom = (left_top[0] + w, left_top[1] + h)
    cv2.rectangle(picmain, left_top, right_bottom, 255, 2)
    cv2.imshow('Detected',picmain)
    cv2.waitKey(0)
    return (w/2+max_loc[0],max_loc[1]+h/2)


if __name__=='__main__':
    picmain=readimg("pic.jfif")
    pictemple=readimg('error.png')
    picMatch(picmain,pictemple)
    

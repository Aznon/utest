import os 
# from PIL import Image
import time

# space=" "
# def AdbShellHead(str):
#     Adbstr="adb shell"+str
#     return Adbstr
# def showImage():
#     M=Image.open("C:/Users/xiaojia/Documents/WXWork/1688856571390461/Cache/Image/2022-10/9fc09b9185ba3cce8849372ee0eba358.jpg")
#     M.show()
# #ADB 发送
# def AdbSend(s):
#     os.system(AdbShellHead(s))
# #点
# def click(self,x:int,y:int):
#     c_str=" input tap "+str(x)+" "+str(y)
#     AdbSend(c_str)
# #点time 次
# def clicktime(self,x:int,y:int,time:int):
#     c_str=" input tap "+str(x)+" "+str(y)
#     for _ in range(1,time):
#         AdbSend(c_str)

# #滑动  start->end
# def swipe(startX,startY,endX,endY):
#     c_str=" input swipe "+str(startX)+space+str(startY)+space+str(endX)+space+str(endY)+space
#     AdbSend(c_str)


if __name__=='__main__':
    devices='huawei'
    project='XXYGf'
    time=str(time.strftime("%Y-%m-%d", time.localtime()))
    logPath='log/'+project+'/'+devices+'/'+time+'/'
   

    
    

import os
import time

#find package name and launchable-activity to start app
#--------------------
#CMDstr='aapt dump badging '+apkpath+' | findstr package'

# str1=os.popen('aapt dump badging E:\\UItest\\test.apk | findstr package').read()
# stringlist= str1.split("'"
# print(stringlist[1])

space=" "
def AdbShellHead(str):
    Adbstr="adb shell"+str
    return Adbstr
#ADB 发送
def AdbSend(s):
    os.system(AdbShellHead(s))
#点
def click(self,x:int,y:int):
    c_str=" input tap "+str(x)+" "+str(y)
    AdbSend(c_str)
#点time 次
def clicktime(self,x:int,y:int,time:int):
    c_str=" input tap "+str(x)+" "+str(y)
    for _ in range(1,time):
        AdbSend(c_str)

#滑动  start->end
def swipe(startX,startY,endX,endY):
    c_str=" input swipe "+str(startX)+space+str(startY)+space+str(endX)+space+str(endY)+space
    AdbSend(c_str)

# return package name
def FindPackageName(ApkPath):
    CMDstr='aapt dump badging '+ApkPath+' | findstr package'
    return os.popen(CMDstr).read().split("'")[1]

# return package activity
def FindPackageActivity(ApkPath):
    CMDstr='aapt dump badging '+ApkPath+' | findstr launchable-activity'
    return os.popen(CMDstr).read().split("'")[1]

#screencap 截图
def screenshot(logPath):
    if not os.path.exists(logPath):
        os.makedirs(logPath)
    CMDstr1='adb shell /system/bin/screencap -p /sdcard/sc.png'
    CMDstr2='adb pull /sdcard/sc.png '+logPath+'/'+str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
#确定设备名称
def getlogPath():
    devices=os.popen('adb devices').read().split('\n')[1].split('device')[0]
    CMDstr='adb -s '+ devices+'shell getprop ro.product.model'
    str1=os.popen(CMDstr).read()
 


if __name__=='__main__':
    # print(FindPackageName('E:\\UItest\\test.apk'))
    # print(FindPackageActivity('E:\\UItest\\test.apk'))
    # print(len(os.popen('adb devices').read().split('\n')[1].split('device')[0]))
    getlogPath()

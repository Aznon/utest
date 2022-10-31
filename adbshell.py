import os
import time

#查看链接
#查看包名和启动项Activity

#获取屏幕截图  screenshot
#ADBscreenshot='adb shell /system/bin/screencap -p /sdcard/sc.png'

ADBhead='adb '
ADBshellhead='adb shell '
ADBscreenshot=' /system/bin/screencap -p '
#截图
# def ADBscreenshot(devicesName,apkname):
    # path="log/"+apkname
    #如果没有路径就创建路径
    #截图放进目标文件夹 保存文件名

    # if not os.path.exists(path):
    #     os.makedirs(path)
    # cmd=ADBshellhead+"-s "+devicesName+ADBscreenshot+path
    # os.system(cmd)

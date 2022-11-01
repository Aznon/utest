

1，放入apk  识别 packgeName ,Activity启动项
2，检测ADB链接 记录设备名

3，启动 APK  
4，按照脚本运行，每次点击事件 截图，传回来 进行图片识别，算出点击坐标
5，
aapt dump badging  apkpath | findstr packgeName 
aapt dump badging  apkpath | findstr launchable-activity 
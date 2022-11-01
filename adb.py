
import os

#find package name and launchable-activity to start app
#--------------------
#CMDstr='aapt dump badging '+apkpath+' | findstr package'

# str1=os.popen('aapt dump badging E:\\UItest\\test.apk | findstr package').read()
# stringlist= str1.split("'"
# print(stringlist[1])


# return package name
def FindPackageName(ApkPath):
    CMDstr='aapt dump badging '+ApkPath+' | findstr package'
    return os.popen(CMDstr).read().split("'")[1]

# return package activity
def FindPackageActivity(ApkPath):
    CMDstr='aapt dump badging '+ApkPath+' | findstr launchable-activity'
    return os.popen(CMDstr).read().split("'")[1]


if __name__=='__main__':
    print(FindPackageName('E:\\UItest\\test.apk'))
    print(FindPackageActivity('E:\\UItest\\test.apk'))

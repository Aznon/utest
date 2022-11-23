# -*- encoding:utf-8 -*-

from PyQt5.QtWidgets import QMainWindow,QListView,QTreeWidget,QTreeWidgetItem
from PyQt5 import QtWidgets,Qt,QtGui
from PyQt5.QtGui import QTextCursor
from Ui_mainwindow import Ui_Utest
import re
import os
liststr=['click','dothis','doubleclick']
class fun_main(Ui_Utest,QMainWindow):
    

    def __init__(self):
        super(fun_main, self).__init__()
        self.setupUi(self)
        self.bt_selectapk.clicked.connect(self.selectclick)
        self.fileui()
        # self.textEdit_2.textChanged.connect(self.cursorget)
        # self.textEdit_2.cursorPositionChanged.connect(self.cursorget)
    
    def selectclick(self):
        path,filed= QtWidgets.QFileDialog.getOpenFileName(self, "选取文件", os.getcwd(), 
        "All Files(*);;Text Files(*.txt)")
        self.filepath.setText(path)
    
    def fileui(self):
        path='.'
        dirs=os.listdir('.')
        fileInfo = Qt.QFileInfo(path)
        fileIcon = Qt.QFileIconProvider()
        icon = QtGui.QIcon(fileIcon.icon(fileInfo))
        root = QTreeWidgetItem(self.filewindows)
        root.setText(0,path.split('/')[-1])
        root.setIcon(0,QtGui.QIcon(icon))
        self.CreateTree(dirs, root, path)
       # self.setCentralWidget(self.filewindows)


    def CreateTree(self, dirs, root, path):
        for i in dirs:
            path_new = path + '\\' + i
            if os.path.isdir(path_new):
                print(path_new+'==== '+str(os.path.isdir(path_new)))
                fileInfo = Qt.QFileInfo(path_new)
                fileIcon = Qt.QFileIconProvider()
                icon = QtGui.QIcon(fileIcon.icon(fileInfo))
                child = QTreeWidgetItem(root)
                child.setText(0,i)
                child.setIcon(0,QtGui.QIcon(icon))
                dirs_new = os.listdir(path_new)
                self.CreateTree(dirs_new, child, path_new)
            else:
                fileInfo = Qt.QFileInfo(path_new)
                fileIcon = Qt.QFileIconProvider()
                icon = QtGui.QIcon(fileIcon.icon(fileInfo))
                child = QTreeWidgetItem(root)
                child.setText(0,i)
                child.setIcon(0,QtGui.QIcon(icon))
        














###################################################################################### 
    # 获取输入光标的前 到最后一个空格的字符串
    # def cursorget(self):
    #     tc=self.textEdit_2.textCursor()
    #     chushi=tc.position()
    #     s=0
    #     m=0
    #     print(chushi)
    #     for str in range(0,tc.position()):
    #         tc.setPosition(chushi-s, QTextCursor.MoveAnchor)
    #         tc.setPosition(chushi-(s+1),QTextCursor.KeepAnchor)
    #         x=tc.selectedText()
    #         s=s+1
    #         if(x==" "):
    #             m=tc.position()
    #             print(m)
    #             break 
    #     tc.setPosition(m, QTextCursor.MoveAnchor)
    #     tc.setPosition(chushi,QTextCursor.KeepAnchor)
    #     text=tc.selectedText()
    #     print(text)
    #     self.textBrowser.setText(text)##设定 取出的字符显示到  文本框中


    # def Qcompleter(text):
    #     liststr=[]
    #     l=['aband','cccsda','cadfa','dadaf']
    #     for str in l:
    #         if re.match('ab',str) :
    #             liststr.append(str)
    #     return liststr
######################################################################################################




            
        




    

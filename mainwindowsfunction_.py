# -*- encoding:utf-8 -*-

from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtWidgets
from Ui_mainwindow import Ui_Utest
import os

class fun_main(Ui_Utest,QMainWindow):

    def __init__(self):
        super(fun_main, self).__init__()
        self.setupUi(self)
        self.select.clicked.connect(self.selectclick)
    
    def selectclick(self):
        path,filed= QtWidgets.QFileDialog.getOpenFileName(self, "选取文件", os.getcwd(), 
        "All Files(*);;Text Files(*.txt)")
        self.textEdit.setText(path)

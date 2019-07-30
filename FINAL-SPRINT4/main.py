# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LogWin.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from img2txt import Imgproc
from PyQt5 import QtCore, QtGui, QtWidgets
from Sign import Sign_up
from datalogic_LogSign import dataLogic_Acc
index = 0

class Login(object):
    def SignWin(self):
        self.Swin = QtWidgets.QWidget()
        self.ui = Sign_up()
        self.ui.setupUi(self.Swin)
        self.Swin.show()
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(275, 257)
        Dialog.setAutoFillBackground(False)
        Dialog.setStyleSheet("")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(100, 70, 71, 71))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/img/test1.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(40, 150, 61, 20))
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 150, 113, 20))
        self.lineEdit_2.setAutoFillBackground(False)
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.Reg = QtWidgets.QPushButton(Dialog)
        self.Reg.setGeometry(QtCore.QRect(20, 210, 101, 23))
        self.Reg.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.Reg.setObjectName("Reg")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(80, 20, 161, 51))
        self.label_4.setStyleSheet("font: 28pt \"MS Shell Dlg 2\";")
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.Nxt = QtWidgets.QPushButton(Dialog)
        self.Nxt.setGeometry(QtCore.QRect(160, 210, 101, 23))
        self.Nxt.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.Nxt.setObjectName("Nxt")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(-20, -20, 401, 371))
        self.label_2.setStyleSheet("background-color: rgb(170, 0, 0);")
        self.label_2.setText("")
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(90, 170, 171, 16))
        self.label_5.setText("")
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_2.raise_()
        self.label_3.raise_()
        self.lineEdit_2.raise_()
        self.Reg.raise_()
        self.label_4.raise_()
        self.Nxt.raise_()
        self.label.raise_()
        self.label_5.raise_()
        self.Nxt.clicked.connect(self.login)
        self.Reg.clicked.connect(self.SignWin)
        self.lineEdit_2.textChanged['QString'].connect(self.label_5.clear)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Welcome"))
        self.label_3.setText(_translate("Dialog", "Username"))
        self.Reg.setText(_translate("Dialog", "Create account"))
        self.label_4.setText(_translate("Dialog", "Sign-in"))
        self.Nxt.setText(_translate("Dialog", "Next"))
        
        
    def login(self): 
        Username = self.lineEdit_2.text()
        if self.UserCheck(Username) is False:
            if Username == '':
                self.label_5.setText("Empty Username")
            else:
                self.label_5.setText("Please type valid username")
        else:
            self.Reg.hide()
            self.label_3.setText("Password")
            self.lineEdit_2.clear()     
            self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
            self.Nxt.setText("Login")
            self.Nxt.clicked.disconnect(self.login)
            self.Nxt.clicked.connect(self.CheckPass)

    def login_Test(self, Username):
        success = False
        if self.UserCheck(Username) is False:
            if Username == '':
                self.label_5.setText("Empty Username")
            else:
                self.label_5.setText("Please type valid username")
        else:
            success = False
            return success
            self.Reg.hide()
            self.label_3.setText("Password")
            self.lineEdit_2.clear()     
            self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
            self.Nxt.setText("Login")
            self.Nxt.clicked.disconnect(self.login)
            self.Nxt.clicked.connect(self.CheckPass)
            
    def UserCheck(self,username):
        found = dl.doExist(username)
        return found
    
    def CheckPass(self):
        pw = self.lineEdit_2.text()
        mess = dl.doMatch(pw)
        if (mess == "Incorrect Password"):
            self.label_5.setText("Incorrect Password")      
        else:
            self.label_5.setText("Welcome "+ mess)
            self.w = Imgproc()
            self.w.show()

    def CheckPass_Test(self, pw):
        match = False
        mess = dl.doMatch(pw)
        if (mess == "Incorrect Password"):
            self.label_5.setText("Incorrect Password")      
        else:
            match = True
            return match
            self.label_5.setText("Welcome "+ mess)
            self.w = Imgproc()
            self.w.show()



if __name__ == "__main__":
    import sys
    dl = dataLogic_Acc()
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('test1.png'))
    Dialog = QtWidgets.QDialog()
    ui = Login()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


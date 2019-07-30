# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SignWin.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from datalogic_LogSign import dataLogic_Acc

class Sign_up(object):
    def setupUi(self, Signup):
        Signup.setObjectName("Signup")
        Signup.resize(275, 257)
        Signup.setAutoFillBackground(False)
        Signup.setStyleSheet("")
        self.FullnameL = QtWidgets.QLabel(Signup)
        self.FullnameL.setGeometry(QtCore.QRect(30, 60, 61, 20))
        self.FullnameL.setObjectName("FullnameL")
        self.FullnameLine = QtWidgets.QLineEdit(Signup)
        self.FullnameLine.setGeometry(QtCore.QRect(140, 60, 113, 20))
        self.FullnameLine.setAutoFillBackground(False)
        self.FullnameLine.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.FullnameLine.setText("")
        self.FullnameLine.setObjectName("FullnameLine")
        self.CreateB = QtWidgets.QPushButton(Signup)
        self.CreateB.setGeometry(QtCore.QRect(80, 200, 101, 23))
        self.CreateB.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.CreateB.setObjectName("CreateB")
        self.label_2 = QtWidgets.QLabel(Signup)
        self.label_2.setGeometry(QtCore.QRect(-20, -50, 401, 371))
        self.label_2.setStyleSheet("background-color: rgb(170, 0, 0);")
        self.label_2.setText("")
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(Signup)
        self.label_5.setGeometry(QtCore.QRect(50, 10, 181, 41))
        self.label_5.setStyleSheet("font: 28pt \"MS Shell Dlg 2\";")
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.UsernameL = QtWidgets.QLabel(Signup)
        self.UsernameL.setGeometry(QtCore.QRect(30, 90, 61, 20))
        self.UsernameL.setObjectName("UsernameL")
        self.UsernameLine = QtWidgets.QLineEdit(Signup)
        self.UsernameLine.setGeometry(QtCore.QRect(140, 90, 113, 20))
        self.UsernameLine.setAutoFillBackground(False)
        self.UsernameLine.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.UsernameLine.setText("")
        self.UsernameLine.setObjectName("UsernameLine")
        self.PasswordL = QtWidgets.QLabel(Signup)
        self.PasswordL.setGeometry(QtCore.QRect(30, 120, 61, 20))
        self.PasswordL.setObjectName("PasswordL")
        self.PasswordLine = QtWidgets.QLineEdit(Signup)
        self.PasswordLine.setGeometry(QtCore.QRect(140, 120, 113, 20))
        self.PasswordLine.setAutoFillBackground(False)
        self.PasswordLine.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.PasswordLine.setText("")
        self.PasswordLine.setObjectName("PasswordLine")
        self.PasswordL_2 = QtWidgets.QLabel(Signup)
        self.PasswordL_2.setGeometry(QtCore.QRect(30, 150, 91, 20))
        self.PasswordL_2.setObjectName("PasswordL_2")
        self.PasswordLine2 = QtWidgets.QLineEdit(Signup)
        self.PasswordLine2.setGeometry(QtCore.QRect(140, 150, 113, 20))
        self.PasswordLine2.setAutoFillBackground(False)
        self.PasswordLine2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.PasswordLine2.setText("")
        self.PasswordLine2.setObjectName("PasswordLine2")
        self.textDito = QtWidgets.QLabel(Signup)
        self.textDito.setGeometry(QtCore.QRect(30, 170, 221, 20))
        self.textDito.setText("")
        self.textDito.setObjectName("textDito")
        self.label_2.raise_()
        self.FullnameL.raise_()
        self.FullnameLine.raise_()
        self.CreateB.raise_()
        self.label_5.raise_()
        self.UsernameL.raise_()
        self.UsernameLine.raise_()
        self.PasswordL.raise_()
        self.PasswordLine.raise_()
        self.PasswordL_2.raise_()
        self.PasswordLine2.raise_()
        self.textDito.raise_()
        self.CreateB.clicked.connect(self.Reg)
        self.UsernameLine.textChanged['QString'].connect(self.textDito.clear)
        self.PasswordLine.textChanged['QString'].connect(self.textDito.clear)
        self.FullnameLine.textChanged['QString'].connect(self.textDito.clear)
        self.PasswordLine2.textChanged['QString'].connect(self.textDito.clear)
        self.retranslateUi(Signup)
        QtCore.QMetaObject.connectSlotsByName(Signup)
        self.Dl = dataLogic_Acc()

    def retranslateUi(self, Signup):
        _translate = QtCore.QCoreApplication.translate
        Signup.setWindowTitle(_translate("Signup", "Signup"))
        self.FullnameL.setText(_translate("Signup", "Full name"))
        self.CreateB.setText(_translate("Signup", "Create account"))
        self.label_5.setText(_translate("Signup", "REGISTER"))
        self.UsernameL.setText(_translate("Signup", "Username"))
        self.PasswordL.setText(_translate("Signup", "Password"))
        self.PasswordL_2.setText(_translate("Signup", "Confirm Password"))

    def Reg(self):
         fullname = self.FullnameLine.text()
         if fullname.isspace() is True or fullname == "":
            self.textDito.setText("Name not found! Try again")
         else:
             username = self.UsernameLine.text()
             if username.isspace() is True or self.UserCheck(username) is True or username == "":
                 self.textDito.setText("Username Invalid or exists. Try again")
             else:
                 password = self.PasswordLine.text()
                 password2 = self.PasswordLine2.text()
                 if password != password2 or password.isspace() is True or password == "":
                     self.textDito.setText("Passwords invalid or do not match! Try again")
                 else:
                    self.Dl.insertData(username, password, fullname)
                    self.textDito.setText("Registration Successful")

    def Reg_Test(self, fullname, username, password, password2):
         if fullname.isspace() is True or fullname == "":
            self.textDito.setText("Name not found! Try again")
            return False
         else:
             if username.isspace() is True or self.UserCheck(username) is True or username == "":
                 self.textDito.setText("Username Invalid or exists. Try again")
                 return False
             else:
                 if password != password2 or password.isspace() is True or password == "":
                     self.textDito.setText("Passwords invalid or do not match! Try again")
                     return False
                 else:
                    self.Dl.insertData(username, password, fullname)
                    self.textDito.setText("Registration Successful")
                    return True

    
    def UserCheck(self, Username):
        found = self.Dl.doExist(Username)
        return found


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('test1.png'))
    Signup = QtWidgets.QDialog()
    ui = Sign_up()
    ui.setupUi(Signup)
    Signup.show()
    sys.exit(app.exec_())


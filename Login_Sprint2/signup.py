# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signup.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import csv

class Ui_SignUp(object):
    def setupUi(self, REGISTER):
        REGISTER.setObjectName("REGISTER")
        REGISTER.resize(400, 300)
        REGISTER.setMaximumSize(400, 300)
        REGISTER.setMinimumSize(400, 300)
        self.pushButton = QtWidgets.QPushButton(REGISTER)
        self.pushButton.setGeometry(QtCore.QRect(160, 230, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(REGISTER)
        self.lineEdit.setGeometry(QtCore.QRect(170, 80, 141, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(REGISTER)
        self.lineEdit_2.setGeometry(QtCore.QRect(170, 110, 141, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(REGISTER)
        self.lineEdit_3.setGeometry(QtCore.QRect(170, 140, 141, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_4 = QtWidgets.QLineEdit(REGISTER)
        self.lineEdit_4.setGeometry(QtCore.QRect(170, 170, 141, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.Password)
        self.label = QtWidgets.QLabel(REGISTER)
        self.label.setGeometry(QtCore.QRect(90, 80, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(REGISTER)
        self.label_2.setGeometry(QtCore.QRect(90, 110, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(REGISTER)
        self.label_3.setGeometry(QtCore.QRect(90, 140, 71, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(REGISTER)
        self.label_4.setGeometry(QtCore.QRect(40, 170, 111, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(REGISTER)
        self.label_5.setGeometry(QtCore.QRect(130, 10, 171, 51))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(REGISTER)
        self.label_6.setGeometry(QtCore.QRect(90, 200, 241, 16))
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(REGISTER)
        self.label_7.setGeometry(QtCore.QRect(90, 190, 241, 31))
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.graphicsView = QtWidgets.QGraphicsView(REGISTER)
        self.graphicsView.setGeometry(QtCore.QRect(-30, -20, 441, 331))
        self.graphicsView.setStyleSheet("QGraphicsView\n"
"{\n"
" background-image: url(C:/Projectzxc/Signup.jpg);\n"
"}")
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView.raise_()
        self.pushButton.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.lineEdit_3.raise_()
        self.lineEdit_4.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.pushButton.clicked.connect(self.Rehistro)
        self.retranslateUi(REGISTER)
        QtCore.QMetaObject.connectSlotsByName(REGISTER)

    def retranslateUi(self, REGISTER):
        _translate = QtCore.QCoreApplication.translate
        REGISTER.setWindowTitle(_translate("REGISTER", "Sign Up"))
        self.pushButton.setText(_translate("REGISTER", "SIGN UP"))
        self.label.setText(_translate("REGISTER", "NAME"))
        self.label_2.setText(_translate("REGISTER", "EMAIL"))
        self.label_3.setText(_translate("REGISTER", "PASSWORD"))
        self.label_4.setText(_translate("REGISTER", "CONFIRM PASSWORD"))
        self.label_5.setText(_translate("REGISTER", "<html><head/><body><p><span style=\" font-size:22pt;\">SIGN UP</span></p></body></html>"))

            
    def Rehistro(self):
        msg = QMessageBox()
        userName = self.lineEdit.text()
        email = self.lineEdit_2.text()
        passWord = self.lineEdit_3.text()
        confirmPass = self.lineEdit_4.text()
        info = userName + ',' + passWord + ',' + email
        infor = userName + passWord + email
        K = open("AccountsP.csv", "a")
        if infor != '':
            if passWord == confirmPass:
                K.write(info + '\n')
                print("Registration Successful")
                self.label_7.setText("Registration Successful")
            elif passWord != confirmPass:
                print("Password does not match")
                self.label_7.setText("Password does not match")
                     
            K.close()
            
        else:
            msg.setWindowTitle("System")
            msg.setText("Username/Email/Password is required")
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('test1.png'))
    REGISTER = QtWidgets.QDialog()
    ui = Ui_SignUp()
    ui.setupUi(REGISTER)
    REGISTER.show()
    sys.exit(app.exec_())


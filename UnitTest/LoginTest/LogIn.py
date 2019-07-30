from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import csv 
from signup import Ui_SignUp
from NewMain import Main
from About import ABOUTSxc


class Login(object):
      
    def setupUi(self, DIZIZDAREALDEAL):
        DIZIZDAREALDEAL.setObjectName("DIZIZDAREALDEAL")
        DIZIZDAREALDEAL.resize(400, 300)
        DIZIZDAREALDEAL.setMaximumSize(400, 300)
        DIZIZDAREALDEAL.setMinimumSize(400, 300)
        self.pushButton = QtWidgets.QPushButton(DIZIZDAREALDEAL)
        self.pushButton.setGeometry(QtCore.QRect(220, 200, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(DIZIZDAREALDEAL)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 200, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit = QtWidgets.QLineEdit(DIZIZDAREALDEAL)
        self.lineEdit.setGeometry(QtCore.QRect(140, 80, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(DIZIZDAREALDEAL)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 120, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.USERNAME = QtWidgets.QLabel(DIZIZDAREALDEAL)
        self.USERNAME.setGeometry(QtCore.QRect(70, 80, 61, 16))
        self.USERNAME.setObjectName("USERNAME")
        self.label_2 = QtWidgets.QLabel(DIZIZDAREALDEAL)
        self.label_2.setGeometry(QtCore.QRect(70, 120, 61, 20))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(DIZIZDAREALDEAL)
        self.label.setGeometry(QtCore.QRect(70, 150, 281, 31))
        self.label.setText("")
        self.label.setObjectName("label")
        self.graphicsView = QtWidgets.QGraphicsView(DIZIZDAREALDEAL)
        self.graphicsView.setGeometry(QtCore.QRect(-20, -10, 441, 331))
        self.graphicsView.setStyleSheet("QGraphicsView\n"
"{\n"
" background-image: url(C:/Projectzxc/Login.jpg);\n"
"}")
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.USERNAME.raise_()
        self.label_2.raise_()
        self.label.raise_()
        self.pushButton.clicked.connect(self.Reg)
        self.pushButton_2.clicked.connect(self.Log)
        self.retranslateUi(DIZIZDAREALDEAL)
        QtCore.QMetaObject.connectSlotsByName(DIZIZDAREALDEAL)

    def retranslateUi(self, DIZIZDAREALDEAL):
        _translate = QtCore.QCoreApplication.translate
        DIZIZDAREALDEAL.setWindowTitle(_translate("DIZIZDAREALDEAL", "MUSIC IZ ALL WE GOT"))
        self.pushButton.setText(_translate("DIZIZDAREALDEAL", "REGISTER"))
        self.pushButton_2.setText(_translate("DIZIZDAREALDEAL", "LOGIN"))
        self.USERNAME.setText(_translate("DIZIZDAREALDEAL", "USERNAME"))
        self.label_2.setText(_translate("DIZIZDAREALDEAL", "PASSWORD"))
        
    def Reg(self):
        self.REGISTER = QtWidgets.QDialog()
        self.ui = Ui_SignUp()
        self.ui.setupUi(self.REGISTER)
        self.REGISTER.show()
        
    def Log(self):
        msg = QMessageBox()
        userName = self.lineEdit.text()
        passWord = self.lineEdit_2.text()
        info = userName + ',' + passWord 
        R = open("AccountsP.csv")
        csv_R = csv.reader(R)
        for user in csv_R:
            if user[0] != ' ':
                checker = user[0] + ',' + user[1]
                if info == checker:
                    print("Password Matched")
                    self.MainWindow = QtWidgets.QMainWindow()
                    self.pi = Main()
                    self.pi.setupUi(self.MainWindow)
                    self.MainWindow.show()
                    DIZIZDAREALDEAL.close()
                    self.pi.actionLogout.triggered.connect(self.Logout)
                    self.pi.actionAbout.triggered.connect(self.Aboutszxc)
                    break
        if userName == '':
            msg.setWindowTitle("System")
            msg.setText("Username/Password is required")
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.exec_()
        else:
            print("Invalid Username/Password")
            self.label.setText("Invalid Username/Password")
        R.close()

    def Log_Test(self, userName, passWord):
        msg = QMessageBox()
        success = false
        #userName = self.lineEdit.text()
        #passWord = self.lineEdit_2.text()
        info = userName + ',' + passWord 
        R = open("AccountsP.csv")
        csv_R = csv.reader(R)
        for user in csv_R:
            if user[0] != ' ':
                checker = user[0] + ',' + user[1]
                if info == checker:
                    success = true
                    print("Password Matched")
                    self.MainWindow = QtWidgets.QMainWindow()
                    self.pi = Main()
                    self.pi.setupUi(self.MainWindow)
                    self.MainWindow.show()
                    DIZIZDAREALDEAL.close()
                    self.pi.actionLogout.triggered.connect(self.Logout)
                    self.pi.actionAbout.triggered.connect(self.Aboutszxc)
                    break
        if userName == '':
            msg.setWindowTitle("System")
            msg.setText("Username/Password is required")
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.exec_()
        else:
            print("Invalid Username/Password")
            self.label.setText("Invalid Username/Password")
            
        R.close()
        return success

    def Aboutszxc(self):
        self.ABOUTS = QtWidgets.QDialog()
        self.ri = ABOUTSxc()
        self.ri.setupUi(self.ABOUTS)
        self.ABOUTS.show()
        self.ri.CLOSER.clicked.connect(self.closings)
        
    def closings(self):
        self.ABOUTS.close()
        
    def Setup(self):
        DIZIZDAREALDEAL = QtWidgets.QDialog()
        ui = Login()
        ui.setupUi(DIZIZDAREALDEAL)
        

    def Logout(self):
        self.MainWindow.close()
        DIZIZDAREALDEAL.show()
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.label.clear()
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('test1.png'))
    DIZIZDAREALDEAL = QtWidgets.QDialog()
    ui = Login()
    ui.setupUi(DIZIZDAREALDEAL)
    DIZIZDAREALDEAL.show()
    sys.exit(app.exec_())

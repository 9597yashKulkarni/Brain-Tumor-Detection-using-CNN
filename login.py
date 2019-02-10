# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from welcome import Ui_MainWindow
from signup import Ui_Dialog1
import sqlite3

class Ui_Dialog(object):
    def loginCheck(self):
        username=self.uname_lineEdit.text()
        password=self.pass_lineEdit.text()
        
        connection=sqlite3.connect("login.db")
        result=connection.execute("SELECT * FROM USERS WHERE USERNAME=? AND PASSWORD=?",(username,password))
        if(len(result.fetchall()) >0):
            print("User Found..!")
            
            #############################3
            self.welcomeWindow=QtWidgets.QMainWindow()
            self.ui=Ui_MainWindow()
            self.ui.setupUi(self.welcomeWindow)
            Dialog.hide()
            self.welcomeWindow.show()
             
            ################################
        else:
            print("User not Found..!")
        
    def signupCheck(self):
        print("Sign up Successfully") 
        
        self.signUp=QtWidgets.QDialog()
        self.ui=Ui_Dialog1()
        self.ui.setupUi(self.signUp)
        Dialog.hide()
        self.signUp.show()
             
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(594, 482)
        Dialog.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        Dialog.setStyleSheet("QDialog{\n"
"    color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 72, 255, 255), stop:0.982955 rgba(235, 230, 224, 255), stop:1 rgba(0, 0, 0, 255));\n"
"background-image: url(C:/Users/OFFICE/Desktop/neurons1.jpg);\n"
"}\n"
"QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton#login_btn{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 72, 255, 255), stop:0.982955 rgba(235, 230, 224, 255), stop:1 rgba(0, 0, 0, 255));\n"
"border:none;\n"
"}\n"
"QPushButton#signup_btn{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 180, 255, 255), stop:0.801136 rgba(235, 230, 224, 255), stop:0.982955 rgba(235, 230, 224, 255), stop:1 rgba(0, 0, 0, 255));\n"
"border:none;\n"
"}")
        self.user_name_label = QtWidgets.QLabel(Dialog)
        self.user_name_label.setGeometry(QtCore.QRect(90, 110, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.user_name_label.setFont(font)
        self.user_name_label.setStyleSheet("selection-color: rgb(255, 255, 255);")
        self.user_name_label.setAlignment(QtCore.Qt.AlignCenter)
        self.user_name_label.setObjectName("user_name_label")
        self.pass_label = QtWidgets.QLabel(Dialog)
        self.pass_label.setGeometry(QtCore.QRect(90, 210, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pass_label.setFont(font)
        self.pass_label.setAlignment(QtCore.Qt.AlignCenter)
        self.pass_label.setObjectName("pass_label")
        self.uname_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.uname_lineEdit.setGeometry(QtCore.QRect(240, 120, 161, 31))
        self.uname_lineEdit.setObjectName("uname_lineEdit")
        self.pass_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.pass_lineEdit.setGeometry(QtCore.QRect(240, 210, 161, 31))
        self.pass_lineEdit.setObjectName("pass_lineEdit")
        self.login_btn = QtWidgets.QPushButton(Dialog)
        self.login_btn.setGeometry(QtCore.QRect(140, 300, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.login_btn.setFont(font)
        self.login_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.login_btn.setObjectName("login_btn")
        #####################LOGINEVENT###################
        self.login_btn.clicked.connect(self.loginCheck)#add main detection page name here
        #loginCheck is method 
        #######################################################
        self.signup_btn = QtWidgets.QPushButton(Dialog)
        self.signup_btn.setGeometry(QtCore.QRect(320, 300, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.signup_btn.setFont(font)
        self.signup_btn.setObjectName("signup_btn")
         #####################LOGINEVENT###################
        self.signup_btn.clicked.connect(self.signupCheck)
        
        #####################################################
        self.user_name_label_2 = QtWidgets.QLabel(Dialog)
        self.user_name_label_2.setGeometry(QtCore.QRect(150, 20, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.user_name_label_2.setFont(font)
        self.user_name_label_2.setAutoFillBackground(False)
        self.user_name_label_2.setStyleSheet(";")
        self.user_name_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.user_name_label_2.setObjectName("user_name_label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.user_name_label.setText(_translate("Dialog", "Username"))
        self.pass_label.setText(_translate("Dialog", "Password"))
        self.login_btn.setText(_translate("Dialog", "LOGIN"))
        self.signup_btn.setText(_translate("Dialog", "SIGN UP"))
        self.user_name_label_2.setText(_translate("Dialog", "Login Form"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


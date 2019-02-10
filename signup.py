# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signup.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import re
from PyQt5 import QtCore, QtGui, QtWidgets
#from login import Ui_Dialog
import sqlite3
class Ui_Dialog1(object):
    def isValidEmail(email):
        if len(email) > 7:
            if re.match("^.+@([?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", email) != None:
                return True
            else:
                return False
            
        #else:
           # return False
    def signupCheck1(self):
        username=self.lineEdit.text()
       # password=self.pass1_lineEdit.text()
        
        connection=sqlite3.connect("login.db")
        result=connection.execute("SELECT * FROM USERS WHERE USERNAME=?",(username,))
        if(len(result.fetchall()) >0):
            print("Username already exists..!")
        else:
            email=self.lineEdit_2.text()
            if ((self.isValidEmail(email)) == True) :#TypeError: isValidEmail() takes 1 positional argument but 2 were given
                print ("This is a valid email address")
                connection=sqlite3.connect("login.db")
                username=self.lineEdit.text()
                email=self.lineEdit_2.text()
                password=self.lineEdit_4.text()
                cpassword=self.lineEdit_5.text()
                connection.execute("INSERT INTO USERS VALUES(?,?,?)",(username,email,password))
                if(password==cpassword):
                    connection.commit()
                    print("Registered...!")
                else:
                    print("password and cpass dont match...!")
            else:
                print("not a valid email address")
              
            
    def loginCheck1(self):
        print("signin clicked")
        from login import Ui_Dialog
        self.login=QtWidgets.QDialog()
        self.ui=Ui_Dialog()
        self.ui.setupUi(self.login)   
     #   self. Dialog1.hide()  #error=AttributeError: 'Ui_Dialog1' object has no attribute 'Dialog1'
        self.login.show()
        
   
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(560, 530)
        Dialog.setStyleSheet("QDialog{\n"
"background-image: url(C:/Users/OFFICE/Desktop/neurons1.jpg);\n"
"}\n"
"QPushButton#signup2_btn{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 72, 255, 255), stop:0.982955 rgba(235, 230, 224, 255), stop:1 rgba(0, 0, 0, 255));\n"
"border:none;\n"
"}\n"
"QPushButton#signin2_btn{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 180, 255, 255), stop:0.801136 rgba(235, 230, 224, 255), stop:0.982955 rgba(235, 230, 224, 255), stop:1 rgba(0, 0, 0, 255));\n"
"border:none;\n"
"}")
        self.user_name1_label = QtWidgets.QLabel(Dialog)
        self.user_name1_label.setGeometry(QtCore.QRect(50, 140, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.user_name1_label.setFont(font)
        self.user_name1_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.user_name1_label.setObjectName("user_name1_label")
        self.email_label_2 = QtWidgets.QLabel(Dialog)
        self.email_label_2.setGeometry(QtCore.QRect(50, 200, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.email_label_2.setFont(font)
        self.email_label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.email_label_2.setObjectName("email_label_2")
        self.pass1_label = QtWidgets.QLabel(Dialog)
        self.pass1_label.setGeometry(QtCore.QRect(50, 260, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pass1_label.setFont(font)
        self.pass1_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.pass1_label.setObjectName("pass1_label")
        self.cpassl_label = QtWidgets.QLabel(Dialog)
        self.cpassl_label.setGeometry(QtCore.QRect(50, 330, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cpassl_label.setFont(font)
        self.cpassl_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.cpassl_label.setObjectName("cpassl_label")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(290, 140, 161, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.signup2_btn = QtWidgets.QPushButton(Dialog)
        self.signup2_btn.setGeometry(QtCore.QRect(110, 440, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.signup2_btn.setFont(font)
        self.signup2_btn.setObjectName("signup2_btn")
        self.signup2_btn.clicked.connect(self.signupCheck1)
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(290, 200, 161, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(290, 330, 161, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_5.setGeometry(QtCore.QRect(290, 260, 161, 31))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.signin2_btn = QtWidgets.QPushButton(Dialog)
        self.signin2_btn.setGeometry(QtCore.QRect(330, 440, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.signin2_btn.setFont(font)
        self.signin2_btn.setObjectName("signin2_btn")
        self.signin2_btn.clicked.connect(self.loginCheck1)###############
        self.user_name_label_2 = QtWidgets.QLabel(Dialog)
        self.user_name_label_2.setGeometry(QtCore.QRect(150, 30, 261, 51))
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
        self.user_name1_label.setText(_translate("Dialog", "Username"))
        self.email_label_2.setText(_translate("Dialog", "EMAIL"))
        self.pass1_label.setText(_translate("Dialog", "Password "))
        self.cpassl_label.setText(_translate("Dialog", "Confirm Password"))
        self.signup2_btn.setText(_translate("Dialog", "SIGN UP"))
        self.signin2_btn.setText(_translate("Dialog", "SIGN IN"))
        self.user_name_label_2.setText(_translate("Dialog", "Sign Up Form"))

#import img_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog1 = QtWidgets.QDialog()
    ui = Ui_Dialog1()
    ui.setupUi(Dialog1)
    Dialog1.show()
    sys.exit(app.exec_())





########################
  
    
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forgotpass.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from PyQt5.QtWidgets import QMessageBox
class Ui_Forgotpass(object):
       #############################################
    def enterCheck(self):
        email=self.lineEdit_email1.text()
        connection=sqlite3.connect("login.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM USERS WHERE EMAIL=? ",(email,))
        result = cursor.fetchall()
        if(len(result) >0):
            for data in result:
              print("Username:",data[0])
              print("Email Id:",data[1])  
              self.textEdit.setText(data[2])
            cursor.close()
            print("User Found..!")
        else:
          self.textEdit.setText("Invalid Email")  
          print("Invalid email")
          msg = QMessageBox()
          msg.setIcon(QMessageBox.Critical)
          msg.setText("Error")
          msg.setInformativeText('Invalid Email Id')
          msg.setWindowTitle("Error")
          msg.exec_()
          #################################333
    def setupUi(self, Forgotpass):
        Forgotpass.setObjectName("Forgotpass")
        Forgotpass.resize(612, 367)
        Forgotpass.setStyleSheet("QDialog#Forgotpass{\n"
"background-image: url(F:/BE Project code/Brain-Tumor-Detection-using-CNN/GUI/BEProj/forgotpass.jpg);\n"
"}")
        self.btn_enter = QtWidgets.QPushButton(Forgotpass)
        self.btn_enter.setGeometry(QtCore.QRect(30, 260, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_enter.setFont(font)
        self.btn_enter.setStyleSheet("background-color: rgb(197, 0, 0);")
        self.btn_enter.setObjectName("btn_enter")
        ############################################
        
        self.btn_enter.clicked.connect(self.enterCheck)
        ########################################
        self.lineEdit_email1 = QtWidgets.QLineEdit(Forgotpass)
        self.lineEdit_email1.setGeometry(QtCore.QRect(30, 60, 201, 41))
        self.lineEdit_email1.setObjectName("lineEdit_email1")
        self.textEdit = QtWidgets.QTextEdit(Forgotpass)
        self.textEdit.setGeometry(QtCore.QRect(30, 150, 201, 41))
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(Forgotpass)
        QtCore.QMetaObject.connectSlotsByName(Forgotpass)

    def retranslateUi(self, Forgotpass):
        _translate = QtCore.QCoreApplication.translate
        Forgotpass.setWindowTitle(_translate("Forgotpass", "Dialog"))
        self.btn_enter.setText(_translate("Forgotpass", "ENTER"))
        self.lineEdit_email1.setPlaceholderText(_translate("Forgotpass", "Enter E-Mail ID"))
        self.textEdit.setPlaceholderText(_translate("Forgotpass", "password will be shown here"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Forgotpass = QtWidgets.QDialog()
    ui = Ui_Forgotpass()
    ui.setupUi(Forgotpass)
    Forgotpass.show()
    sys.exit(app.exec_())


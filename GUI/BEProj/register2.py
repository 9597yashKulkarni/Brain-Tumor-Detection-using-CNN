# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from inputt import Ui_MainWindow1
import sqlite3 
from PyQt5.QtWidgets import QMessageBox
#import re
#import lepl.apps.rfc3696
class Ui_Register(object):
   
        
   # def isValidEmail(email, event = None):
        
    #        if re.match("^.+@([?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$",email) != None:
    #            return True
     #       return False
    def registerCheck2(self):
       username=self.lineEdit_uname2.text()
       password=self.lineEdit_pass2.text()
       email=self.lineEdit_email2.text()
       #####################IF block start#########################################
       if email=="" or username=="" or password=="":
          msg = QMessageBox()
          msg.setIcon(QMessageBox.Critical)
          msg.setText("Error")
          msg.setInformativeText('Please fill all information')
          msg.setWindowTitle("Error")
          msg.exec_()
       else:
        if (len(username)<3):####################length of username
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText('Username should be of atleast 3 letters')
            msg.setWindowTitle("Error")
            msg.exec_()
        else:
            username=self.lineEdit_uname2.text()
            password=self.lineEdit_pass2.text()
            email=self.lineEdit_email2.text()
            connection=sqlite3.connect("login.db")
            result_e=connection.execute("SELECT * FROM USERS WHERE EMAIL=?",(email,))
            if(len(result_e.fetchall()) >0):
                print("email already exists..!")
                ######################################################Error message################################
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Error")
                msg.setInformativeText('E-mail ID already exist')
                msg.setWindowTitle("Error")
                msg.exec_()
                ######################################################################
                username=self.lineEdit_uname2.text()
                password=self.lineEdit_pass2.text()
                email=self.lineEdit_email2.text()
            result_u=connection.execute("SELECT * FROM USERS WHERE USERNAME=?",(username,))
            if(len(result_u.fetchall()) >0):
                    print("Username already exists..!")
                    ######################################################Error message################################
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Critical)
                    msg.setText("Error")
                    msg.setInformativeText('Username already exist')
                    msg.setWindowTitle("Error")
                    msg.exec_()
                    ######################################################################
            else:
                   username=self.lineEdit_uname2.text()
                   email=self.lineEdit_email2.text()
                   password=self.lineEdit_pass2.text()
                   cpassword=self.lineEdit_cpass2.text()
                   #################Email pattern#####################
             #if self.isValidEmail(email) == True :
                 #print("This is a valid email address")
                 ################pass and cpass check##################
            
              
                   if(password==cpassword):
                       connection.execute("INSERT INTO USERS VALUES(?,?,?)",(username,email,password))
                       connection.commit()
                       print("Registered...!")
                    #   msg = QMessageBox()
                     #  msg.setIcon(QMessageBox.Information)
                      # msg.setText("Info:")
                       #msg.setInformativeText("Registered...!")
                       #msg.setWindowTitle("Info")
                       #msg.exec_()
                       
                      
                       self.windoww=QtWidgets.QMainWindow()
                       self.ui=Ui_MainWindow1()
                       self.ui.setupUi(self.windoww)
                       #Register.hide()  ##################errorrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr
                       self.windoww.show()
                   else:
                      print("password and cpass dont match...!")
                      ######################################################Error message################################
                      msg = QMessageBox()
                      msg.setIcon(QMessageBox.Critical)
                      msg.setText("Error")
                      msg.setInformativeText("password and cpass don't match...!")
                      msg.setWindowTitle("Error")
                      msg.exec_()
         #####################ELSE  block ends#########################################    
    def setupUi(self, Register):
        Register.setObjectName("Register")
        Register.resize(1920, 1080)
        Register.setStyleSheet("background-image: url(F:/BE Project code/Brain-Tumor-Detection-using-CNN/GUI/BEProj/Main.jpg);")
        self.Reg = QtWidgets.QWidget(Register)
        self.Reg.setObjectName("Reg")
        self.frame_left2 = QtWidgets.QFrame(self.Reg)
        self.frame_left2.setGeometry(QtCore.QRect(250, 200, 481, 571))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.frame_left2.setFont(font)
        self.frame_left2.setStyleSheet("background-image: url(F:/BE Project code/Brain-Tumor-Detection-using-CNN/GUI/BEProj/right.jpg);\n"
"\n"
"\n"
"\n"
"")
        self.frame_left2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_left2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_left2.setObjectName("frame_left2")
        self.register_btn = QtWidgets.QPushButton(self.frame_left2)
        self.register_btn.setGeometry(QtCore.QRect(50, 470, 371, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.register_btn.setFont(font)
        self.register_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.register_btn.setStyleSheet("QPushButton#register_btn{\n"
"background-color: rgb(57, 76, 127);\n"
"}\n"
"")
        self.register_btn.setObjectName("register_btn")
        ####################################################
        self.register_btn.clicked.connect(self.registerCheck2)
        #####################################################
        self.plainTextEdit_wel1 = QtWidgets.QPlainTextEdit(self.frame_left2)
        self.plainTextEdit_wel1.setGeometry(QtCore.QRect(50, 30, 291, 91))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.plainTextEdit_wel1.setFont(font)
        self.plainTextEdit_wel1.setStyleSheet("QPlainTextEdit#plainTextEdit_wel1{\n"
"\n"
"border:none;\n"
"}")
        self.plainTextEdit_wel1.setReadOnly(True)
        self.plainTextEdit_wel1.setObjectName("plainTextEdit_wel1")
        self.lineEdit_email2 = QtWidgets.QLineEdit(self.frame_left2)
        self.lineEdit_email2.setGeometry(QtCore.QRect(50, 150, 371, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_email2.setFont(font)
        self.lineEdit_email2.setInputMethodHints(QtCore.Qt.ImhEmailCharactersOnly)
        self.lineEdit_email2.setObjectName("lineEdit_email2")
        self.lineEdit_uname2 = QtWidgets.QLineEdit(self.frame_left2)
        self.lineEdit_uname2.setGeometry(QtCore.QRect(50, 230, 371, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_uname2.setFont(font)
        self.lineEdit_uname2.setObjectName("lineEdit_uname2")
        self.lineEdit_pass2 = QtWidgets.QLineEdit(self.frame_left2)
        self.lineEdit_pass2.setGeometry(QtCore.QRect(50, 300, 371, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_pass2.setFont(font)
        self.lineEdit_pass2.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhSensitiveData)
        self.lineEdit_pass2.setObjectName("lineEdit_pass2")
                #####################################67687788878
        self.lineEdit_pass2.setEchoMode(QtWidgets.QLineEdit.Password)
        #######################################3        
        self.lineEdit_cpass2 = QtWidgets.QLineEdit(self.frame_left2)
        self.lineEdit_cpass2.setGeometry(QtCore.QRect(50, 370, 371, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_cpass2.setFont(font)
        self.lineEdit_cpass2.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhSensitiveData)
        self.lineEdit_cpass2.setClearButtonEnabled(False)
        #self.lineEdit_cpass2.setObjectName("lineEdit_cpass2")
                #####################################67687788878
        self.lineEdit_cpass2.setEchoMode(QtWidgets.QLineEdit.Password)
        #######################################3
        self.frame_right2 = QtWidgets.QFrame(self.Reg)
        self.frame_right2.setGeometry(QtCore.QRect(1020, 200, 481, 571))
        self.frame_right2.setStyleSheet("background-image: url(F:/BE Project code/Brain-Tumor-Detection-using-CNN/GUI/BEProj/left.jpg);")
        self.frame_right2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_right2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_right2.setObjectName("frame_right2")
        self.textEdit_health2 = QtWidgets.QTextEdit(self.frame_right2)
        self.textEdit_health2.setGeometry(QtCore.QRect(1020, 200, 301, 51))
        self.textEdit_health2.setStyleSheet("QTextEdit#textEdit_health2{\n"
"border:none;\n"
"}")
        self.textEdit_health2.setReadOnly(True)
        self.textEdit_health2.setObjectName("textEdit_health2")
        self.textEdit_slogan2 = QtWidgets.QTextEdit(self.frame_right2)
        self.textEdit_slogan2.setGeometry(QtCore.QRect(100, 230, 301, 251))
        self.textEdit_slogan2.setStyleSheet("\n"
"border:none;\n"
"")
        self.textEdit_slogan2.setReadOnly(True)
        self.textEdit_slogan2.setObjectName("textEdit_slogan2")
        self.textEdit_health2_2 = QtWidgets.QTextEdit(self.frame_right2)
        self.textEdit_health2_2.setGeometry(QtCore.QRect(100, 40, 301, 161))
        self.textEdit_health2_2.setStyleSheet("QTextEdit#textEdit_health2_2{\n"
"border:none;\n"
"}")
        self.textEdit_health2_2.setReadOnly(True)
        self.textEdit_health2_2.setObjectName("textEdit_health2_2")
        self.frame_left2.raise_()
        self.frame_right2.raise_()
        self.textEdit_slogan2.raise_()
        Register.setCentralWidget(self.Reg)
        self.statusbar = QtWidgets.QStatusBar(Register)
        self.statusbar.setObjectName("statusbar")
        Register.setStatusBar(self.statusbar)

        self.retranslateUi(Register)
        QtCore.QMetaObject.connectSlotsByName(Register)

    def retranslateUi(self, Register):
        _translate = QtCore.QCoreApplication.translate
        Register.setWindowTitle(_translate("Register", "MainWindow"))
        self.register_btn.setText(_translate("Register", "REGISTER"))
        self.plainTextEdit_wel1.setPlainText(_translate("Register", "\n"
"Register Here...!"))
        self.lineEdit_email2.setPlaceholderText(_translate("Register", "E-Mail ID"))
        self.lineEdit_uname2.setPlaceholderText(_translate("Register", "USERNAME"))
        self.lineEdit_pass2.setPlaceholderText(_translate("Register", "PASSWORD"))
        self.lineEdit_cpass2.setPlaceholderText(_translate("Register", "Confirm Password"))
        self.textEdit_health2.setHtml(_translate("Register", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt; color:#ffffff;\">HEALTHCARE</span></p></body></html>"))
        self.textEdit_slogan2.setHtml(_translate("Register", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-style:italic; color:#ffffff;\">The Knowledge to Save </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-style:italic; color:#ffffff;\">LIVES</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-style:italic; color:#ffffff;\">The Location to Save </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-style:italic; color:#ffffff;\">TIME</span></p></body></html>"))
        self.textEdit_health2_2.setHtml(_translate("Register", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt; color:#ffffff;\">HEALTHCARE</span></p></body></html>"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Register = QtWidgets.QMainWindow()
    ui = Ui_Register()
    ui.setupUi(Register)
    Register.show()
    sys.exit(app.exec_())


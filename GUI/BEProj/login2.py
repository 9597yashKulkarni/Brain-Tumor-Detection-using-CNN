# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from inputt import Ui_MainWindow1
from register2 import Ui_Register
import sqlite3
from forgotpass import Ui_Forgotpass
from PyQt5.QtWidgets import QMainWindow

class Ui_MainWindow(QMainWindow):
    def loginCheck(self):
        username=self.lineEdit_uname.text()
        password=self.lineEdit_pass.text()  
        connection=sqlite3.connect("login.db")
        result=connection.execute("SELECT * FROM USERS WHERE USERNAME=? AND PASSWORD=?",(username,password))
        if(len(result.fetchall()) >0):
            print("User Found..!")
            
            #############################
            self.predictWindow=QtWidgets.QMainWindow()
            self.ui=Ui_MainWindow1()
            self.ui.setupUi(self.predictWindow)
            MainWindow.hide()
            self.predictWindow.show()
             
            ################################
        else:
          print("User not Found..!")
         ######################################################Error message################################
          msg = QMessageBox()
          msg.setIcon(QMessageBox.Critical)
          msg.setText("Error")
          msg.setInformativeText('User not found')
          msg.setWindowTitle("Error")
          msg.exec_()
          ######################################################################
    def registerCheck(self):
        print("Clicked on Register") 
        self.Register=QtWidgets.QMainWindow()
        self.ui=Ui_Register()
        self.ui.setupUi(self.Register)
        MainWindow.hide()
        self.Register.show()
        
    def forgotpassCheck(self):
        print("Clicked on Register") 
        self.Forgotpass=QtWidgets.QMainWindow()
        self.ui=Ui_Forgotpass()
        self.ui.setupUi(self.Forgotpass)
        #MainWindow.hide()
        self.Forgotpass.show()    
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        MainWindow.setStyleSheet("\n"
"background-image: url(F:/BE Project code/Brain-Tumor-Detection-using-CNN/GUI/BEProj/Main.jpg);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_right = QtWidgets.QFrame(self.centralwidget)
        self.frame_right.setGeometry(QtCore.QRect(1020, 200, 481, 571))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.frame_right.setFont(font)
        self.frame_right.setStyleSheet("background-image: url(F:/BE Project code/Brain-Tumor-Detection-using-CNN/GUI/BEProj/right.jpg);\n"
"\n"
"\n"
"")
        self.frame_right.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_right.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_right.setObjectName("frame_right")
        self.reg_btn = QtWidgets.QPushButton(self.frame_right)
        self.reg_btn.setGeometry(QtCore.QRect(40, 500, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.reg_btn.setFont(font)
        self.reg_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.reg_btn.setStyleSheet("QPushButton#reg_btn{\n"
"\n"
"border:none;\n"
"}")
        self.reg_btn.setObjectName("reg_btn")
               ###################################### 
        self.reg_btn.clicked.connect(self.registerCheck)
        ######################################
        self.login_btn = QtWidgets.QPushButton(self.frame_right)
        self.login_btn.setGeometry(QtCore.QRect(40, 440, 401, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.login_btn.setFont(font)
        self.login_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.login_btn.setStyleSheet("background-color: rgb(57, 76, 127);\n"
"")
        self.login_btn.setObjectName("login_btn")
        ############################################
        
        self.login_btn.clicked.connect(self.loginCheck)#add main detection page name here
        #loginCheck is method 
        
        
        
        
        
        
        ############################################################        
        self.plainTextEdit_wel = QtWidgets.QPlainTextEdit(self.frame_right)
        self.plainTextEdit_wel.setGeometry(QtCore.QRect(40, 160, 291, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.plainTextEdit_wel.setFont(font)
        self.plainTextEdit_wel.setStyleSheet("QPlainTextEdit#plainTextEdit_wel{\n"
"\n"
"border:none;\n"
"}")
        self.plainTextEdit_wel.setReadOnly(True)
        self.plainTextEdit_wel.setObjectName("plainTextEdit_wel")
        self.forgotPass_btn = QtWidgets.QPushButton(self.frame_right)
        self.forgotPass_btn.setGeometry(QtCore.QRect(310, 500, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(50)
        self.forgotPass_btn.setFont(font)
        self.forgotPass_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.forgotPass_btn.setStyleSheet("QPushButton#signup_btn{\n"
"\n"
"border:none;\n"
"}")
        self.forgotPass_btn.setObjectName("forgotPass_btn")
        ################################################
        self.forgotPass_btn.clicked.connect(self.forgotpassCheck)
        ################################################        
        self.plainTextEdit_cont = QtWidgets.QPlainTextEdit(self.frame_right)
        self.plainTextEdit_cont.setGeometry(QtCore.QRect(40, 230, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.plainTextEdit_cont.setFont(font)
        self.plainTextEdit_cont.setStyleSheet("QPlainTextEdit#plainTextEdit_cont{\n"
"\n"
"border:none;\n"
"}")
        self.plainTextEdit_cont.setReadOnly(True)
        self.plainTextEdit_cont.setObjectName("plainTextEdit_cont")
        self.graphicsView_brain = QtWidgets.QGraphicsView(self.frame_right)
        self.graphicsView_brain.setGeometry(QtCore.QRect(40, 20, 101, 111))
        self.graphicsView_brain.setStyleSheet("QGraphicsView{\n"
"    background-image: url(F:/BE Project code/Brain-Tumor-Detection-using-CNN/GUI/BEProj/brain5.jpg);\n"
"border:none;}")
        self.graphicsView_brain.setObjectName("graphicsView_brain")
        self.lineEdit_uname = QtWidgets.QLineEdit(self.frame_right)
        self.lineEdit_uname.setGeometry(QtCore.QRect(40, 280, 401, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_uname.setFont(font)
        self.lineEdit_uname.setObjectName("lineEdit_uname")
        self.lineEdit_pass = QtWidgets.QLineEdit(self.frame_right)
        self.lineEdit_pass.setGeometry(QtCore.QRect(40, 360, 401, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_pass.setFont(font)
        self.lineEdit_pass.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhSensitiveData)
        #self.lineEdit_pass.setObjectName("lineEdit_pass")
        #####################################67687788878
        self.lineEdit_pass.setEchoMode(QtWidgets.QLineEdit.Password)
        #######################################3
        self.frame_left = QtWidgets.QFrame(self.centralwidget)
        self.frame_left.setGeometry(QtCore.QRect(250, 200, 481, 571))
        self.frame_left.setStyleSheet("background-image: url(F:/BE Project code/Brain-Tumor-Detection-using-CNN/GUI/BEProj/left.jpg);")
        self.frame_left.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_left.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_left.setObjectName("frame_left")
        self.textEdit_health = QtWidgets.QTextEdit(self.frame_left)
        self.textEdit_health.setGeometry(QtCore.QRect(90, 50, 301, 161))
        self.textEdit_health.setStyleSheet("QTextEdit#textEdit_health{\n"
"border:none;\n"
"}")
        self.textEdit_health.setReadOnly(True)
        self.textEdit_health.setObjectName("textEdit_health")
        self.textEdit_slogan = QtWidgets.QTextEdit(self.frame_left)
        self.textEdit_slogan.setGeometry(QtCore.QRect(90, 220, 301, 251))
        self.textEdit_slogan.setStyleSheet("\n"
"border:none;\n"
"")
        self.textEdit_slogan.setReadOnly(True)
        self.textEdit_slogan.setObjectName("textEdit_slogan")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.reg_btn.setText(_translate("MainWindow", "Register"))
        self.login_btn.setText(_translate("MainWindow", "LOGIN"))
        self.plainTextEdit_wel.setPlainText(_translate("MainWindow", "Welcome User"))
        
        self.forgotPass_btn.setText(_translate("MainWindow", "Forgot password?"))
        self.plainTextEdit_cont.setPlainText(_translate("MainWindow", "sign in to continue"))
        self.lineEdit_uname.setPlaceholderText(_translate("MainWindow", "USERNAME"))
        self.lineEdit_pass.setPlaceholderText(_translate("MainWindow", "PASSWORD"))
        self.textEdit_health.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt; color:#ffffff;\">HEALTHCARE</span></p></body></html>"))
        self.textEdit_slogan.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
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



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


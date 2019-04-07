# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'welcomepg.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
from login2 import Ui_MainWindow
from register2 import Ui_Register
from PyQt5 import QtCore, QtGui, QtWidgets
from predict import *
class Ui_MainWindow2(object):
    def openLoginWindow(self):
        self.window= QtWidgets.QMainWindow2()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()
                
    def openRegisterWindow(self):
        self.window= QtWidgets.QMainWindow()
        self.ui=Ui_Register()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.244318, fy:0.773, stop:0 rgba(36, 131, 198, 206), stop:0.35 rgba(255, 188, 188, 80), stop:0.4 rgba(255, 162, 162, 80), stop:0.425 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), stop:1 rgba(255, 255, 255, 0));")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.leftframe = QtWidgets.QFrame(self.centralwidget)
        self.leftframe.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.leftframe.setStyleSheet("\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(147, 106, 55, 255), stop:1 rgba(255, 255, 255, 255));")
        self.leftframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.leftframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.leftframe.setLineWidth(0)
        self.leftframe.setObjectName("leftframe")
        self.label = QtWidgets.QLabel(self.leftframe)
        self.label.setGeometry(QtCore.QRect(350, 90, 431, 51))
        font = QtGui.QFont()
        font.setFamily("Bodoni MT")
        font.setPointSize(17)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label.setLineWidth(0)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setWordWrap(True)
        self.label.setIndent(0)
        self.label.setObjectName("label")
        self.register_2 = QtWidgets.QPushButton(self.leftframe)
        self.register_2.setGeometry(QtCore.QRect(400, 310, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.register_2.setFont(font)
        self.register_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.register_2.setAutoFillBackground(False)
        self.register_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 178, 39, 255), stop:1 rgba(255, 255, 255, 255));\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("F:/BE Project code/Brain-Tumor-Detection-using-CNN/GUI/BEProj/register.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.register_2.setIcon(icon)
        self.register_2.setIconSize(QtCore.QSize(20, 20))
        self.register_2.setObjectName("register_2")
        self.register_2.clicked.connect(self.openRegisterWindow)
        self.label_4 = QtWidgets.QLabel(self.leftframe)
        self.label_4.setGeometry(QtCore.QRect(70, 420, 91, 71))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("F:/BE Project code/Brain-Tumor-Detection-using-CNN/GUI/BEProj/contactus.jpg"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.leftframe)
        self.label_5.setGeometry(QtCore.QRect(50, 510, 181, 16))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.leftframe)
        self.label_6.setGeometry(QtCore.QRect(40, 530, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_2 = QtWidgets.QLabel(self.leftframe)
        self.label_2.setGeometry(QtCore.QRect(820, 70, 111, 101))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("F:/BE Project code/Brain-Tumor-Detection-using-CNN/GUI/BEProj/brain5.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.leftframe)
        self.pushButton.setGeometry(QtCore.QRect(800, 310, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 178, 39, 255), stop:1 rgba(255, 255, 255, 255));")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("F:/BE Project code/Brain-Tumor-Detection-using-CNN/GUI/BEProj/images.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(20, 20))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.openLoginWindow)
        self.gridLayout.addWidget(self.leftframe, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1077, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "WE CARE FOR YOUR HEALTH..!!! "))
        self.register_2.setText(_translate("MainWindow", "NEW USER??\n"
"Register First.."))
        self.label_5.setText(_translate("MainWindow", "020-1234654/45 OR"))
        self.label_6.setText(_translate("MainWindow", "healthcare@gmail.com"))
        self.pushButton.setText(_translate("MainWindow", "Have Account??\n"
"   Login..."))

#import image2_rc
#import images_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow2()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


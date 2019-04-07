# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'inputt.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow,QApplication,QFileDialog
#from register2 import Ui_Register
class Ui_MainWindow1(QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStatusTip("")
        self.frame.setStyleSheet("\n"
"background-color: rgb(214, 214, 214);")
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setLineWidth(0)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setEnabled(True)
        self.frame_2.setGeometry(QtCore.QRect(690, 200, 331, 481))
        self.frame_2.setAutoFillBackground(False)
        self.frame_2.setStyleSheet("")
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(60, 10, 131, 121))
        self.label.setAutoFillBackground(False)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("F:/BE Project code/Brain-Tumor-Detection-using-CNN/GUI/BEProj/brain-logo-new-final-twitter.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(30, 210, 261, 211))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setObjectName("label_2")
        self.label.raise_()
        self.label_2.raise_()
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(40, 20, 601, 791))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("F:/BE Project code/Brain-Tumor-Detection-using-CNN/GUI/BEProj/Doctor-Symbol-Caduceus-Free-Download-PNG.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(970, 30, 751, 751))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setBold(True)
        font.setWeight(75)
        self.frame_3.setFont(font)
        self.frame_3.setWhatsThis("")
        self.frame_3.setStyleSheet("")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit.setGeometry(QtCore.QRect(30, 190, 431, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit.setFont(font)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setGeometry(QtCore.QRect(50, 30, 641, 141))
        font = QtGui.QFont()
        font.setFamily("MingLiU_HKSCS-ExtB")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.frame_3)
        self.pushButton.setGeometry(QtCore.QRect(140, 270, 261, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(85, 0, 255);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("F:/BE Project code/Brain-Tumor-Detection-using-CNN/GUI/BEProj/images.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(21, 21))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.predictCancer)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_2.setGeometry(QtCore.QRect(490, 190, 151, 51))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(85, 0, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.openFileDialog)
        '''self.pushButton_3 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_3.setGeometry(QtCore.QRect(140, 350, 261, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(85, 0, 255);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/moreinfo/F:/BE Project code/Brain-Tumor-Detection-using-CNN/GUI/BEProj/moreinfo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setIconSize(QtCore.QSize(21, 21))
        self.pushButton_3.setObjectName("pushButton_3")'''
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_4.setGeometry(QtCore.QRect(370, 700, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: rgb(85, 0, 255);")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("F:/BE Project code/Brain-Tumor-Detection-using-CNN/GUI/BEProj/logout.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_5 = QtWidgets.QLabel(self.frame_3)
        self.label_5.setGeometry(QtCore.QRect(100, 470, 411, 51))
        font = QtGui.QFont()
        font.setFamily("Lucida Bright")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.label_5.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame_3)
        self.label_6.setGeometry(QtCore.QRect(50, 540, 581, 141))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.label_6.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1630, 51))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionRegister = QtWidgets.QAction(MainWindow)
        self.actionRegister.setText("")
        self.actionRegister.setIconText("")
        self.actionRegister.setObjectName("actionRegister")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.frame.setWhatsThis(_translate("MainWindow", "register"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p>Take care of your body</p><p>its The Only Place </p><p>you Live ...</p></body></html>"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Enter image to process"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p>You are just one step ahead </p><p>to get your output...</p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Submit"))
        self.pushButton_2.setText(_translate("MainWindow", "Browse"))
        #self.pushButton_3.setText(_translate("MainWindow", "More Info"))
        self.pushButton_4.setText(_translate("MainWindow", "LOGOUT"))
        self.actionRegister.setToolTip(_translate("MainWindow", "register"))
    def openFileDialog(self):
        self.fileName=QFileDialog.getOpenFileName(self,'Open File','*')
        if self.fileName:
            print(self.fileName)
            self.lineEdit.setText(self.fileName[0])
            #return(self.fileName[0])
        else:
            print("None")
            #self.lineEdit.show()
    def predictCancer(self):
            tno=0
            img='testImage'+str(tno)+'.png'
            from nilearn import plotting
            display = plotting.plot_epi(self.fileName[0],output_file=img)
            print(tno)
            from keras.models import model_from_json
            json_file = open('model.json', 'r')
            loaded_model_json = json_file.read()
            json_file.close()
            loaded_model = model_from_json(loaded_model_json)
            # load weights into new model
            loaded_model.load_weights("model.h5")
            print("Loaded model from disk")
            import numpy as np
            from keras.preprocessing import image
            #classifier.load('file_name.h5')\n",
            test_image = image.load_img(img, target_size = (64, 64))
            test_image = image.img_to_array(test_image)
            test_image = np.expand_dims(test_image, axis = 0)
            result = loaded_model.predict(test_image)
            #training_set.class_indices
            if result == 1:
                 prediction = 'LGG'
                 self.label_5.setText("This MRI has non-cancerous cells")
            else:
                 prediction = 'HGG'
                 self.label_5.setText("This MRI has cancerous cells")
            print(result)
            print(prediction)
            
            if prediction=='LGG':
                self.label_6.setText("Lgg- They are classified as a grade 2 tumor making them slowest growing \ntype of glioma in adults. low grade gliomas would encompass grade I and \ngrade II neuro-epithelial tumours in childs. Most low-grade gliomas are \nboth highly treatable and highly curable. Low-grade cancers usually have \na better prognos is than high-grade cancers and may not need \ntreatment right away.")
            else:
                self.label_6.setText("HGG -They are classified as grade 4 tumor in most cases. High-grade cancer \ncells tend to grow and spread more quickly than low-grade cancer cells.\nCancer grade may be used to help plan treatment and determined to help \nplan treatment and determine prognosis. High-grade cancers usually have a \nworse prognosis than low-grade cancers and may need treatment \nright away or treatment that is more aggressive (intensive).")
#import inputt_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow1()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'predict.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_predict(object):
    def setupUi(self, predict):
        predict.setObjectName("predict")
        predict.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(predict)
        self.centralwidget.setObjectName("centralwidget")
        predict.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(predict)
        self.statusbar.setObjectName("statusbar")
        predict.setStatusBar(self.statusbar)

        self.retranslateUi(predict)
        QtCore.QMetaObject.connectSlotsByName(predict)

    def retranslateUi(self, predict):
        _translate = QtCore.QCoreApplication.translate
        predict.setWindowTitle(_translate("predict", "MainWindow"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    predict = QtWidgets.QMainWindow()
    ui = Ui_predict()
    ui.setupUi(predict)
    predict.show()
    sys.exit(app.exec_())


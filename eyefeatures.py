# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eyefeatures.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(846, 560)
        MainWindow.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(200, 470, 391, 31))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(780, 50, 31, 33))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(780, 90, 31, 33))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(780, 130, 31, 33))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(780, 170, 31, 33))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 50, 701, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 90, 471, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 170, 491, 21))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 130, 571, 21))
        self.label_6.setObjectName("label_6")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 210, 571, 21))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(780, 210, 31, 33))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_9.setGeometry(QtCore.QRect(690, 0, 151, 33))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 10, 131, 21))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(10, 250, 611, 21))
        self.label_8.setObjectName("label_8")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(780, 250, 31, 33))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(10, 290, 781, 21))
        self.label_9.setObjectName("label_9")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(780, 290, 31, 33))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(10, 330, 521, 21))
        self.label_10.setObjectName("label_10")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_10.setGeometry(QtCore.QRect(780, 330, 31, 33))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(10, 370, 601, 21))
        self.label_11.setObjectName("label_11")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_11.setGeometry(QtCore.QRect(780, 370, 31, 33))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(10, 410, 551, 21))
        self.label_12.setObjectName("label_12")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_12.setGeometry(QtCore.QRect(780, 410, 31, 33))
        self.lineEdit_12.setObjectName("lineEdit_12")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Eye Features"))
        self.pushButton.setText(_translate("MainWindow", "Store Eye Features in Data base"))
        self.lineEdit_3.setText(_translate("MainWindow", "1"))
        self.lineEdit_4.setText(_translate("MainWindow", "1"))
        self.lineEdit_5.setText(_translate("MainWindow", "1"))
        self.lineEdit_6.setText(_translate("MainWindow", "1"))
        self.label_3.setText(_translate("MainWindow", "Maximum PD{\'PD Max Abnormal\':-1,\'PD Max Prolonged\':0,\'PD Max Normal\':1}"))
        self.label_4.setText(_translate("MainWindow", "Mean PD {\'Usual Mean PD\':1,\'Poor Mean PD\':0}"))
        self.label_5.setText(_translate("MainWindow", "PD Min X-Axis {\'X PD Min Up\':1,\'X PD Min Down\':0}"))
        self.label_6.setText(_translate("MainWindow", "PD Max X-Axis {\'X PD Max normal\':1,\'X PD Max abnormal\':0}"))
        self.label_2.setText(_translate("MainWindow", "PD Max Y-Axis {\'Usual Y PD Max\':1,\'Depressed Y PD Max\':0}"))
        self.lineEdit_2.setText(_translate("MainWindow", "1"))
        self.lineEdit_9.setText(_translate("MainWindow", "001"))
        self.label_7.setText(_translate("MainWindow", "Patient ID:"))
        self.label_8.setText(_translate("MainWindow", "PD Min Y-Axis {\'Y PD Min normal\':1,\'Y PD Min abnormal\':0}"))
        self.lineEdit_7.setText(_translate("MainWindow", "1"))
        self.label_9.setText(_translate("MainWindow", "Minimum PD {\'PD Min above Range\':-1,\'PD Min below Range\':0,\'PD Min in Range\':1}"))
        self.lineEdit_8.setText(_translate("MainWindow", "1"))
        self.label_10.setText(_translate("MainWindow", "PD Skewness {\'Regular PD Skew\':1,\'Irregular PD Skew\':0}"))
        self.lineEdit_10.setText(_translate("MainWindow", "1"))
        self.label_11.setText(_translate("MainWindow", "PD Variance {\'Effective PD Variance\':1,\'Ineffective PD Variance\':0}"))
        self.lineEdit_11.setText(_translate("MainWindow", "1"))
        self.label_12.setText(_translate("MainWindow", "PD Median {\'Norma lPD Median\':1,\'Abnormal PD Median\':0}"))
        self.lineEdit_12.setText(_translate("MainWindow", "1"))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainView.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(773, 499)
        self.result_window_4 = QtWidgets.QTextEdit(Dialog)
        self.result_window_4.setGeometry(QtCore.QRect(100, 50, 151, 121))
        self.result_window_4.setObjectName("result_window_4")
        self.result_window_3 = QtWidgets.QTextEdit(Dialog)
        self.result_window_3.setGeometry(QtCore.QRect(610, 190, 151, 121))
        self.result_window_3.setObjectName("result_window_3")
        self.result_window_2 = QtWidgets.QTextEdit(Dialog)
        self.result_window_2.setGeometry(QtCore.QRect(360, 50, 151, 121))
        self.result_window_2.setObjectName("result_window_2")
        self.result_window_0 = QtWidgets.QTextEdit(Dialog)
        self.result_window_0.setGeometry(QtCore.QRect(100, 320, 151, 121))
        self.result_window_0.setObjectName("result_window_0")
        self.result_window_1 = QtWidgets.QTextEdit(Dialog)
        self.result_window_1.setGeometry(QtCore.QRect(310, 320, 151, 121))
        self.result_window_1.setObjectName("result_window_1")
        self.SendButton = QtWidgets.QPushButton(Dialog)
        self.SendButton.setGeometry(QtCore.QRect(630, 440, 75, 23))
        self.SendButton.setObjectName("SendButton")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(200, 280, 151, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(390, 280, 191, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(Dialog)
        self.line_3.setGeometry(QtCore.QRect(433, 210, 20, 81))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(Dialog)
        self.line_4.setGeometry(QtCore.QRect(200, 200, 221, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(Dialog)
        self.line_5.setGeometry(QtCore.QRect(470, 200, 118, 3))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(Dialog)
        self.line_6.setGeometry(QtCore.QRect(580, 170, 3, 61))
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(Dialog)
        self.line_7.setGeometry(QtCore.QRect(580, 270, 3, 61))
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(150, 260, 54, 12))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(350, 260, 54, 12))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(380, 220, 54, 12))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(500, 240, 54, 12))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(150, 230, 54, 12))
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(120, 200, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setCheckable(True)
        self.pushButton.toggle()

        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 280, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(400, 190, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(330, 280, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(560, 240, 51, 20))
        self.pushButton_5.setObjectName("pushButton_5")
        self.spinBox = QtWidgets.QSpinBox(Dialog)
        self.spinBox.setGeometry(QtCore.QRect(660, 400, 61, 22))
        self.spinBox.setObjectName("spinBox")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(580, 400, 181, 21))
        self.label_6.setObjectName("label_6")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.SendButton.setText(_translate("Dialog", "开始发送"))
        self.label.setText(_translate("Dialog", "0号路由器"))
        self.label_2.setText(_translate("Dialog", "1号路由器"))
        self.label_3.setText(_translate("Dialog", "2号路由器"))
        self.label_4.setText(_translate("Dialog", "3号路由器"))
        self.label_5.setText(_translate("Dialog", "4号路由器"))
        self.pushButton.setText(_translate("Dialog", "PushButton"))
        self.pushButton_2.setText(_translate("Dialog", "PushButton"))
        self.pushButton_3.setText(_translate("Dialog", "PushButton"))
        self.pushButton_4.setText(_translate("Dialog", "PushButton"))
        self.pushButton_5.setText(_translate("Dialog", "PushButton"))
        self.label_6.setText(_translate("Dialog", "发送间隔时间：          秒"))


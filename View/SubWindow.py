# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SubWindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_Sub(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(572, 407)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(250, 120, 54, 12))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(320, 30, 54, 12))
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 120, 54, 12))
        self.label.setObjectName("label")
        self.line_13 = QtWidgets.QFrame(Dialog)
        self.line_13.setGeometry(QtCore.QRect(340, 140, 141, 20))
        self.line_13.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_13.setObjectName("line_13")
        self.line_23_1 = QtWidgets.QFrame(Dialog)
        self.line_23_1.setGeometry(QtCore.QRect(330, 60, 151, 20))
        self.line_23_1.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_23_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_23_1.setObjectName("line_23_1")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(35, 40, 75, 23))
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("QPushButton{border-image:url(../images/router.png);}")
        self.pushButton.setFixedSize(50, 50)
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(240, 130, 75, 23))
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setStyleSheet("QPushButton{border-image:url(../images/router.png);}")
        self.pushButton_4.setFixedSize(50, 50)
        self.line_ = QtWidgets.QFrame(Dialog)
        self.line_.setGeometry(QtCore.QRect(470, 120, 20, 31))
        self.line_.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_.setObjectName("line_")
        self.line_01 = QtWidgets.QFrame(Dialog)
        self.line_01.setGeometry(QtCore.QRect(40, 140, 201, 20))
        self.line_01.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_01.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_01.setObjectName("line_01")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(50, 40, 54, 12))
        self.label_5.setObjectName("label_5")
        self.line_24 = QtWidgets.QFrame(Dialog)
        self.line_24.setGeometry(QtCore.QRect(40, 60, 291, 21))
        self.line_24.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_24.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_24.setObjectName("line_24")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(400, 100, 54, 12))
        self.label_4.setObjectName("label_4")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(455, 90, 71, 20))
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.setStyleSheet("QPushButton{border-image:url(../images/router.png);}")
        self.pushButton_5.setFixedSize(50, 50)
        self.line_23_2 = QtWidgets.QFrame(Dialog)
        self.line_23_2.setGeometry(QtCore.QRect(470, 70, 20, 31))
        self.line_23_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_23_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_23_2.setObjectName("line_23_2")
        self.line_3 = QtWidgets.QFrame(Dialog)
        self.line_3.setGeometry(QtCore.QRect(333, 60, 20, 91))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(35, 130, 75, 23))
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet("QPushButton{border-image:url(../images/router.png);}")
        self.pushButton_2.setFixedSize(50, 50)
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(320, 40, 75, 23))
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setStyleSheet("QPushButton{border-image:url(../images/router.png);}")
        self.pushButton_3.setFixedSize(50, 50)

        self.tableView_3 = QtWidgets.QTableView(Dialog)
        self.tableView_3.setGeometry(QtCore.QRect(10, 230, 141, 161))
        self.tableView_3.setObjectName("tableView_3")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(20, 10, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(40, 180, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.line_123 = QtWidgets.QFrame(Dialog)
        self.line_123.setGeometry(QtCore.QRect(290, 140, 51, 21))
        self.line_123.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_123.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_123.setObjectName("line_123")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(330, 180, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.tableView_0 = QtWidgets.QTableView(Dialog)
        self.tableView_0.setGeometry(QtCore.QRect(190, 230, 371, 161))
        self.tableView_0.setObjectName("tableView_0")
        self.line_123.raise_()
        self.line_24.raise_()
        self.line_3.raise_()
        self.line_01.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label.raise_()
        self.line_13.raise_()
        self.line_23_1.raise_()
        self.line_.raise_()
        self.label_5.raise_()
        self.label_4.raise_()
        self.line_23_2.raise_()
        self.tableView_3.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.pushButton_5.raise_()
        self.pushButton_4.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.label_8.raise_()
        self.tableView_0.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "1号路由器"))
        self.label_3.setText(_translate("Dialog", "2号路由器"))
        self.label.setText(_translate("Dialog", "0号路由器"))
        self.label_5.setText(_translate("Dialog", "4号路由器"))
        self.label_4.setText(_translate("Dialog", "3号路由器"))
        self.label_6.setText(_translate("Dialog", "最短路径树"))
        self.label_7.setText(_translate("Dialog", "路由表"))
        self.label_8.setText(_translate("Dialog", "结点关系表"))


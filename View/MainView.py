# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainView.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Ui_Dialog(object):
    TableList=[]
    ButtonList=[]
    EditList=[]
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(787, 501)
        self.SendButton = QtWidgets.QPushButton(Dialog)
        self.SendButton.setGeometry(QtCore.QRect(680, 440, 81, 41))
        self.SendButton.setObjectName("SendButton")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(90, 280, 221, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(350, 280, 191, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(Dialog)
        self.line_3.setGeometry(QtCore.QRect(393, 210, 20, 81))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(Dialog)
        self.line_4.setGeometry(QtCore.QRect(90, 200, 321, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(Dialog)
        self.line_5.setGeometry(QtCore.QRect(387, 200, 161, 20))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(Dialog)
        self.line_6.setGeometry(QtCore.QRect(540, 180, 3, 61))
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(Dialog)
        self.line_7.setGeometry(QtCore.QRect(540, 260, 3, 61))
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(80, 260, 54, 12))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(320, 251, 54, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(340, 220, 54, 12))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(460, 240, 54, 12))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(80, 230, 54, 12))
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(70, 180, 75, 23))
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("QPushButton{border-image:url(../images/router.png);}")
        self.pushButton.setFixedSize(50, 50)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(70, 260, 75, 23))
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet("QPushButton{border-image:url(../images/router.png);}")
        self.pushButton_2.setFixedSize(50, 50)
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(380, 180, 75, 23))
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setStyleSheet("QPushButton{border-image:url(../images/router.png);}")
        self.pushButton_3.setFixedSize(50, 50)
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(310, 260, 75, 23))
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setStyleSheet("QPushButton{border-image:url(../images/router.png);}")
        self.pushButton_4.setFixedSize(50, 50)
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(520, 230, 71, 20))
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.setStyleSheet("QPushButton{border-image:url(../images/router.png);}")
        self.pushButton_5.setFixedSize(50, 50)
        self.spinBox = QtWidgets.QSpinBox(Dialog)
        self.spinBox.setGeometry(QtCore.QRect(590, 390, 61, 22))
        self.spinBox.setMinimum(5)
        self.spinBox.setSingleStep(1)
        self.spinBox.setDisplayIntegerBase(10)
        self.spinBox.setObjectName("spinBox")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(510, 390, 181, 21))
        self.label_6.setObjectName("label_6")
        self.ModifyDistanceButton = QtWidgets.QPushButton(Dialog)
        self.ModifyDistanceButton.setGeometry(QtCore.QRect(550, 440, 81, 41))
        self.ModifyDistanceButton.setObjectName("pushButton_6")
        self.lineEdit_24 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_24.setGeometry(QtCore.QRect(240, 200, 31, 20))
        self.lineEdit_24.setObjectName("lineEdit_24")
        self.lineEdit_01 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_01.setGeometry(QtCore.QRect(210, 280, 31, 20))
        self.lineEdit_01.setObjectName("lineEdit_01")
        self.lineEdit_13 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_13.setGeometry(QtCore.QRect(450, 280, 31, 20))
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.lineEdit_23 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_23.setGeometry(QtCore.QRect(460, 200, 31, 20))
        self.lineEdit_23.setObjectName("lineEdit_23")
        self.lineEdit_12 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_12.setGeometry(QtCore.QRect(390, 240, 31, 20))
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.tableView_6 = QtWidgets.QTableView(Dialog)
        self.tableView_6.setEnabled(True)
        self.tableView_6.setGeometry(QtCore.QRect(30, 20, 181, 161))
        self.tableView_6.setObjectName("tableView_6")
        self.tableView_2 = QtWidgets.QTableView(Dialog)
        self.tableView_2.setGeometry(QtCore.QRect(310, 20, 181, 161))
        self.tableView_2.setObjectName("tableView_2")
        self.tableView_3 = QtWidgets.QTableView(Dialog)
        self.tableView_3.setGeometry(QtCore.QRect(600, 180, 181, 161))
        self.tableView_3.setObjectName("tableView_3")
        self.tableView_1 = QtWidgets.QTableView(Dialog)
        self.tableView_1.setGeometry(QtCore.QRect(250, 330, 181, 161))
        self.tableView_1.setObjectName("tableView_1")
        self.tableView_0 = QtWidgets.QTableView(Dialog)
        self.tableView_0.setGeometry(QtCore.QRect(30, 330, 181, 161))
        self.tableView_0.setObjectName("tableView_0")
        self.SetTimeButton = QtWidgets.QPushButton(Dialog)
        self.SetTimeButton.setGeometry(QtCore.QRect(690, 390, 75, 23))
        self.SetTimeButton.setObjectName("pushButton_8")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(570, 10, 171, 91))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(27)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(560, 110, 201, 16))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.SendButton.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.line_3.raise_()
        self.line_4.raise_()
        self.line_5.raise_()
        self.line_6.raise_()
        self.line_7.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.pushButton_3.raise_()
        self.pushButton_5.raise_()
        self.label_6.raise_()
        self.ModifyDistanceButton.raise_()
        self.lineEdit_24.raise_()
        self.lineEdit_01.raise_()
        self.lineEdit_13.raise_()
        self.lineEdit_23.raise_()
        self.lineEdit_12.raise_()
        self.tableView_6.raise_()
        self.tableView_2.raise_()
        self.tableView_3.raise_()
        self.tableView_1.raise_()
        self.tableView_0.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_4.raise_()
        self.SetTimeButton.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.spinBox.raise_()


        self.TableList.append(self.tableView_0)
        self.TableList.append(self.tableView_1)
        self.TableList.append(self.tableView_2)
        self.TableList.append(self.tableView_3)
        self.TableList.append(self.tableView_6)
        for i in range(5):
            self.TableList[i].horizontalHeader().setStretchLastSection(True)
            self.TableList[i].horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            self.TableList[i].setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.ButtonList.append(self.pushButton_2)
        self.ButtonList.append(self.pushButton_4)
        self.ButtonList.append(self.pushButton_3)
        self.ButtonList.append(self.pushButton_5)
        self.ButtonList.append(self.pushButton)

        self.EditList.append(self.lineEdit_01)
        self.EditList.append(self.lineEdit_12)
        self.EditList.append(self.lineEdit_23)
        self.EditList.append(self.lineEdit_13)
        self.EditList.append(self.lineEdit_24)
        reg = QRegExp("[0-9]+|inf|INF$")#设置每个空中只能填数字或者inf INF
        pValidator = QRegExpValidator(self)
        pValidator.setRegExp(reg)
        for i in range(len(self.EditList)):
            self.EditList[i].setValidator(pValidator)
            self.EditList[i].setText("100")


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
        self.label_6.setText(_translate("Dialog", "发送间隔时间：          秒"))
        self.ModifyDistanceButton.setText(_translate("Dialog", "修改距离"))
        self.SetTimeButton.setText(_translate("Dialog", "设定"))
        self.label_7.setText(_translate("Dialog", "模拟 OSPF"))
        self.label_8.setText(_translate("Dialog", "161630229  王山岳"))



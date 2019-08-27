# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(711, 600)
        self.columnView = QtWidgets.QColumnView(MainWindow)
        self.columnView.setGeometry(QtCore.QRect(0, 110, 181, 491))
        self.columnView.setObjectName("columnView")
        self.normal = QtWidgets.QPushButton(MainWindow)
        self.normal.setGeometry(QtCore.QRect(30, 150, 111, 31))
        self.normal.setObjectName("normal")
        self.trash = QtWidgets.QPushButton(MainWindow)
        self.trash.setGeometry(QtCore.QRect(30, 200, 111, 31))
        self.trash.setObjectName("trash")
        self.listView = QtWidgets.QListView(MainWindow)
        self.listView.setGeometry(QtCore.QRect(0, 0, 711, 111))
        self.listView.setObjectName("listView")
        self.listView_2 = QtWidgets.QListView(MainWindow)
        self.listView_2.setGeometry(QtCore.QRect(180, 110, 531, 491))
        self.listView_2.setObjectName("listView_2")
        self.mailList = QtWidgets.QListWidget(MainWindow)
        self.mailList.setGeometry(QtCore.QRect(180, 110, 531, 411))
        self.mailList.setObjectName("mailList")
        self.logout = QtWidgets.QPushButton(MainWindow)
        self.logout.setGeometry(QtCore.QRect(600, 40, 71, 31))
        self.logout.setObjectName("logout")
        self.username = QtWidgets.QLabel(MainWindow)
        self.username.setGeometry(QtCore.QRect(30, 40, 271, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.username.setFont(font)
        self.username.setObjectName("username")
        self.checkmail = QtWidgets.QPushButton(MainWindow)
        self.checkmail.setGeometry(QtCore.QRect(430, 540, 81, 31))
        self.checkmail.setObjectName("checkmail")
        self.blacklist = QtWidgets.QLineEdit(MainWindow)
        self.blacklist.setGeometry(QtCore.QRect(10, 320, 113, 20))
        self.blacklist.setObjectName("blacklist")
        self.whitelist = QtWidgets.QLineEdit(MainWindow)
        self.whitelist.setGeometry(QtCore.QRect(10, 350, 113, 20))
        self.whitelist.setObjectName("whitelist")
        self.blackconfirm = QtWidgets.QPushButton(MainWindow)
        self.blackconfirm.setGeometry(QtCore.QRect(130, 320, 41, 21))
        self.blackconfirm.setObjectName("blackconfirm")
        self.whiteconfirm = QtWidgets.QPushButton(MainWindow)
        self.whiteconfirm.setGeometry(QtCore.QRect(130, 350, 41, 21))
        self.whiteconfirm.setObjectName("whiteconfirm")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.normal.setText(_translate("MainWindow", "收件箱"))
        self.trash.setText(_translate("MainWindow", "垃圾箱"))
        self.logout.setText(_translate("MainWindow", "退出"))
        self.username.setText(_translate("MainWindow", "用户名"))
        self.checkmail.setText(_translate("MainWindow", "查看"))
        self.blacklist.setPlaceholderText(_translate("MainWindow", "添加黑名单"))
        self.whitelist.setPlaceholderText(_translate("MainWindow", "添加白名单"))
        self.blackconfirm.setText(_translate("MainWindow", "确认"))
        self.whiteconfirm.setText(_translate("MainWindow", "确认"))

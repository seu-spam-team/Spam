# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'blackwhitelist.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_BlackWhiteList(object):
    def setupUi(self, BlackWhiteList):
        BlackWhiteList.setObjectName("BlackWhiteList")
        BlackWhiteList.resize(609, 401)
        BlackWhiteList.setWindowModality(QtCore.Qt.ApplicationModal)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(BlackWhiteList)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.blackwhitelist = QtWidgets.QListWidget(BlackWhiteList)
        self.blackwhitelist.setMinimumSize(QtCore.QSize(591, 347))
        self.blackwhitelist.setObjectName("blackwhitelist")
        self.verticalLayout_2.addWidget(self.blackwhitelist)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.deletebutton = QtWidgets.QPushButton(BlackWhiteList)
        self.deletebutton.setMinimumSize(QtCore.QSize(100, 28))
        self.deletebutton.setMaximumSize(QtCore.QSize(100, 28))
        self.deletebutton.setObjectName("deletebutton")
        self.verticalLayout.addWidget(self.deletebutton, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(BlackWhiteList)
        QtCore.QMetaObject.connectSlotsByName(BlackWhiteList)

    def retranslateUi(self, BlackWhiteList):
        _translate = QtCore.QCoreApplication.translate
        BlackWhiteList.setWindowTitle(_translate("BlackWhiteList", "BlackList"))
        self.deletebutton.setText(_translate("BlackWhiteList", "删除"))

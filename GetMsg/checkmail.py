# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'checkmail.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CheckMail(object):
    def setupUi(self, CheckMail):
        CheckMail.setObjectName("CheckMail")
        CheckMail.resize(898, 600)
        self.info = QtWidgets.QListView(CheckMail)
        self.info.setGeometry(QtCore.QRect(0, 0, 901, 81))
        self.info.setObjectName("info")
        self.sender = QtWidgets.QLabel(CheckMail)
        self.sender.setGeometry(QtCore.QRect(0, 0, 211, 31))
        self.sender.setObjectName("sender")
        self.subject = QtWidgets.QLabel(CheckMail)
        self.subject.setGeometry(QtCore.QRect(0, 50, 211, 31))
        self.subject.setObjectName("subject")
        self.displaymail = QtWidgets.QTextEdit(CheckMail)
        self.displaymail.setGeometry(QtCore.QRect(0, 80, 901, 521))
        self.displaymail.setObjectName("displaymail")

        self.retranslateUi(CheckMail)
        QtCore.QMetaObject.connectSlotsByName(CheckMail)

    def retranslateUi(self, CheckMail):
        _translate = QtCore.QCoreApplication.translate
        CheckMail.setWindowTitle(_translate("CheckMail", "CheckMail"))
        self.sender.setText(_translate("CheckMail", "发件人"))
        self.subject.setText(_translate("CheckMail", "主题"))

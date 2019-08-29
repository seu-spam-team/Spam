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
        CheckMail.resize(898, 594)
        self.verticalLayout = QtWidgets.QVBoxLayout(CheckMail)
        self.verticalLayout.setObjectName("verticalLayout")
        self.sender = QtWidgets.QLabel(CheckMail)
        self.sender.setMinimumSize(QtCore.QSize(880, 25))
        self.sender.setMaximumSize(QtCore.QSize(16777215, 25))
        self.sender.setObjectName("sender")
        self.verticalLayout.addWidget(self.sender)
        self.subject = QtWidgets.QLabel(CheckMail)
        self.subject.setMinimumSize(QtCore.QSize(880, 25))
        self.subject.setMaximumSize(QtCore.QSize(16777215, 25))
        self.subject.setObjectName("subject")
        self.verticalLayout.addWidget(self.subject)
        self.displaymail = QtWidgets.QTextEdit(CheckMail)
        self.displaymail.setEnabled(False)
        self.displaymail.setMinimumSize(QtCore.QSize(880, 514))
        self.displaymail.setObjectName("displaymail")
        self.verticalLayout.addWidget(self.displaymail)

        self.retranslateUi(CheckMail)
        QtCore.QMetaObject.connectSlotsByName(CheckMail)

    def retranslateUi(self, CheckMail):
        _translate = QtCore.QCoreApplication.translate
        CheckMail.setWindowTitle(_translate("CheckMail", "CheckMail"))
        self.sender.setText(_translate("CheckMail", "发件人"))
        self.subject.setText(_translate("CheckMail", "主题"))

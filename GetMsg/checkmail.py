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
        CheckMail.setWindowModality(QtCore.Qt.ApplicationModal)
        CheckMail.resize(768, 526)
        self.verticalLayout = QtWidgets.QVBoxLayout(CheckMail)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(CheckMail)
        self.label.setMinimumSize(QtCore.QSize(50, 30))
        self.label.setMaximumSize(QtCore.QSize(50, 30))
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.senderName = QtWidgets.QLabel(CheckMail)
        self.senderName.setMinimumSize(QtCore.QSize(750, 30))
        self.senderName.setMaximumSize(QtCore.QSize(16777215, 30))
        self.senderName.setText("")
        self.senderName.setObjectName("senderName")
        self.horizontalLayout_2.addWidget(self.senderName)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(CheckMail)
        self.label_2.setMinimumSize(QtCore.QSize(50, 30))
        self.label_2.setMaximumSize(QtCore.QSize(50, 30))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.title = QtWidgets.QLabel(CheckMail)
        self.title.setMinimumSize(QtCore.QSize(750, 30))
        self.title.setMaximumSize(QtCore.QSize(16777215, 30))
        self.title.setText("")
        self.title.setObjectName("title")
        self.horizontalLayout_3.addWidget(self.title)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.content = QtWidgets.QTextBrowser(CheckMail)
        self.content.setEnabled(True)
        self.content.setMinimumSize(QtCore.QSize(750, 400))
        self.content.setObjectName("content")
        self.verticalLayout.addWidget(self.content)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.closebutton = QtWidgets.QPushButton(CheckMail)
        self.closebutton.setMinimumSize(QtCore.QSize(100, 28))
        self.closebutton.setMaximumSize(QtCore.QSize(100, 28))
        self.closebutton.setObjectName("closebutton")
        self.horizontalLayout.addWidget(self.closebutton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(CheckMail)
        QtCore.QMetaObject.connectSlotsByName(CheckMail)

    def retranslateUi(self, CheckMail):
        _translate = QtCore.QCoreApplication.translate
        CheckMail.setWindowTitle(_translate("CheckMail", "CheckMail"))
        self.label.setText(_translate("CheckMail", "发件人："))
        self.label_2.setText(_translate("CheckMail", "主题："))
        self.content.setHtml(_translate("CheckMail", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9.26733pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9.26733pt;\"><br /></p></body></html>"))
        self.closebutton.setText(_translate("CheckMail", "关闭"))

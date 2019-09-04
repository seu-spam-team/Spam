# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sendmail.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SendMail(object):
    def setupUi(self, SendMail):
        SendMail.setObjectName("SendMail")
        SendMail.resize(815, 553)
        SendMail.setWindowModality(QtCore.Qt.ApplicationModal)
        self.verticalLayout = QtWidgets.QVBoxLayout(SendMail)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(SendMail)
        self.label_2.setMinimumSize(QtCore.QSize(50, 30))
        self.label_2.setMaximumSize(QtCore.QSize(50, 30))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.receiver = QtWidgets.QLineEdit(SendMail)
        self.receiver.setMinimumSize(QtCore.QSize(728, 30))
        self.receiver.setMaximumSize(QtCore.QSize(16777215, 30))
        self.receiver.setObjectName("receiver")
        self.horizontalLayout_2.addWidget(self.receiver)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(SendMail)
        self.label.setMinimumSize(QtCore.QSize(50, 30))
        self.label.setMaximumSize(QtCore.QSize(50, 30))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.title = QtWidgets.QLineEdit(SendMail)
        self.title.setMinimumSize(QtCore.QSize(728, 30))
        self.title.setMaximumSize(QtCore.QSize(16777215, 30))
        self.title.setObjectName("title")
        self.horizontalLayout.addWidget(self.title)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(SendMail)
        self.label_3.setMinimumSize(QtCore.QSize(50, 30))
        self.label_3.setMaximumSize(QtCore.QSize(50, 30))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3, 0, QtCore.Qt.AlignTop)
        self.content = QtWidgets.QTextEdit(SendMail)
        self.content.setMinimumSize(QtCore.QSize(728, 404))
        self.content.setObjectName("content")
        self.horizontalLayout_3.addWidget(self.content)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.closewindow = QtWidgets.QPushButton(SendMail)
        self.closewindow.setMinimumSize(QtCore.QSize(100, 28))
        self.closewindow.setMaximumSize(QtCore.QSize(100, 28))
        self.closewindow.setObjectName("closewindow")
        self.horizontalLayout_4.addWidget(self.closewindow)
        self.saveAsDraft = QtWidgets.QPushButton(SendMail)
        self.saveAsDraft.setMinimumSize(QtCore.QSize(100, 28))
        self.saveAsDraft.setMaximumSize(QtCore.QSize(100, 28))
        self.saveAsDraft.setObjectName("saveAsDraft")
        self.horizontalLayout_4.addWidget(self.saveAsDraft)
        self.sendButton = QtWidgets.QPushButton(SendMail)
        self.sendButton.setMinimumSize(QtCore.QSize(100, 28))
        self.sendButton.setMaximumSize(QtCore.QSize(100, 28))
        self.sendButton.setObjectName("sendButton")
        self.horizontalLayout_4.addWidget(self.sendButton)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.retranslateUi(SendMail)
        QtCore.QMetaObject.connectSlotsByName(SendMail)

    def retranslateUi(self, SendMail):
        _translate = QtCore.QCoreApplication.translate
        SendMail.setWindowTitle(_translate("SendMail", "写信"))
        self.label_2.setText(_translate("SendMail", "收件人"))
        self.label.setText(_translate("SendMail", "主题"))
        self.label_3.setText(_translate("SendMail", "正文"))
        self.closewindow.setText(_translate("SendMail", "关闭"))
        self.saveAsDraft.setText(_translate("SendMail", "存草稿"))
        self.sendButton.setText(_translate("SendMail", "发送"))

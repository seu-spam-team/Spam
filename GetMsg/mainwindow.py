# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QCoreApplication
from mailusr import MailUser

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1091, 712)
        self.columnView = QtWidgets.QColumnView(Form)
        self.columnView.setGeometry(QtCore.QRect(0, 110, 201, 601))
        self.columnView.setObjectName("columnView")
        self.normal = QtWidgets.QPushButton(Form)
        self.normal.setGeometry(QtCore.QRect(30, 150, 141, 31))
        self.normal.setObjectName("normal")
        self.trash = QtWidgets.QPushButton(Form)
        self.trash.setGeometry(QtCore.QRect(30, 200, 141, 31))
        self.trash.setObjectName("trash")
        self.listView = QtWidgets.QListView(Form)
        self.listView.setGeometry(QtCore.QRect(0, 0, 1091, 111))
        self.listView.setObjectName("listView")
        self.listView_2 = QtWidgets.QListView(Form)
        self.listView_2.setGeometry(QtCore.QRect(200, 110, 891, 601))
        self.listView_2.setObjectName("listView_2")
        self.mailList = QtWidgets.QListWidget(Form)
        self.mailList.setGeometry(QtCore.QRect(200, 110, 891, 551))
        self.mailList.setObjectName("mailList")
        self.logout = QtWidgets.QPushButton(Form)
        self.logout.setGeometry(QtCore.QRect(980, 40, 71, 31))
        self.logout.setObjectName("logout")
        self.portrait = QtWidgets.QLabel(Form)
        self.portrait.setGeometry(QtCore.QRect(50, 20, 91, 81))
        self.portrait.setObjectName("portrait")
        self.username = QtWidgets.QLabel(Form)
        self.username.setGeometry(QtCore.QRect(130, 50, 271, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.username.setFont(font)
        self.username.setObjectName("username")
        self.checkmail = QtWidgets.QPushButton(Form)
        self.checkmail.setGeometry(QtCore.QRect(780, 670, 81, 31))
        self.checkmail.setObjectName("checkmail")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.normal.clicked.connect(self.clickNormal)
        self.trash.clicked.connect(self.clickTrash)
        self.logout.clicked.connect(self.logOut)
        self.setUserName("待定")

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.normal.setText(_translate("Form", "收件箱"))
        self.trash.setText(_translate("Form", "垃圾箱"))
        self.logout.setText(_translate("Form", "退出"))
        self.portrait.setText(_translate("Form", "头像"))
        self.username.setText(_translate("Form", "用户名"))
        self.checkmail.setText(_translate("Form", "查看"))

    def clickNormal(self):
        self.mailList.clear()
        normallist = ["normal mail1", "normal mail2", "normal mail3"]
        self.mailList.addItems(normallist)

    def clickTrash(self):
        self.mailList.clear()
        trashlist = ["trash mail1", "trash mail2", "trash mail3"]
        self.mailList.addItems(trashlist    )

    def setUserName(self,str):
        self.username.setText(str)

    def logOut(self):
        QCoreApplication.instance().quit()

    def showWidget(self):
        app = QtWidgets.QApplication(sys.argv)
        widget = QtWidgets.QWidget()
        ui = Ui_Form()
        ui.setupUi(widget)
        widget.show()
        sys.exit(app.exec_())

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'titlebar.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TitleBar(object):
    def setupUi(self, TitleBar):
        TitleBar.setObjectName("TitleBar")
        TitleBar.resize(975, 42)
        TitleBar.setMaximumSize(QtCore.QSize(16777215, 42))
        self.horizontalLayout = QtWidgets.QHBoxLayout(TitleBar)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.minimum = QtWidgets.QPushButton(TitleBar)
        self.minimum.setMinimumSize(QtCore.QSize(24, 24))
        self.minimum.setMaximumSize(QtCore.QSize(24, 24))
        self.minimum.setText("")
        self.minimum.setObjectName("minimum")
        self.horizontalLayout.addWidget(self.minimum)
        self.maximum = QtWidgets.QPushButton(TitleBar)
        self.maximum.setMinimumSize(QtCore.QSize(24, 24))
        self.maximum.setMaximumSize(QtCore.QSize(24, 24))
        self.maximum.setText("")
        self.maximum.setObjectName("maximum")
        self.horizontalLayout.addWidget(self.maximum)
        self.closewidget = QtWidgets.QPushButton(TitleBar)
        self.closewidget.setMinimumSize(QtCore.QSize(24, 24))
        self.closewidget.setMaximumSize(QtCore.QSize(24, 24))
        self.closewidget.setText("")
        self.closewidget.setObjectName("closewidget")
        self.horizontalLayout.addWidget(self.closewidget)

        self.retranslateUi(TitleBar)
        QtCore.QMetaObject.connectSlotsByName(TitleBar)

    def retranslateUi(self, TitleBar):
        _translate = QtCore.QCoreApplication.translate
        TitleBar.setWindowTitle(_translate("TitleBar", "TitleBar"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    a = Ui_TitleBar()
    a.show()
    sys.exit(app.exec_())

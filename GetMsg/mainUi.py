from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(498, 430)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 501, 431))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.txt_view = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("方正姚体")
        font.setPointSize(20)
        self.txt_view.setFont(font)
        self.txt_view.setObjectName("txt_view")
        self.verticalLayout.addWidget(self.txt_view)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        # 设置字体信息
        # 用于左侧选择栏的字体
        fontleft = QFont()
        # 字体
        fontleft.setFamily('微软雅黑')
        # 加粗
        fontleft.setBold(True)
        # 大小
        fontleft.setPointSize(15)
        fontleft.setWeight(75)


        self.setMinimumSize(300,300) # 设置窗口最小尺寸
        self.setMaximumSize(300,300) # 设置窗口最大尺寸



from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow, strl):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 300)
        MainWindow.setWindowOpacity(0.8)




        message = QLabel(MainWindow)
        message.setGeometry(QtCore.QRect(55, 85, 200, 100))

        pa = QPalette()
        pa.setColor(QPalette.WindowText,Qt.white)
        message.setPalette(pa)


        MainWindow.setStyleSheet("#MainWindow{border-image:url(timg.png);}")
        font = QtGui.QFont()
        font.setFamily("方正姚体")
        font.setPointSize(20)
        message.setFont(font)
        message.setStyleSheet("QComboBox{color:rgb(30,144,255)}")


        message.setText('收到一封邮件\n'+strl)


        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        # 设置关闭按钮
        self.closebtn = QPushButton('×', self)
        self.closebtn.setGeometry(260, 0, 40, 30)
        self.closebtn.setStyleSheet("QPushButton{color:black}"
                                    "QPushButton:hover{background-color:rgb(255, 0, 0)}"
                                    "QPushButton:hover{color:white}"
                                    "QPushButton{background-color:rgb(255, 255, 255)}"
                                    "QPushButton{border:none;}")
        self.closebtn.clicked.connect(self.close)

        self.setMinimumSize(300,300) # 设置窗口最小尺寸
        self.setMaximumSize(300,300) # 设置窗口最大尺寸



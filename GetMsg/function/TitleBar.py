from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import pyqtSignal, QPoint
from PyQt5.QtWidgets import QWidget

from titlebar.titlebar import Ui_TitleBar


class UI_TitleBar(QtWidgets.QWidget, Ui_TitleBar):

    # 窗口最小化信号
    windowMinimumed = pyqtSignal()
    # 窗口最大化信号
    windowMaximumed = pyqtSignal()
    # 窗口还原信号
    windowNormaled = pyqtSignal()
    # 窗口关闭信号
    windowClosed = pyqtSignal()
    # 窗口移动
    windowMoved = pyqtSignal(QPoint)

    def __init__(self):
        super(UI_TitleBar, self).__init__()
        self.setupUi(self)

    # def __init__(self):
    #     super(TitleBar, self).__init__()
    #     self.setMinimumSize(QtCore.QSize(0, 42))
    #     self.setMaximumSize(QtCore.QSize(16777215, 42))
    #     horizontalLayout = QtWidgets.QHBoxLayout(self)
    #     # self.horizontalLayout.setObjectName("horizontalLayout")
    #     spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
    #     horizontalLayout.addItem(spacerItem)
    #     self.minimum = QtWidgets.QPushButton()
    #     self.minimum.setMinimumSize(QtCore.QSize(24, 24))
    #     self.minimum.setMaximumSize(QtCore.QSize(24, 24))
    #     self.minimum.setText("")
    #     self.minimum.setObjectName("minimum")
    #     horizontalLayout.addWidget(self.minimum)
    #     self.maximum = QtWidgets.QPushButton()
    #     self.maximum.setMinimumSize(QtCore.QSize(24, 24))
    #     self.maximum.setMaximumSize(QtCore.QSize(24, 24))
    #     self.maximum.setText("")
    #     self.maximum.setObjectName("maximum")
    #     horizontalLayout.addWidget(self.maximum)
    #     self.closewidget = QtWidgets.QPushButton()
    #     self.closewidget.setMinimumSize(QtCore.QSize(24, 24))
    #     self.closewidget.setMaximumSize(QtCore.QSize(24, 24))
    #     self.closewidget.setText("")
    #     self.closewidget.setObjectName("closewidget")
    #     horizontalLayout.addWidget(self.closewidget)

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    a = UI_TitleBar()
    a.show()
    sys.exit(app.exec_())
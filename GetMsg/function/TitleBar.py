import qtawesome
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import pyqtSignal, QPoint, Qt
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QWidget

from titlebar import Ui_TitleBar


class UI_TitleBar(QtWidgets.QWidget, Ui_TitleBar):

    # 窗口最大化信号
    windowMaximumed = pyqtSignal()
    # 窗口还原信号
    windowNormaled = pyqtSignal()
    # 窗口移动信号
    windowMoved = pyqtSignal(QPoint)

    def __init__(self):
        super(UI_TitleBar, self).__init__()
        self.setupUi(self)
        self.maximum.setIcon(qtawesome.icon("fa5.window-maximize", color="black"))
        self.minimum.setIcon(qtawesome.icon("fa5.window-minimize", color="black"))
        self.closewidget.setIcon(qtawesome.icon("fa5.window-close", color="black"))
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setTransparency()
        self.mPos = None
        # 设置默认背景颜色,否则由于受到父窗口的影响导致透明
        # self.setAutoFillBackground(True)
        # palette = self.palette()
        # palette.setColor(palette.Window, QColor(85, 170, 255))
        # self.setPalette(palette)
        self.maxOrNormal = True

    def enterEvent(self, event):
        super(UI_TitleBar, self).enterEvent(event)
        self.setCursor(Qt.ArrowCursor)

    def mouseDoubleClickEvent(self, event):
        # super(UI_TitleBar, self).mouseDoubleClickEvent(event) #这句没注释掉之前双击放大缩小窗口老是出bug！！！
        self.showMaximizedOrNormal()

    def showMaximizedOrNormal(self):
        if self.maxOrNormal:
            self.windowMaximumed.emit()
        else:
            self.windowNormaled.emit()

    def mousePressEvent(self, event):
        """鼠标点击事件"""
        if event.button() == Qt.LeftButton:
            self.mPos = event.pos()
        event.accept()

    def mouseReleaseEvent(self, event):
        '''鼠标弹起事件'''
        self.mPos = None
        event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton and self.mPos:
            self.windowMoved.emit(self.mapToGlobal(event.pos() - self.mPos))
        event.accept()

    def setTransparency(self):
        minPalette = self.minimum.palette()
        minPalette.setColor(minPalette.Window, Qt.transparent)
        self.minimum.setPalette(minPalette)

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
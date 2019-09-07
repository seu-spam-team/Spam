import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QFileDialog
import sliding_window
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import time
import random


class MainCode(QMainWindow,sliding_window.Ui_MainWindow):
    def __init__(self,str):
        QMainWindow.__init__(self)
        sliding_window.Ui_MainWindow.__init__(self)
        self.setupUi(self,strl=str)
        self.setWindowFlags(Qt.FramelessWindowHint|Qt.Tool)
        #self.setAttribute(Qt.WA_TranslucentBackground)
        #|Qt.Tool

        self.desktop=QDesktopWidget() 
        self.move((self.desktop.availableGeometry().width()-self.width()),self.desktop.availableGeometry().height()) #初始化位置到右下角 
        self.showAnimation()


    def showAnimation(self): 
        #显示弹出框动画 
        self.animation=QPropertyAnimation(self) 
        self.animation.setTargetObject(self)
        self.animation.setPropertyName(b'pos')
        self.animation.setDuration(1000) 
        self.animation.setStartValue(QPoint(self.x(),self.y())) 
        self.animation.setEndValue(QPoint((self.desktop.availableGeometry().width()-self.width()),(self.desktop.availableGeometry().height()-self.height())))
        self.animation.start() 
          
        #设置弹出框1秒弹出，然后渐隐 
        self.remainTimer=QTimer() 
        self.remainTimer.timeout.connect(self.closeAnimation) 
        self.remainTimer.start(10000) #定时器10秒 
        #关闭动画 
    @pyqtSlot() 
    def closeAnimation(self): 
      #清除Timer和信号槽 
        self.remainTimer.stop() 
        self.remainTimer.timeout.disconnect(self.closeAnimation)
        self.remainTimer.deleteLater() 
        self.remainTimer=None
        #弹出框渐隐 
        self.animation =QPropertyAnimation(self) 
        self.animation.setTargetObject(self)
        self.animation.setPropertyName(b'windowOpacity')
        self.animation.setDuration(1000) 
        self.animation.setStartValue(1) 
        self.animation.setEndValue(0) 
        self.animation.start() 
        #动画完成后清理 
        self.animation.finished.connect(self.clearAll) 
      
    #清理及退出 
    @pyqtSlot() 
    def clearAll(self): 
        self.animation.finished.disconnect(self.clearAll)
        self.close()





        


# if __name__=='__main__':
#     app=QApplication(sys.argv)
#     md=MainCode('疑似垃圾邮件')
#     md.show()
#     sys.exit(app.exec_())
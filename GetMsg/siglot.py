# -*- coding: utf-8 -*-
#信号与槽（QTabWidget略）

from PyQt5.QtCore import QObject,pyqtSignal
from PyQt5.QtWidgets import  QMessageBox
from PyQt5 import QtWidgets

class SiganlObj(QObject):
     sendMsg=pyqtSignal(object) #定义信号

     def __init__(self):
         super(SiganlObj, self).__init__()
     def run(self,msg):
         self.sendMsg.emit(msg)#发射信号

class TypeSlot(QObject):#定义槽对象
     def __init__(self):
         super(TypeSlot, self).__init__()
     def get(self,msg):#定义槽函数
         print(">>",msg)
         if msg=='':
           QMessageBox.information(QtWidgets.QWidget(), "提醒", "收到一封新来信")
         elif msg=='垃圾':
           QMessageBox.information(QtWidgets.QWidget(), "提醒", "收到一封新来信,疑似为垃圾邮件")

if __name__=='__main__':
    send=SiganlObj()
    slot=TypeSlot()
    send.sendMsg.connect(slot.get)#绑定信号和槽函数
    send.run()#发信号
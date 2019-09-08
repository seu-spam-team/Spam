# -*- coding: utf-8 -*-
#信号与槽（QTabWidget略）

from PyQt5.QtCore import QObject,pyqtSignal
from PyQt5.QtWidgets import  QMessageBox
from PyQt5 import QtWidgets
from screen_tray import MainCode
class SiganlObj(QObject):
     sendMsg=pyqtSignal(object) #定义信号

     def __init__(self):
         super(SiganlObj, self).__init__()
     def run(self,msg):
         self.sendMsg.emit(msg)#发射信号

class TypeSlot(QObject):#定义槽对象
     def __init__(self,mainwindow,mailusr):
         super(TypeSlot, self).__init__()
         self.mailusr=mailusr
         self.mainwindow=mainwindow
     def get(self,msg):#定义槽函数
         print(">>",msg)
         if msg=='正常':
           #QMessageBox.information(QtWidgets.QWidget(), "提醒", "收到一封新来信")
           md = MainCode('',self.mailusr,self.mainwindow)
           md.show()
         elif msg=='垃圾':
           #QMessageBox.information(QtWidgets.QWidget(), "提醒", "收到一封新来信,疑似为垃圾邮件")
           md = MainCode('疑似垃圾邮件',self.mailusr,self.mainwindow)
           md.show()


if __name__=='__main__':
    # send=SiganlObj()
    # slot=TypeSlot()
    # send.sendMsg.connect(slot.get)#绑定信号和槽函数
    # send.run()#发信号
    t='sender:131315 sub: dasda \n text: neirong'
    import re

    str = "a123b"

    sender=(re.findall(r"sender:(.+?) sub", t))  #
    print(sender[0])



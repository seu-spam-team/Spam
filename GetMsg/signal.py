# coding=gbk
#�ź���ۣ�QTabWidget�ԣ�

from PyQt5.QtCore import QObject,pyqtSignal
from PyQt5.QtWidgets import  QMessageBox
from PyQt5 import QtWidgets
import sys
class SiganlObj(QObject):
     sendMsg=pyqtSignal(object) #�����ź�

     def __init__(self):
         super(SiganlObj, self).__init__()
     def run(self):
         self.sendMsg.emit('')#�����ź�

class TypeSlot(QObject):#����۶���
     def __init__(self):
         super(TypeSlot, self).__init__()
     def get(self,msg):#����ۺ���
         print(">>",msg)
         QMessageBox.information(QtWidgets.QWidget(), "����", "�յ�һ��������")

if __name__=='__main__':
    send=SiganlObj()
    slot=TypeSlot()
    send.sendMsg.connect(slot.get)#���źźͲۺ���
    send.run()#���ź�
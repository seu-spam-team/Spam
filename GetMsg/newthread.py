# coding=gbk
import threading
import time

class MyThread (threading.Thread):
    def __init__(self, mailusr,signal):
        threading.Thread.__init__(self)
        self.mailusr = mailusr
        self.signal = signal

    def run(self):
        print ("��ʼ�̣߳�" + self.name)
        self.mailusr.checknew(self.signal)
        print ("�˳��̣߳�" + self.name)




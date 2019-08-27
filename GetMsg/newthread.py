# coding=gbk
import threading
import time

class MyThread (threading.Thread):
    def __init__(self, mailusr,signal):
        threading.Thread.__init__(self)
        self.mailusr = mailusr
        self.signal = signal

    def run(self):
        print ("开始线程：" + self.name)
        self.mailusr.checknew(self.signal)
        print ("退出线程：" + self.name)




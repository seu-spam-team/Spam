# coding=gbk
import threading
import time

class MyThread (threading.Thread):
    def __init__(self, mailusr,signal,sock):
        threading.Thread.__init__(self)
        self.mailusr = mailusr
        self.signal = signal
        self.sock=sock
    def run(self):
        print ("开始线程：" + self.name)
        self.mailusr.checknew(self.signal,self.sock)
        print ("退出线程：" + self.name)




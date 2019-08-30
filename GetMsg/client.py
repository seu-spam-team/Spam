import socket
import time
import sys
import json
HOST = '10.203.191.162'
PORT = 8080
BUFIZ = 1024
ADDR = (HOST, PORT)

class Client:
    def __init__(self):
        self.cliSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.cliSock.connect(ADDR)

    def sendUsr(self, usr):
        t = 'a' + usr
        self.cliSock.send(bytes(t, encoding='utf-8'))
        time.sleep(0.2)
        self.cliSock.close()

    def sendmail(self, text,level=0.5):
        self.cliSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.cliSock.connect(ADDR)
        t = 'b' + text
        #print(t)
        self.cliSock.send(bytes(t, encoding='utf-8'))
        time.sleep(0.1)

    def sendfrom(self,usr,sender):
        self.cliSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.cliSock.connect(ADDR)
        t = 'g' + usr+' '+sender
        print(t)
        self.cliSock.send(bytes(t, encoding='utf-8'))
        time.sleep(0.1)

    def get_sender(self):
        msg = self.cliSock.recv(4096)
        t = str(msg, encoding='utf-8')
        print(t)
        self.cliSock.close()
        return t




    #发送添加黑名单请求
    def sendBlack(self, name):
        self.cliSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.cliSock.connect(ADDR)
        t = 'c' + name
        self.cliSock.send(bytes(t, encoding='utf-8'))
        time.sleep(0.2)
        self.cliSock.close()

    #发送添加白名单请求
    def sendWhite(self, name):
        self.cliSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.cliSock.connect(ADDR)
        t = 'd' + name
        self.cliSock.send(bytes(t, encoding='utf-8'))
        time.sleep(0.2)
        self.cliSock.close()

    def sendgetblack(self,usr):
        self.cliSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.cliSock.connect(ADDR)
        t = 'e'+usr
        self.cliSock.send(bytes(t, encoding='utf-8'))
        time.sleep(0.2)

    def sendgetwhite(self,usr):
        self.cliSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.cliSock.connect(ADDR)
        t = 'f'+usr
        self.cliSock.send(bytes(t, encoding='utf-8'))
        time.sleep(0.2)



    def getlist(self):
        msg = self.cliSock.recv(4096)
        if msg==b'':
            return []
        t = json.loads(msg.decode('utf-8'))
        print(t)
        self.cliSock.close()
        return t

    def getresult(self):

        msg = self.cliSock.recv(4096)
        t = str(msg,encoding='utf-8')
        print(t)
        self.cliSock.close()
        if t=='1':
            return True
        else:
            return False


    def close(self):
        self.cliSock.close()

if __name__ == "__main__":
        cli = Client()
        cli.sendBlack('haonan_0204@163.com hei')
        cli.sendWhite('hapnan_0204@163.com bai')
        cli.sendfrom('haonan_0204@163.com','....')
        cli.get_sender()
        cli.sendfrom('haonan_0204@163.com', 'bai')
        cli.get_sender()



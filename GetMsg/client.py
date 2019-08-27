import socket
import time
import sys

HOST = '10.0.0.6'
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



    def sendemail(self, text):
        t = 'b' + text
        self.cliSock.send(bytes(t, encoding='utf-8'))
        time.sleep(0.2)


    def sendBlack(self, name):
        t = 'c' + name
        self.cliSock.send(bytes(t, encoding='utf-8'))
        time.sleep(0.2)


    def sendWhite(self, name):
        t = 'd' + name
        self.cliSock.send(bytes(t, encoding='utf-8'))
        time.sleep(0.2)


    def getresult(self):
        msg = self.cliSock.recv(4096)
        t = str(msg, encoding='utf-8')
        print(t)
        return t

    def close(self):
        self.cliSock.close()

if __name__ == "__main__":
        cli = Client()
        cli.sendemail('mail')
        cli.getresult()
        cli.close()

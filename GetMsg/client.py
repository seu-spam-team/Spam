import socket
import time
import sys

HOST = '10.203.211.207'
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



    def sendBlack(self, name):
        self.cliSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.cliSock.connect(ADDR)
        t = 'c' + name
        self.cliSock.send(bytes(t, encoding='utf-8'))
        time.sleep(0.2)
        self.cliSock.close()


    def sendWhite(self, name):
        self.cliSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.cliSock.connect(ADDR)
        t = 'd' + name
        self.cliSock.send(bytes(t, encoding='utf-8'))
        time.sleep(0.2)
        self.cliSock.close()


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
        cli.sendUsr('usr')
        for i in range(0,3):
           cli.sendmail('Please call our customer service representative on FREEPHONE 0808 145 4742 between 9am-11pm as you have WON a guaranteed ?1000 cash or ?5000 prize!')

        cli.sendBlack('black')
        cli.sendWhite('white')
        cli.close()

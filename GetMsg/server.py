import classifier
from socket import *
import time
import sys
import os
import threading


class ServerDaemon:

	MAX_THREADS = 10
	CURRENT_THREADS = 0

	def __init__(self):
		print('Server started.')
		HOST = '139.219.132.178'
		PORT = 8080
		ADDR = (HOST,PORT)

		sockfd = socket(AF_INET,SOCK_STREAM)
		sockfd.bind(ADDR)
		sockfd.listen(ServerDaemon.MAX_THREADS)
		while True:
			if ServerDaemon.CURRENT_THREADS < ServerDaemon.MAX_THREADS:
				cliSockfd,addr = sockfd.accept()
				thread = ServerThread(cliSockfd)
				ServerDaemon.CURRENT_THREADS = ServerDaemon.CURRENT_THREADS + 1
				thread.start()



class ServerThread(threading.Thread):
	def __init__(self,socket1):
		threading.Thread.__init__(self)
		self.cliSockfd = socket1

	def run(self):
		try:
			while True:
				msg = str(self.cliSockfd.recv(4096),encoding='utf-8')
				if len(msg) <= 0:
					self.cliSockfd.close()
				elif msg[0] == 'a':#账户，创建检索table          a
					msg = msg[1:]
					print(msg)
					pass
				elif msg[0] == 'b':#正文分类     
					msg = msg[1:]
					if classifier.classify(msg):
						self.cliSockfd.send(bytes('1',encoding='utf-8'))
					else:
						self.cliSockfd.send(bytes('0',encoding='utf-8'))
					pass
				elif msg[0] == 'c':#黑名单                     b
					msg = msg[1:]
					user = msg.split(' ')[0]
					print(msg)
					pass
				elif msg[0] == 'd':#白名单                     b
					msg = msg[1:]
					user = msg.split(' ')[0]
					print(msg)
					pass
				else:
					print('无意义')
		except:
			#print('error')
			pass
		finally:
			self.cliSockfd.close()
			ServerDaemon.CURRENT_THREADS = ServerDaemon.CURRENT_THREADS - 1


a = ServerDaemon()


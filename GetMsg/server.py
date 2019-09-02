import classifier
from socket import *
import time
import sys
import os
import threading
import Database
import json

class ServerDaemon:

	MAX_THREADS = 10
	CURRENT_THREADS = 0

	def __init__(self):
		print('Server started.')
		HOST = '10.203.194.161'
		PORT = 8080
		ADDR = (HOST,PORT)
		Database.create()
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
					print(msg)
					if classifier.classify(msg):
						self.cliSockfd.send(bytes('1',encoding='utf-8'))
					else:
						self.cliSockfd.send(bytes('0',encoding='utf-8'))
					pass
				elif msg[0] == 'c':#黑名单                     b
					msg = msg[1:]
					user = msg.split(' ')[0]
					black=msg.split(' ')[1]
					Database.add_black(user,black)
					pass
				elif msg[0] == 'd':#白名单                     b
					msg = msg[1:]
					user = msg.split(' ')[0]
					white=msg.split(' ')[1]
					Database.add_white(user, white)
					pass
				elif msg[0]=='e':
					msg=msg[1:]
					list=Database.black_list(msg)
					js=json.dumps(list)
					self.cliSockfd.send(js.encode('utf-8'))
				elif msg[0]=='f':
					msg=msg[1:]
					list=Database.white_list(msg)
					js=json.dumps(list)
					self.cliSockfd.send(js.encode('utf-8'))
				elif msg[0]=='g':
					msg=msg[1:]
					print(msg)
					user = msg.split(' ')[0]
					sender = msg.split(' ')[1]
					print(user,sender)
					blacklist=Database.black_list(user)
					whitelist=Database.white_list(user)
					if sender in blacklist:
						self.cliSockfd.send(bytes('1', encoding='utf-8'))
					elif sender in whitelist:
						self.cliSockfd.send(bytes('2', encoding='utf-8'))
					else:
						self.cliSockfd.send(bytes('3', encoding='utf-8'))
				elif msg[0]=='h':#删除白名单
					msg=msg[1:]
					user = msg.split(' ')[0]
					listname = msg.split(' ')[1]
					print(user,listname)
					Database.delete_white(user,listname)
				elif msg[0]=='i':#删除黑名单
					msg = msg[1:]
					user = msg.split(' ')[0]
					listname = msg.split(' ')[1]
					print(user, listname)
					Database.delete_black(user, listname)
				else:
					print('无意义')
		except:
			#print('error')
			pass
		finally:
			self.cliSockfd.close()
			ServerDaemon.CURRENT_THREADS = ServerDaemon.CURRENT_THREADS - 1


a = ServerDaemon()


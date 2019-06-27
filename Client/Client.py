from socket import *
print('Input Host IP')
HOST = input()    #'172.31.1.144'
PORT = 54600
BUFSIZ = 1024
ADDR = (HOST,PORT)
tcpCliSock = socket(AF_INET,SOCK_STREAM)
tcpCliSock.connect(ADDR)
while True:
	data = input('>')
	if not data:
		break
	tcpCliSock.send(data.encode())
	data = tcpCliSock.recv(BUFSIZ)
	if not data:
		break
	print(data.decode('utf-8'))
tcpCliSock.close()


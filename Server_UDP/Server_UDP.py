from socket import *
from time import *

HOST = '127.0.0.2'
PORT = 54600
BUFSIZ = 1024
ADDR = (HOST,PORT)

udpSerSock = socket(AF_INET,SOCK_DGRAM)
udpSerSock.bind(ADDR)

while True:
	print('waitong for message...')
	data,addr = udpSerSock.recvfrom(BUFSIZ)
	data2 = ('['+ctime()+'] '+data.decode('utf-8')).encode()
	udpSerSock.sendto(data2,addr)
	print('..received from and returned to:',addr)
	
udpSerSock.Close()

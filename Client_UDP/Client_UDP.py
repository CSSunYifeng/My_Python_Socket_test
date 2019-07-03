from socket import *

print('HOSP IP:')
HOST = input()
print('HOSP PORT:')
PORT = int(input())
BUFSIZ = 1024
ADDR = (HOST,PORT)

udpCliSock = socket(AF_INET,SOCK_DGRAM)

while True:
	data = input('> ')
	if not data:
		break
	udpCliSock.sendto(data.encode(),(HOST,PORT))
	data, ADDR = udpCliSock.recvfrom(BUFSIZ)
	if not data:
		break
	print(data.decode('utf-8'))

udpCliSock.Close()

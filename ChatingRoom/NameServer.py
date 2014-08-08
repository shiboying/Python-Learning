from socket import *
HOST=''
PORT=21568
PORTSer=21567
IP='localhost'
BUFSIZ=1024
ADDR=(HOST,PORT)

tcpSerSock=socket(AF_INET,SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)
while True:
    print 'waiting for connection...'
    tcpCliSock, addr=tcpSerSock.accept()
    print '...connected from: ',addr
    tcpCliSock.send(IP)
    tcpCliSock.send('21567')
    tcpCliSock.close()
tcpSerSock.close()

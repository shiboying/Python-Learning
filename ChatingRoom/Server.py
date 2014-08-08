from socket import *
from time import ctime

HOST=''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)
filename='log.txt'

while True:
    print 'waiting for connection...'
    tcpCliSock, addr = tcpSerSock.accept()
    f=open(filename,'a')
    while True:
        Cdata=tcpCliSock.recv(BUFSIZ)
        if not Cdata:
            break
        print 'Client:' ,Cdata
        f.write('Client: %s\n' %(Cdata))
        Sdata=raw_input('Server: ')
        if not Sdata:
            break
        tcpCliSock.send('[%s] \n %s' %(ctime(),Sdata))
        f.write('Server: [%s] \n %s' %(ctime(),Sdata))
        f.write('\n')
    f.write('\n \n')
    f.close()
    tcpCliSock.close()
tcpSerSock.close()

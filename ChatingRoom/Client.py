from socket import *
from time import ctime
import string
HOST='localhost'
NAMESERVERPORT=21568
BUFSIZ=1024

ADDR=(HOST,NAMESERVERPORT)
tcpCliSock=socket(AF_INET,SOCK_STREAM)
tcpCliSock.connect(ADDR)

SIP=tcpCliSock.recv(BUFSIZ)
SPORT=int(tcpCliSock.recv(BUFSIZ))
SADDR=(SIP,SPORT)
tcpCliSock.close()
tcpCliSock2=socket(AF_INET,SOCK_STREAM)
tcpCliSock2.connect(SADDR)
while True:
    Cdata=raw_input('Client:')
    if not Cdata:
        break
    tcpCliSock2.send('[%s] \n %s' %(ctime(),Cdata))
    Sdata=tcpCliSock2.recv(BUFSIZ)
    if not Sdata:
        break
    print 'Server:' ,Sdata 
tcpCliSock2.close()

import socket
mysock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)#create a socket
#mysock.connect(('data.pr4e.org',80))#set the target of connect
mysock.connect(('localhost',9000))#set the target of connect, conect to local server that I created.
#cmd='GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n'.encode()
cmd='GET http://127.0.0.1/romeo.txt HTTP/1.0\r\n\r\n'.encode()
#cmd= Get url protocol  \r\n rturn newLine
mysock.send(cmd)
while True:
    data=mysock.recv(512)
    if len(data)<1:
        break
    print(data.decode(),end='')
mysock.close()

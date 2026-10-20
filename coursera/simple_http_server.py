from socket import *
def createServer():
    serversocket=socket(AF_INET,SOCK_STREAM)#create a socket
    try:
        serversocket.bind(('localhost',9000))# set the receiver
        serversocket.listen(5)
        while(1):#infinite loop that sits and wait for request
            (clientsocket,address)=serversocket.accept()#make the server a live to receive the request
            rd=clientsocket.recv(5000).decode()
            pieces=rd.split('\n')
            if(len(pieces)>0):print(pieces[0])
            data ="HTTP/1.1 200 OK \r\n"
            data +="Content-Type: text/html; charset=utf-8\r\n"
            data+="\r\n"
            data +='<html><body>Hello World</body></html>\r\n\r\n'
            clientsocket.sendall(data.encode())
            clientsocket.shutdown(SHUT_WR)
    except KeyboardInterrupt:
        print("\nshutting down...\n")
    except Exception as exc:
        print("Error:\n")
        print(exc)
    serversocket.close()
print('Access http://localhost:9000')
createServer()
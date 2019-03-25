import socket
##https://www.geeksforgeeks.org/socket-programming-multi-threading-python/           (( REFERENCE for socket programming))
from threading import Thread
##https://www.geeksforgeeks.org/multithreading-python-set-1/     (( REFERENCE for multi-threading))

class Clientsocket:
    def __init__(self,sock=None):
        if sock is None:
            self.sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        else:
            self.sock=sock
            
    def connect(self):
        ip='172.16.133.189' #it is the ip address of server
        port=input("SERVER PORT->") #it is the port of server
        self.sock.connect((ip,port))
        print "CONNECTED TO: " +str(ip)

    def client_send(self):
        while True:
            message=raw_input("ME-> ")
            self.sock.send(message)

    def client_recieve(self):
        while True:
            data=self.sock.recv(1024)
            print "CLIENT-> "+str(data)


if __name__=="__main__":
    c = Clientsocket()
    c.connect()
    t = Thread(target = c.client_send)
    r = Thread(target = c.client_recieve)
    t.start()
    r.start()

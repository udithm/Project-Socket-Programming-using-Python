import socket
#https://www.geeksforgeeks.org/socket-programming-multi-threading-python/
#https://www.geeksforgeeks.org/simple-chat-room-using-python/   (( REFERENCE for socket programming))
from thread import *
#https://www.geeksforgeeks.org/multithreading-python-set-1/     (( REFERENCE for multi-threading))
import logging
#https://youtu.be/-ARI4Cz-awo      ((REFERENCE for the information of logging ))
logging.basicConfig(filename='chat.log', level=logging.INFO, format='%(asctime)s: %(levelname)s: %(message)s')


class Serversocket:
    list_of_clients=[]
    def __init__(self,sock=None):
      if sock == None:
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      else:
        self.sock = sock

    def serverconnect(self):
        IP_address = '172.16.133.189'#IP_address is the ip address of server
        Port = input("PORT NUMBER ")# port number of Server
        self.sock.bind((IP_address, Port))
        self.sock.listen(2)
    def clientthread(self,conn, (ip,port)):

        conn.send("CONNECTED TO CHAT !")

        while True:
            try:
                message = conn.recv(2048)
                if message:
                    logging.info( "<" +str(ip)+str(port)+ "> " + message)
                    Serversocket.mysend(self,message,conn)
            except:
                continue
    def mysend(self,message, connection):
       for clients in Serversocket.list_of_clients:
         if clients!=connection:
            try:
                clients.send(message)
            except:
                clients.close()
    def serveraccept(self):
            while True:
               conn, addr = self.sock.accept()
               Serversocket.list_of_clients.append(conn)
               print "<"+str(addr[0])+str(addr[1])+">" + " CONNECTED"
               start_new_thread(self.clientthread,(conn,addr))

if __name__=="__main__":
    s= Serversocket()
    s.serverconnect()
    s.serveraccept()


conn.close()
server.close()

                  

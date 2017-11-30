import sys
import socket
class SocketConnection():
    def __init__(self):
        self.graphSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.graphIp='10.211.55.10'
        self.graphPort=8080
        self.graphSocket.connect((self.graphIp, self.graphPort))
        
    def sendMessage(self, message):
        self.graphSocket.send(message)
        mes=''
        try:
           mes=self.graphSocket.recv(64)
        except Exception as e :
            print(e)
        if mes:
             return mes
        else :
            return 'SendError'

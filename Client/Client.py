import socket
from threading import Thread
from queue import Queue
import random
def encoding(message):
    message = message.encode("utf-8")
    return message
def decoding(message):
    message = message.decode("utf-8")
    return message
class ClientChat:
    def __init__(self, host, port):
        host = socket.gethostbyname(socket.gethostname())
        port = random.randint(6000,10000)
        self.host = host
        self.port = port
        self.name = "Guest"
        self.messageQueue = Queue()
        self.server = (self.host, 1235)
    def createSocket(self):
        try:
            print(f"Creating chat client on host {self.host}, port {self.port}")
            self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.clientSocket.bind((self.host, self.port))
            print(f"Creating chat client on host {self.host}, port {self.port} sucessfully")
        except Exception as e:
            print(e)
            print(f"Creating chat client on host {self.host}, port {self.port} failed")
    def defineUser(self):
        name = input("Enter your name: ")
        if name != "":
            self.name = name
        self.clientSocket.sendto(encoding(self.name + "join the chat server"), self.server)
    def messageReciever(self):
        while True:
            try:
                message, address = self.clientSocket.recvfrom(1024)
                print(message)
                self.messageQueue.put((message, address))
            except: 
                pass
    def startThread(self):
        reciever = Thread(target= self.messageReciever)
        reciever.start()

    def run(self):
        while True:
            message = input()
            if (message == 'quit'):
                break
            if message =='':
                continue
            message = self.name +":" + message
            message = encoding(message)
            self.clientSocket.sendto(message,self.server)
        self.clientSocket.sendto(encoding('qqq'), server)
        self.clientSocket.close(
        os._exit(1)
        )
if __name__ == "__main__":
    host = input("Serverhost: ")
    port = input("serverport: ")
    client =  ClientChat(host, port)
    client.createSocket()
    client.defineUser()
    client.startThread()
    client.run()

import socket
from threading import Thread
from queue import Queue
def encoding(message):
    return message.encode("utf-8")
def decoding(message):
    return message.decode("utf-8")
class ServerChat:

    def __init__(self, host, port):
        self.host = host
        self.port = int(port)
        self.messageQueue = Queue()

    def createSocket(self):
        # khoi tao socket udp
        try:
            self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.serverSocket.bind((self.host, self.port))
            print("Create server socket successfull")
        except Exception as e:
            print(f"Coundnt create server socket on host {self.host}, port {self.port}")

    def messageReciever(self):
        while True:
            message, address = self.serverSocket.recvfrom(2048)
            self.messageQueue.put((message, address))
    def run(self):
        print(f"Running server on host {self.host}, port {self.port}")

        reciever = Thread(target= self.messageReciever)
        reciever.start()

        allAddress = set()

        while True:
            while not self.messageQueue.empty():
                message, currAddress = self.messageQueue.get()
                if currAddress not in allAddress:
                    allAddress.add(currAddress)
                message = decoding(message)
                if (message == "exit"):
                    allAddress.remove(currAddress)
                    continue
                print(str(currAddress) + message)
                for addr in allAddress:
                    if (addr == currAddress):
                        continue
                    message = encoding(message)
                    self.serverSocket.sendto(message, addr)

if __name__ == "__main__": 
    host = "10.1.4.104"
    port = int(1235)
    server = ServerChat(host, port)          
    server.createSocket()         
    server.run()
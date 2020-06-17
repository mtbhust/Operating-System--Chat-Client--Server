import socket
from threading import Thread
from queue import Queue
def encoding(message):
    return message.encode("utf-8")
def decoding(message):
    return message.decode("utf-8")
def extractName(message):
    index = message.find(':')
    name = message[:index]
    return name
def isPersonalMessage(message):
    header = message[:4]
    if header == "<pm>":
        return 1
    return 0

class ServerChat:

    def __init__(self, host, port):
        self.host = host
        self.port = int(port)
        self.messageQueue = Queue()
        self.listUser = {}
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
            try:
                message, address = self.serverSocket.recvfrom(2048)
                self.messageQueue.put((message, address))
            except:
                pass
        
    def run(self):
        print(f"Running server on host {self.host}, port {self.port}")

        reciever = Thread(target= self.messageReciever)
        reciever.start()

        # user = {}
        allAddress = set()

        while True:
            while not self.messageQueue.empty():
                message, currAddress = self.messageQueue.get()
                if currAddress not in allAddress:
                    allAddress.add(currAddress)
                message = decoding(message)
                name = extractName(message) # tu tin nhan gui den -> trich xuat ra ten
                self.listUser[name] = currAddress
                # exit signal chua dung
                if (message == "exit"):
                    allAddress.remove(currAddress)
                    del self.listUser[name]
                    continue
                #con dang o dang name : <pm><name> => can extract message
                if isPersonalMessage(message):
                    message = message[4:]
                    nameindex = [message.find('<'), message.find('>')]
                    name = message[nameindex[0]+1:nameindex[1]] #lay ten ra o trong message
                    address = self.listUser[name] # tim dia chi cua thang co ten trong dicttionary
                    try:
                        #can xu ly du lieu
                        self.serverSocket.sendto(message, address)                        
                    except:
                        allAddress.remove(address)
                        del self.listUser[name]
                else:
                    print(str(currAddress) + message)
                    message = encoding(message)
                    for addr in allAddress:
                        if (addr == currAddress):
                            continue
                        self.serverSocket.sendto(message, addr)
if __name__ == "__main__": 
    host = socket.gethostbyname(socket.gethostname())
    port = int(1235)
    server = ServerChat(host, port)          
    server.createSocket()         
    server.run()
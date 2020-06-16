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
                message, currAddress = self.messageQueue.get() #xu ly hang doi tin nhan, lay ra tin dau tien
                message = decoding(message) # tap tin gui ve la bytes, da duoc ma hoa (encode), nen can giai ma (decode) truoc khi tiep tuc
                if currAddress not in allAddress: #check co phai la nguoi dung moi hay khong
                    allAddress.add(currAddress) # neu nguoi dung moi -> them vao danh sach nguoi dang su dung
                    # name = ""    # xu ly ten de co the dung cho personal message
                    # for i in message:
                    #     if (i != ':'):
                    #         name += i
                    # print(name)               
                if (message == "exit"): # kiem tra thang clien co muon thoat khong
                    allAddress.remove(currAddress)
                    continue
                print(str(currAddress) + message) #in ra console server
                for addr in allAddress: # gui den tat ca thang con lai ngoai thang hien tai
                    if (addr == currAddress):
                        continue
                    message = encoding(message) #ma hoa tin nhan roi gui di
                    try:
                        self.serverSocket.sendto(message, addr) # gui tin nhawn den addr voi noi dung message
                    except:
                        allAddress.remove(addr)

if __name__ == "__main__": 
    host = socket.gethostbyname(socket.gethostname())
    port = int(1235)
    server = ServerChat(host, port)          
    server.createSocket()         
    server.run()
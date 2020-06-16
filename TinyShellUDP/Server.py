import socket

class ServerShell:
    def __init__(self, host, port, password):
        self.host = host
        self.port = int(port)
        self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clientSocket.bind((self.host, self.port))
        self.clientSocket.listen(1)
        self.password = password
    def isPassword(self, password):
        if password == self.password:
            return 1
        return 0

    def run(self):
        while True:
            connection, address = self.clientSocket.accept()
            while True:
                print(f'Get connection from {address}')
                data = connection.recv(9999)
                data.decode("utf-8")
                if (data[:8] == "password" and data[-8:] == "password"):
                    if self.isPassword(data[8:-8]):
                        connection.send("Successful".encode('utf-8'))
                    else:
                        connection.send("Failed".encode('utf-8'))
                        connection.close()
                else:
                    #processing data
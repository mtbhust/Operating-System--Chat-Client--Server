import socket

class ClientShell:
    def __init__(self, host, port, password):
        self.hostS = host
        self.portS = int(port)
        self.password = password
        self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    def checkConnection(self):
        try:
            self.clientSocket.connect((self.hostS, self.ports))
            password = self.password
            password = "password" + password+"password"
            password = password.encode('utf-8')
            self.clientSocket.send(password)
            res = self.clientSocket.recv(1024)
            res = res.decode('utf-8')
            return res
        except:
            return "Failed"
    def sendRequest(self, data):
        if self.checkConnection == "Failed":
            return "Failed"
        data = data.encode('utf-8')
        try:
            self.clientSocket.send(data)
        except:
            self.clientSocket.close()
            print("Connection is closed")
            return "Failed"
        return self.clientSocket.recv(9999).decode('utf-8')
        
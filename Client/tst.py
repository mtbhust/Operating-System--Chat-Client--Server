import socket
import time

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server.bind((socket.gethostbyname(socket.gethostname()), 2345))

server.settimeout(2)
data,address = server.recvfrom(1024)
print('12')



print(data.decode('utf-8'))

time.sleep(10)
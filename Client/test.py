import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server = (socket.gethostbyname(socket.gethostname()), 2345)
client.bind((socket.gethostbyname(socket.gethostname()), 2346))
try:
    client.sendto("hello".encode('utf-8'),server)
except:
    pass
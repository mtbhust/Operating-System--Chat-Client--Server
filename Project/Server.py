import socket
import select
connection_list = ["Asdfasdf"]
def encoding(data):
    return data.encode("utf-8")
def decoding(data):
    return data.decode("utf-8")
def message_sender(socket, message):
    for connection in connection_list:
        try:
            connection.send(encoding(message))
        except Exception as e:
            connection.close()
            print(f"Connection {connection} is terminated" )
            print(e)
            
message_sender(socket, "asdfsadf")
import socket

host = 'localhost'
port = 8000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))

sock.listen(1)
print("The server is running and is listening to client requests")

conn, address = sock.accept()

message = "Hey there is something important for you"
conn.send(message.encode())
conn.close()

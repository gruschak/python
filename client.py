import socket

my_str = ('Hello, world!'.encode())

sock = socket.socket()
sock.connect(('localhost', 9090))
sock.send(my_str)

data = sock.recv(1024)
sock.close()

print(data)

import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
service_addr = (socket.gethostname(), 9090)
serversocket.bind(service_addr)
serversocket.listen(1)

while True:
    clientsocket, clientaddr = serversocket.accept()
    print("accepted connection ", clientsocket, clientaddr)
    

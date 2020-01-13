import socket
from select import select

SRV_ADDR = ('127.0.0.1', 5050)
SRV_ADDR = ('127.0.0.1', 5051)
to_monitor = []

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(SRV_ADDR)
server_socket.listen()

def accept_connection(srv_socket):
    cl_socket, cl_addr = srv_socket.accept()
    print(cl_socket, " connected at ", cl_addr)
    to_monitor.append(cl_socket)

def talk_to_client(client_socket):
    request = client_socket.recv(4096)
    if request:
        client_socket.send("the Message from server\n".encode())
    else:
        # to_monitor.pop(client_socket) --- выдаст ошибку
        client_socket.close()

def event_loop():
    while True:
        ready_for_reading, _, _ = select(to_monitor, [], []) # read, write, error
        for sock in ready_for_reading:
            if sock is server_socket:
                accept_connection(sock)
            else: # sock is client_socket --- выдаст ошибку
                talk_to_client(sock)
            
to_monitor.append(server_socket)
event_loop()

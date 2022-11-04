"""
See also
https://docs.python.org/3.7/library/selectors.html
https://pymotw.com/3/selectors/
"""

import socket
import selectors

SRV_ADDR = ('127.0.0.1', 5050)
selector = selectors.DefaultSelector()


def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(SRV_ADDR)
    server_socket.listen()
    selector.register(fileobj=server_socket, events=selectors.EVENT_READ, data=accept_connection)

def accept_connection(srv_socket):
    cl_socket, cl_addr = srv_socket.accept()
    print("SERVER: Client socket fileno={} connected at {}".format(cl_socket.fileno(), cl_addr))
    selector.register(fileobj=cl_socket, events=selectors.EVENT_READ, data=talk_to_client)

def talk_to_client(client_socket):
    request = client_socket.recv(4096)
    if request:
        print("received from client: {}".format(request.decode()))
        response = request.decode().upper()
        client_socket.send(" -> sending {}\n\r".format(response).encode())
    else:
        selector.unregister(client_socket)
        client_socket.close()

def event_loop():
    while True:
        events = selector.select()  # (key, event)
        print("{0} {1}".format(events[0][0].fileobj, events[0][0].data))
        for key, _ in events:
            callback = key.data
            callback(key.fileobj)

server()
event_loop()

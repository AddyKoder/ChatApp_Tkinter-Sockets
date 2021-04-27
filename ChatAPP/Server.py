import socket
import threading

##################### VARIABLES ########################
IP = 0
ADDRESS = 0
server = 0
connections = []
PORT = 8080
PASSWORD = '1111'
encoding = 'utf-8'


###################### METHODS #########################

def start_sockets():
    start_server()
    threading.Thread(target=listen_connections).start()
    threading.Thread(target=send_message).start()


def send_message():
    while True:
        user_message = '___'.join(['SERVER', input()])
        for i in connections:
            i.send(user_message.encode(encoding))


def send_to_all(name, message, client):
    message = '___'.join([name, message])
    for i in connections:
        if i != client:
            i.send(message.encode(encoding))


def listen_connections():
    while True:
        conn, addr = server.accept()
        connections.append(conn)

        threading.Thread(target=handle_connection, args=(conn, addr)).start()


def handle_connection(client, address):
    connected = False

    name_pass = client.recv(1024).decode(encoding)
    try:
        name, password = name_pass.split('___')

    except:
        pass

    else:
        if password == PASSWORD:
            connected = True
            print(f'[CONNECTION] :  {name} joined')

    while connected:
        try:
            message = client.recv(1024).decode(encoding)
        except:

            print(f'[DISCONNECTED] :  {name} left')
            connections.remove(client)
            return 0

        if message != 'disconn' and message:
            print(f'[{name}] :  {message}')
            send_to_all(name, message, client)
        else:
            connected = False

    print(f'[DISCONNECTED] :  {name} left')
    client.send('You were disconnected by the server'.encode(encoding))
    connections.remove(client)


def start_server():
    global IP, ADDRESS, server

    IP = socket.gethostbyname(socket.gethostname())
    ADDRESS = (IP, PORT)

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDRESS)

    server.listen(4)


start_sockets()

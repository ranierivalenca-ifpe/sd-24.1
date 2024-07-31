# a simple server that listens for multiple clients and print their messages
# each client on a separate thread

import socket
import threading

# create a socket object
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket to a specific address and port
server.bind(('0.0.0.0', 1234))

# listen for incoming connections
server.listen()

# list of clients
clients = []

# function to handle clients
def pegar_nome(client):
    while True:
        try:
            # receive data from client
            message = client.recv(150).decode('utf-8')
            if not message:
                break
            print(message)
        except:
            # remove the client from the list
            clients.remove(client)
            client.close()
            break

# main loop
while True:
    print('waiting connection...')
    # accept incoming connection
    client, address = server.accept()
    print(f'Connected with {str(address)}')

    # add the client to the list
    clients.append(client)

    # create a thread for the client
    thread = threading.Thread(target=pegar_nome, args=(client,))
    thread.start()
    # handle_client(client)
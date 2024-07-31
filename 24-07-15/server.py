# create a simple echo server using tcp socket

import socket

# create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()
port = 9999

# bind to the port
server_socket.bind((host, port))

# queue up to 5 requests
server_socket.listen(5)

while True:
    # establish a connection
    client_socket, addr = server_socket.accept()
    print("Got a connection from %s" % str(addr))
    msg = 'Thank you for connecting' + "\r\n"
    client_socket.send(msg.encode('ascii'))
    client_socket.close()

    # close the connection
    server_socket.close()

# create a simple echo client using tcp socket that reads user input and sends it to the server

import socket

# create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()
port = 9999

# connection to hostname on the port
client_socket.connect((host, port))

# get user input and send it to the server
msg = input("Enter message to send to server: ")
client_socket.send(msg.encode('ascii'))

# receive data from the server
data = client_socket.recv(1024)
print("Received from server: %s" % data.decode('ascii'))

# close the connection
client_socket.close()

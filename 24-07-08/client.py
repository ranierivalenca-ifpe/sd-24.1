# a simple tcp echo client that reads data from the user and sends it to the server

import socket

def main():
    # create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect to the server
    s.connect(
        ("localhost", 9090) # the server's address also known as ENDPOINT TCP/IP
    )

    while True:
        # read data from the user
        data = input("Enter data: ")

        # send the data to the server
        s.send(data.encode())

        # receive the response from the server
        response = s.recv(1024)
        print("Received", response.decode())

    # close the connection
    s.close()

if __name__ == "__main__":
    main()
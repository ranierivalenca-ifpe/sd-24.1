# a simple tcp echo server

import socket

def main():
    # create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # bind the socket to a local address
    s.bind(("localhost", 9090))

    # listen for incoming connections
    s.listen(5)

    while True:
        # accept a connection
        c, addr = s.accept()
        print("Got connection from", addr)

        # read data from the connection
        while True:
            data = c.recv(6)
            print("Received", data)

            if data[0:4] == b"exit":
                break

            # send the data back to the client
            c.send(data)

        # close the connection
        c.close()
    
    # close the server socket
    s.close()

if __name__ == "__main__":
    main()
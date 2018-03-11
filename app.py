import socket

HOST = "127.0.0.1"
PORT = 9000

# By default, socket.socket creates TCP sockets.
with socket.socket() as server_sock:

    # reuse sockets that are in `TIME_WAIT` state
    server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_sock.bind((HOST, PORT))

    # number of pending connections, equal or more will be refused.
    server_sock.listen(0) # one connection at a time
    print("Listening on {}:{}...".format(HOST, PORT))
    RESPONSE = b"""HTTP/1.1 200 OK\r\nContent-type: text/html\r\nContent-length: 37\r\n\r\n<h1>Hello!</h1>\r\n<h2>I am working!</h2>"""



    while True:
        client_sock, client_addr = server_sock.accept() # waiting for connection
        print(f"New connection from {client_addr}.")
        with client_sock:
            client_sock.sendall(RESPONSE)
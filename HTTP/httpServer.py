import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# need to give the socket an IP and port number
host = 'localhost'
port = 10000

server.bind((host, port))

# will accept 5 requests
server.listen(5)

# now listening to requets coming into this port

# handle the incoming requests
while True: 
    # this accept returns a tuple, so we assing each one here in one statement
    connection, addr = server.accept() 

    msg = connection.recv(2000).decode()

    response = \
    "HTTP/1.1 200 OK\r\n" +\
    "Content-Type: text/html\r\n" +\
    "Content-Length: 13\r\n" +\
    "\r\n" +\
    "<h1>Hello World!</h1>"

    # this converts the binary stream to a string and prints it. 
    print(msg)

    #ack = 'Acknowledge reciept of: ' + msg
    # send an ack back
    connection.send(response.encode())

    connection.close()

    

    
    
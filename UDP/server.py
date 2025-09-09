# UDP_PingerServer.py
# We will need the following module to generate randomized lost packets
import random
from socket import *
import time

# Create a UDP socket
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Assign IP address and port number to socket
serverSocket.bind(('localhost', 12001))

while True:
# Receive the client packet along with the address it is coming from
    message, address = serverSocket.recvfrom(1024)
    print('message: ', message.decode(), address)
    # Generate random number in the range of 0 to 1
    rand = random.random()
    # If rand is less is than 4, we consider the packet lost and do not respond
    if rand > 0.7:
        print('rand is ', rand)
        print('message lost')
    else:
        time.sleep(rand/10) #sleep for rand/10 sec.
        # Otherwise, the server responds
        print('send response back')
        serverSocket.sendto(message, address)


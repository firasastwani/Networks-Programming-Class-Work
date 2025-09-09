from socket import *

client = socket(AF_INET, SOCK_STREAM)

host = 'localhost'
port = 10000

client.connect((host, port))

# takes the string and converts it into binary

msg = 'hello world'

client.send(msg.encode())

ack = client.recv(1024)

print('Recieved ', ack.decode())

client.close() 
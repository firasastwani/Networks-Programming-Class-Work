from socket import *

client = socket(AF_INET, SOCK_STREAM)

host = 'gaia.cs.umass.edu'
port = 80

client.connect((host, port))

# takes the string and converts it into binary

request = "GET /wireshark-labs/INTRO-wireshark-file1.html HTTP/1.1\r\n" +\
          "Host: gaia.cs.umass.edu\r\n" +\
          "Connection: close\r\n\r\n"

client.send(request.encode())


ack = client.recv(4096)
print('Recieved ', ack.decode())


client.close() 
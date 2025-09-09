from socket import *
import time

#  sets up a UDP socket, not TCP
client = socket(AF_INET, SOCK_DGRAM) 


host = 'localhost'
port = 12001 

# client waits 2 seconds, if no response it will throw an error
client.settimeout(2) 

# nunber of packets we will send
n = 10

#store the rtts
rtts = [] # init an empty list (an array list)



for i in range(n):    
    ta = time.time() # curr time in seconds

    msg = 'Ping: ' + str(i) + ' ' + str(ta)

    # udp send, no confirmating 
    client.sendto(msg.encode(), (host, port))

    try: 
        # waits for a reply for 2 seconds
        resp, addr = client.recvfrom(1024)

        tb = time.time()

        rtt = tb - ta 

        rtts.append(rtt)

        print('Took: ', rtt)
    except: 
        print("no response")


print("Num packets sent=", n)
print("Num packets recieved=", len(rtts))
print("Num pacets lost=", n - len(rtts))

print('Minimum=', min(rtts))
print('Maximum=', max(rtts))

avg = sum(rtts) / len(rtts)

print("Average rtt=", avg)










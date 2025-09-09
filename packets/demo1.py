#Demo0.py
#We are building a demo version of TCP reliable transfer protocol
#using a minimalistic simulation framework.
#We need to first import Node and Simulator

#Demo1.py
#The previous version implemented "Stop and Wait".
#Let's implement pipelining where a stream of packets can be transmitted
#sequentially.

#include these 3 lines, if you are having difficulty running it on
#VisualStudio Code debbugger
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from Node import *
from Simulator import Simulator
import random

#1. create nodes - generic class that can be treated as a FSM and be a part of the network
sender = Node('Sender', ['Ready', 'Wait'])
receiver = Node('Receiver', ['Wait'])
#2. connect them - bidirectional
sender.connect(receiver)
#3. create a simulator by passing the nodes we just created
simulator = Simulator([sender, receiver])

packets = []
for i in range(10):
    p = Packet(sender, receiver, [i, 'hello'])
    packets.append(p)

#4. We need to tell each Node what to do at each iteration inside the simulator
timer_intval = 5
sender.next = 0 #this points to the next packet to be transmitted.
def runSender(self):
    if self.current == 'Ready':
        if len(packets):
            packet = packets[self.next % len(packets)]
            self.next += 1
            print(self.name, 'sending...', packet)
            self.send(receiver, packet)
            #start a timer
            self.startTimer(timer_intval)

        self.current = 'Wait'
    elif self.current == 'Wait':
        if self.timeout:
            #timer ran out -- we need to resent the packet
            print(self.name, 're-sending...', packets[0])
            self.send(receiver, packets[0])
            #start a timer
            self.startTimer(timer_intval)
            
        #wait for an acknowledgement
        link = self.linkFrom(receiver)
        if not link.empty():
            ack = link.pop()
            print(self.name, 'receiving ack...', ack)
            #search for the acknowledged packet and remove it from the input buffer
            seqnum = ack.msg[0]
            for p in packets:
                if p.msg[0] == seqnum:
                    packets.remove(p)

            #packets.pop(0) #now being acknoledged, remove it
            self.stopTimer()

            if len(packets) == 0: #all the packets are sent. Finish the loop
                simulator.finish()
        self.current = 'Ready'

loss_prob = 0.2
received = [None] * 10 #initialied with 10 items
def runReceiver(self):
    link = self.linkFrom(sender)
    if not link.empty():
        packet = link.pop()
        if random.random() < loss_prob:
            print(self.name, 'Lost packet', packet)
        else:
            print(self.name, 'receiving...', packet)
            if random.random() < loss_prob:
                print(self.name, 'Lost acknowledgement')
            else:
                #send back an acknowledgement
                seqnum = packet.msg[0]
                ack = Packet(receiver, sender, [seqnum, 'Acknowledged'])
                self.send(sender, ack)
                #received.append(packet) #keep it in the received array
                received[seqnum] = packet
        
        
#5. give those methods to the Nodes
sender.setupFSM(runSender)
receiver.setupFSM(runReceiver)
#6. run the simulator
simulator.run()

#examin all the packets being received
for r in received:
    print(r)






















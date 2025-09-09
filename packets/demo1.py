#Demo0.py
#We are building a demo version of TCP reliable transfer protocol
#using a minimalistic simulation framework.
#We need to first import Node and Simulator

#Demo1.py
#The previous version implemented "Stop and Wait".
#Let's implement pipelining where a stream of packets can be transmitted
#sequentially.

#Demo2.py 
# will implement a sliding window

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
for i in range(30):
    p = Packet(sender, receiver, [i, 'hello'])
    packets.append(p)

#4. We need to tell each Node what to do at each iteration inside the simulator
timer_intval = 5

cwin = 10 # window size is set to 10
sender.base = 0
sender.next = 0 #this points to the next packet to be transmitted.
sender.numSend = 0
sender.numTimeouts = 0

def runSender(self):

    print(self.name, self.base, self.next, self.timerOn())

    if self.current == 'Ready':
        if self.next - self.base < cwin and self.next < len(packets):
            packet = packets[self.next]
            self.next += 1
            print(self.name, 'sending...', packet)
            self.numSend += 1
            self.send(receiver, packet)

            #start a timer, if not on

            if not self.timerOn():
                self.startTimer(timer_intval)

        self.current = 'Wait'
    elif self.current == 'Wait':
        link = self.linkFrom(receiver)
        if self.timeout:
            #timer ran out -- we need to resend the packet
            packet = packets[self.base] # send the oldest unacknowledged packet

            self.numTimeouts += 1

            print(self.name, 're-sending...', packet)
            self.numSend += 1
            self.send(receiver, packet)
            #restart a timer
            self.startTimer(timer_intval)
            self.timeout = False
        else:
            if not link.empty():
                ack = link.pop()
                print(self.name, 'receiving ack...', ack)
                # cumulative ACK index (first missing packet index at receiver)
                cack = ack.msg[0]
                if cack > self.base:
                    self.base = cack

                if self.base == self.next:
                    self.stopTimer()

                if self.base >= len(packets): # all packets sent and acknowledged
                    simulator.finish()

        self.current = 'Ready'

loss_prob = 0.2
received = []
def runReceiver(self):
    link = self.linkFrom(sender)
    if not link.empty():
        packet = link.pop()
        if random.random() < loss_prob:
            print(self.name, 'Lost packet', packet)
        else:
            print(self.name, 'receiving...', packet)
            seqnum = packet.msg[0]

            # ensure buffer can hold this sequence number
            if seqnum >= len(received):
                received.extend([None] * (seqnum - len(received) + 1))

            received[seqnum] = packet

            # compute cumulative ACK as first missing index
            if received.count(None):
                cack = received.index(None)
            else:
                cack = len(received)

            ack = Packet(receiver, sender, [cack, 'Acknowledged', seqnum])

            if random.random() < loss_prob:
                print(self.name, 'Lost acknowledgement')
            else:
                #send back an acknowledgement
                self.send(sender, ack)                
        

#5. give those methods to the Nodes
sender.setupFSM(runSender)
receiver.setupFSM(runReceiver)
#6. run the simulator
simulator.run()

#examin all the packets being received
print("\n=== SIMULATION RESULTS ===")
print("Packets received:")
for r in received:
    print(r)

print(f"\n=== STATISTICS ===")
print(f"Total packets sent: {sender.numSend}")
print(f"Total timeouts: {sender.numTimeouts}")
print(f"Number of packets: {len(packets)}")
print(f"Average sends per packet: {sender.numSend / len(packets):.2f}")
print(f"Timeout rate: {sender.numTimeouts / sender.numSend * 100:.1f}%")




















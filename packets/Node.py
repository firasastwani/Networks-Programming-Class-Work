from threading import Timer
import types

#This class implements an abstract data object transmitted from SRC to DEST
#with the payload of MSG.
class Packet:
    def __init__(self, src, dest, msg):
        self.src = src
        self.dest = dest;
        self.msg = msg
    def __str__(self):
        return ' '.join(['Pckt:', self.src.name, self.dest.name, str(self.msg)])

#This class implements an abstract communication chanell object, connecting
#SRC node to DEST node.
class Link:
    def __init__(self,src,dest):
        self.ibuffer = []
        self.src = src #src node
        self.dest = dest #destination node
    def empty(self):
        return len(self.ibuffer)==0
    def size(self):
        return len(self.ibuffer)
    def pop(self):
        if len(self.ibuffer) > 0:
            return self.ibuffer.pop(0)
        else:
            return None
    def __str__(self):
        return self.src.name + '-' + self.dest.name
    
#This class implements an abstract network node object. It can be a host,
#router, switch, etc. It is also a FSM (finite state machine).
class Node:
    #The constructor takes the name of the node, a set of states to be taken,
    #and the initial state.
    def __init__(self, name, state_names, init_state=None):
        self.name = name;
        self.states = state_names
        self.current = None; 
        for n in self.states:
            if n == init_state:
                self.current = n
        if not self.current:
            self.current = self.states[0]
        self.neighbors=[]
        self.links = {}
        self.handlers = {}
##        self.run = None
        self.timer = None
        self.timeout = False
        self.timerStarted = False
        
    def __str__(self):
        return self.name
    def run(self):
        print(self.name, 'no actions implemented.')
        
    #implements one-way connection
    def connect1(self,node):
        link = self.links.get(node)
        if link == None:
            link = Link(self, node)
            self.links[node]=link
##            print(f'{self.name}: adding link from {link.src} to {link.dest}')
    #implements two-way connection
    def connect(self,node):
        self.connect1(node)
        node.connect1(self)
        if self.neighbors.count(node)==0:
            self.neighbors.append(node)

    #returns the communcation channel from this node to NODE
    def linkTo(self, node):
        return self.links.get(node)
    #returns the communcation channel from NODE to this node
    def linkFrom(self, node):
        return node.links.get(self)

    #send a PACKET to its neighbor given in HOP
    def send(self,hop,packet):
        link = self.linkTo(hop)
        if link:
            link.ibuffer.append(packet)
        else:
            print(f'Error: {hop} not connected from {self}')
    #receive a PACKET from its neighbor
    def receive(self,nbr):
        packet = None
        link = self.linkFrom(nbr)
        if link:
            packet = link.pop()
        else:
            print(f'Error: {nbr} not connected to {self}')
            
        return packet

    #set its RUN method to the given function. RUN is called from the
    #Simulator in Simulator.py
    def setupFSM(self, runFunc): #bind the custom FSM function to run()
        self.run = types.MethodType(runFunc, self)

    #next set of methods implements a timer        
    def startTimer(self,interval):
        def _handler():
            self.timeout = True
            self.timerStarted = False
            
        if self.timerOn():
            self.timer.cancel()
        self.timeout = False
        self.timer = Timer(interval, _handler)
        self.timer.start()
        self.timerStarted = True
    def stopTimer(self):
        self.timer.cancel()
        self.timerStarted = False
    def timerOn(self):
        return self.timerStarted;
        



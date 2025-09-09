from Node import *
import time

class Simulator:
    def __init__(self, nodes, end_cond=None, sleep_time=1):
        self.nodes = nodes
        self.done = False
        self.step = 0
        self.end_cond = end_cond
        self.sleep_time = sleep_time
    #call this to end the simulation
    def finish(self):
        self.done = True
    #return the current simulation time step
    def getStep(self):
        return self.step
    #the main simulation loop
    def run(self):
        self.step=1
        while not self.done:
            print("Step: ", self.step)
            self.step += 1

            for node in self.nodes:
                node.run()
                
            time.sleep(self.sleep_time)
            if self.end_cond and self.end_cond() == True:
                self.finish()

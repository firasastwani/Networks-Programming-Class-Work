import math
import scipy

class LossModel:
    #evaluate the network capacity at time t
    def eval(self, t): 
        return 0
    #evaluate the probability of timeout at time t at the send rate
    def timeout_prob(self, t, rate):
        return 1
    #evaluate the probability of duplicate acknowledgement at time t at the send rate
    def dupacks_prob(self, t, rate):
        return 1

class ConstModel(LossModel):
    def __init__(self, A, sgms):
        self.A = A
        self.sigmas = sgms
    def eval(self, t):
        return self.A 
    def timeout_prob(self, t, rate):
        mu = self.eval(t)
        s = (rate - mu) / self.sigmas[0]
        p = scipy.stats.norm.cdf(s)
        return p
    def dupacks_prob(self, t, rate):
        mu = self.eval(t)
        s = (rate - mu) / self.sigmas[1]
        p = scipy.stats.norm.cdf(s)
        return p

class SineModel(LossModel):
    def __init__(self, A, omega, phase, offset, sgms):
        self.A = A
        self.omega = omega
        self.phase = phase
        self.offset = offset
        self.sigmas = sgms
    def eval(self, t):
        return self.A * math.sin(self.omega*(t - self.phase)) + self.offset
    def timeout_prob(self, t, rate):
        mu = self.eval(t)
        s = (rate - mu) / self.sigmas[0]
        p = scipy.stats.norm.cdf(s)
        return p
    def dupacks_prob(self, t, rate):
        mu = self.eval(t)
        s = (rate - mu) / self.sigmas[1]
        p = scipy.stats.norm.cdf(s)
        return p


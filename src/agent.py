import numpy as np 
import torch 
import torch.nn as nn 
from torch.optim import Adam 

from networks import MLP




class Agent(object):
    def __init__(self, **kwargs):
        self.encoder = MLP()
        self.decoder = MLP()
        self.optimizer = Adam()

    def act(self, obs):
        pass 
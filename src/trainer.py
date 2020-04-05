from agent import Agent 




class Trainer(object):
    def __init__(self, agent_configs, **kwargs):
        self.n_agents = len(agent_configs)
        self.agent_configs = agent_configs
        self.agents = [Agent(**a_cfg) for a_cfg in agent_configs]

    def step(self, obs_n):
        pass 
        
    def train(self, samples):
        pass 

    def save(self):
        pass 

    def load(self):
        pass 
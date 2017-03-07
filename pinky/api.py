from . import src
import numpy as np

class distribution(object):
    def __init__(self, P=None, **kwargs):
        self.P = None
        self.extent = kwargs.get('extent', np.array([0, 1, 0, 1]))
        self.bins = kwargs.get('bins', (100,100))

    def Gaussian(self, **kwargs):
        src.distributions._gaussian.dist(self, **kwargs)

    def sample(self, n_samples=1, **kwargs):
        if self.P is None:
            raise AttributeError('''
            Probability distribution not defined.''')
        return src._generate.sample(self.P, n_samples, extent=self.extent, **kwargs)

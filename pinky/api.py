from . import stats
import numpy as np

class Pinky(object):
    def __init__(self, P=None, **kwargs):
        self.P = P
        self.extent = kwargs.get('extent', np.array([-1, 1, -1, 1]))
        self.bins = kwargs.get('bins', 100)

    def Gaussian(self, **kwargs):
        stats.functions._gaussian.dist(self, **kwargs)

    def sample(self, n_samples=1, **kwargs):
        if self.P is None:
            raise AttributeError('''
            Probability distribution not defined.''')
        return stats.sample(self.P, n_samples, extent=self.extent, **kwargs)

import numpy as np

class DTPytorchWrapper():
    def __init__(self, shape=(120, 160, 3), normalize=True):
        self.shape = shape
        self.normalize = True

    def preprocess(self, obs):
        if self.normalize:
            obs *= 255.0/obs.max()

        from scipy.misc import imresize
        return imresize(obs, self.shape)
import numpy as np
from scipy.ndimage import zoom

class DTPytorchWrapper():
    def __init__(self, shape=(120, 160, 3)):
        self.shape = shape
        self.transposed_shape = (shape[2], shape[0], shape[1])

    def preprocess(self, obs):
        return zoom(obs, self.shape).transpose(2, 0, 1)

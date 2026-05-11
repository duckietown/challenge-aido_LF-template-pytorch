"""Observation preprocessing for the PyTorch template."""

import cv2
import numpy as np


class DTPytorchWrapper:
    """Resize and channel-reorder observations for PyTorch policies."""

    _transposed_shape: tuple[int, int, int]
    shape: tuple[int, int, int]

    def __init__(self, shape: tuple[int, int, int] = (64, 64, 3)) -> None:
        """Store the target image shape used by the policy."""
        self.shape = shape
        self._transposed_shape = (shape[2], shape[0], shape[1])

    def preprocess(self, observation: np.ndarray) -> np.ndarray:
        """Resize an observation and convert it to CHW RGB format."""
        resize_shape = self.shape[0:2]
        resized_observation = cv2.resize(observation, resize_shape)
        # NOTICE: OpenCV changes the order of the channels !!!
        rgb_observation = cv2.cvtColor(resized_observation, cv2.COLOR_BGR2RGB)
        return rgb_observation.transpose(2, 0, 1)

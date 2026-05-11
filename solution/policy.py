"""Placeholder policy used by the PyTorch template."""

import numpy as np


class TemplatePolicy:
    """Return a stationary action.

    Users are expected to replace this template logic.
    """

    def predict(self, observation: np.ndarray) -> np.ndarray:
        """Return a stationary action for the provided observation."""
        del observation
        return np.zeros(2, dtype=np.float32)

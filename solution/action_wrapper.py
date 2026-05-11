"""Action conversion helpers for the PyTorch template."""

from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class _ActionParameters:
    gain: float = 1
    limit: float = 1
    motor_constant: float = 27
    radius: float = 0.0318
    speed_gain: float = 0.8
    trim: float = 0
    wheel_dist: float = 0.102


_DEFAULT_ACTION_PARAMETERS = _ActionParameters()


class DTPytorchActionWrapper:
    """Convert [velocity, steering] actions to wheel PWM values."""

    _gain: float
    _limit: float
    _motor_constant: float
    _radius: float
    _speed_gain: float
    _trim: float
    _wheel_dist: float

    def __init__(self, parameters: _ActionParameters | None = None) -> None:
        """Store the wheel-geometry and motor scaling parameters."""
        action_parameters = parameters or _DEFAULT_ACTION_PARAMETERS
        self._gain = action_parameters.gain
        self._limit = action_parameters.limit
        self._motor_constant = action_parameters.motor_constant
        self._radius = action_parameters.radius
        self._speed_gain = action_parameters.speed_gain
        self._trim = action_parameters.trim
        self._wheel_dist = action_parameters.wheel_dist

    def convert(self, action: np.ndarray) -> np.ndarray:
        """Convert one action into left/right wheel PWM values."""
        normalized_action = np.asarray(action, dtype=float)
        velocity = normalized_action[0]
        steering = normalized_action[1]
        velocity *= self._speed_gain

        right_gain_inverse = (self._gain + self._trim) / self._motor_constant
        left_gain_inverse = (self._gain - self._trim) / self._motor_constant

        omega_right = (
            velocity + 0.5 * steering * self._wheel_dist
        ) / self._radius
        omega_left = (
            velocity - 0.5 * steering * self._wheel_dist
        ) / self._radius

        pwm_right = np.clip(
            omega_right * right_gain_inverse,
            -self._limit,
            self._limit,
        )
        pwm_left = np.clip(
            omega_left * left_gain_inverse,
            -self._limit,
            self._limit,
        )
        return np.array([pwm_left, pwm_right], dtype=float)

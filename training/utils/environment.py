"""Helpers for constructing learning environments."""

import gymnasium as gym
from gym_duckiematrix.db21j_env import DuckiematrixDB21JEnv
from gymnasium import Env

ENTITY_NAME = "map_0/vehicle_0"
OUT_OF_ROAD_PENALTY = -1000


def launch_environment(environment_id: str | None = None) -> Env:
    """Launch the default learning environment."""
    if environment_id:
        return gym.make(environment_id)
    return DuckiematrixDB21JEnv(
        entity_name=ENTITY_NAME,
        out_of_road_penalty=OUT_OF_ROAD_PENALTY,
    )

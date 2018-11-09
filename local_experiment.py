#!/usr/bin/env python
import torch
import traceback

import gym
import numpy as np

# noinspection PyUnresolvedReferences
import gym_duckietown_agent  # DO NOT CHANGE THIS IMPORT (the environments are defined here)
from duckietown_challenges import wrap_solution, ChallengeSolution, ChallengeInterfaceSolution, InvalidEnvironment
from wrappers import SteeringToWheelVelWrapper

from env import launch_env


def launch_local_experiment(environment):
    # Use our launcher
    env = launch_env(environment)

    # === BEGIN SUBMISSION ===

    # If you created custom wrappers, you also need to copy them into this folder.

    from wrappers import NormalizeWrapper, ImgWrapper, ActionWrapper, ResizeWrapper

    env = ResizeWrapper(env)
    env = NormalizeWrapper(env)
    # to make the images pytorch-conv-compatible
    env = ImgWrapper(env)
    env = ActionWrapper(env)

    # you ONLY need this wrapper if you trained your policy on [speed,steering angle]
    # instead [left speed, right speed]
    # env = SteeringToWheelVelWrapper(env)

    # you have to make sure that you're wrapping at least the actions
    # and observations in the same as during training so that your model
    # receives the same kind of input, because that's what it's trained for
    # (for example if your model is trained on grayscale images and here
    # you _don't_ make it grayscale too, then your model wont work)

    # HERE YOU NEED TO CREATE THE POLICY NETWORK SAME AS YOU DID IN THE TRAINING CODE
    # if you aren't using the DDPG baseline code, then make sure to copy your model
    # into the model.py file and that it has a model.predict(state) method.
    from model import DDPG

    model = DDPG(state_dim=env.observation_space.shape, action_dim=2, max_action=1, net_type="cnn")

    model.load("model", "models", for_inference=True)

    # === END SUBMISSION ===

    # deactivate the automatic differentiation (i.e. the autograd engine, for calculating gradients)
    with torch.no_grad():
        observation = env.reset()

        # While there are no signal of completion (simulation done)
        # we run the predictions for a number of episodes, don't worry, we have the control on this part
        while True:
            # we passe the observation to our model, and we get an action in return
            action = model.predict(observation)
            # we tell the environment to perform this action and we get some info back in OpenAI Gym style
            observation, reward, done, info = env.step(action)
            # here you may want to compute some stats, like how much reward are you getting
            # notice, this reward may no be associated with the challenge score.

            # it is important to check for this flag, the Evalution Engine will let us know when should we finish
            # if we are not careful with this the Evaluation Engine will kill our container and we will get no score
            # from this submission
            if done:
                env.reset()


if __name__ == '__main__':
    print('Starting submission')
    launch_local_experiment(environment=None)

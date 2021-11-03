#!/bin/bash

set -ex

# install PyTorch
pip3 install torch==1.7.1
pip3 install torchvision==0.8.1

# clean
pip3 uninstall -y dataclasses

#!/bin/bash

set -ex

# install PyTorch and Torchvision (versions are defined in the base image's Dockerfile)
pip3 install torch==${PYTORCH_VERSION}
pip3 install torchvision==${TORCHVISION_VERSION}

# clean
pip3 uninstall -y dataclasses

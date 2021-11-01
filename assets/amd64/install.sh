#!/bin/bash

set -ex

# install PyTorch
pip3 install torch==1.7.1

# clean
pip3 uninstall -y dataclasses

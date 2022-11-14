# Definition of Submission container
ARG DOCKER_REGISTRY=docker.io
ARG ARCH=amd64
ARG MAJOR=daffy
ARG BASE_TAG=${MAJOR}

FROM ${DOCKER_REGISTRY}/duckietown/dt-machine-learning-base-environment:${BASE_TAG}

ARG PIP_INDEX_URL="https://pypi.org/simple"
ENV PIP_INDEX_URL=${PIP_INDEX_URL}

# install Torch
ARG ARCH
COPY assets/${ARCH} "${REPO_PATH}/install"
RUN "${REPO_PATH}/install/install.sh"

# Setup any additional pip packages
COPY requirements.* ./
RUN cat requirements.* > .requirements.txt
RUN python3 -m pip install  -r .requirements.txt

RUN python3 -m pip uninstall -y dataclasses

# let's copy all our solution files to our workspace
WORKDIR /submission
COPY solution.py /submission
COPY models /submission/models
COPY model.py /submission
COPY wrappers.py /submission

CMD ["python3", "solution.py"]

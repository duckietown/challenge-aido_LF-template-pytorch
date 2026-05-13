# syntax=docker/dockerfile:1.4

# Definition of Submission container
ARG DOCKER_REGISTRY=docker.io
ARG ARCH=amd64
ARG DISTRO=ente
ARG BASE_TAG=${DISTRO}-${ARCH}

FROM ${DOCKER_REGISTRY}/duckietown/dt-machine-learning-base-pytorch:${BASE_TAG}

ARG PIP_INDEX_URL="https://pypi.org/simple/"
ENV PIP_INDEX_URL=${PIP_INDEX_URL}

COPY dependencies.txt /tmp/dependencies.txt
RUN if [ -s /tmp/dependencies.txt ]; then python3 -m pip install --no-cache-dir -r /tmp/dependencies.txt; fi

RUN python3 -m pip uninstall -y dataclasses

RUN rm -rf /workspace && mkdir /workspace

WORKDIR /workspace

COPY ./solution /workspace/solution
COPY ./training /workspace/training
COPY ./models /workspace/models

CMD ["python3", "-m", "solution.main"]

# syntax=docker/dockerfile:1.4

# Definition of Submission container
ARG DOCKER_REGISTRY=docker.io
ARG ARCH=amd64
ARG DISTRO=ente
ARG BASE_TAG=${DISTRO}-${ARCH}

FROM ${DOCKER_REGISTRY}/duckietown/dt-machine-learning-base-pytorch:${BASE_TAG}

ARG PIP_INDEX_URL="https://pypi.org/simple/"
ENV PIP_INDEX_URL=${PIP_INDEX_URL}

COPY --from=zuper-typing-z6 . /vendor/zuper-typing-z6
COPY --from=duckietown-messages . /vendor/duckietown-messages
COPY --from=duckietown-sdk . /vendor/duckietown-sdk
COPY --from=aido-protocols . /vendor/aido-protocols
COPY --from=gym-duckiematrix . /vendor/gym-duckiematrix
COPY --from=dt-duckiematrix assets/embedded_maps /opt/duckietown/dt-duckiematrix/maps
RUN python3 -m pip install \
    /vendor/zuper-typing-z6 \
    /vendor/duckietown-messages \
    /vendor/duckietown-sdk \
    /vendor/aido-protocols \
    /vendor/gym-duckiematrix

RUN python3 -m pip uninstall -y dataclasses

RUN rm -rf /workspace && mkdir /workspace

WORKDIR /workspace

COPY ./solution /workspace/solution
COPY ./training /workspace/training
COPY ./models /workspace/models

CMD ["python3", "-m", "solution.main"]

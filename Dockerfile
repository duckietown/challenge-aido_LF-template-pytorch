# Definition of Submission container
ARG AIDO_REGISTRY=docker.io
FROM ${AIDO_REGISTRY}/duckietown/dt-machine-learning-base-environment:daffy-amd64

ARG PIP_INDEX_URL="https://pypi.org/simple"
ENV PIP_INDEX_URL=${PIP_INDEX_URL}

# Setup any additional pip packages
RUN pip3 install -U "pip>=20.2"
COPY requirements.* ./
RUN cat requirements.* > .requirements.txt
RUN  pip3 install --use-feature=2020-resolver -r .requirements.txt

RUN pip3 uninstall -y dataclasses

# let's copy all our solution files to our workspace
WORKDIR /submission
COPY solution.py /submission
COPY models /submission/models
COPY model.py /submission
COPY wrappers.py /submission

# let's see what you've got there...
ENTRYPOINT ["python3", "solution.py"]
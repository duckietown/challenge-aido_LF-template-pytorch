# Definition of Submission container
ARG AIDO_REGISTRY
FROM ${AIDO_REGISTRY}/duckietown/dt-machine-learning-base-environment:daffy-amd64

# let's copy all our solution files to our workspace
# if you have more file use the COPY command to move them to the workspace
WORKDIR /submission

ARG PIP_INDEX_URL
ENV PIP_INDEX_URL=${PIP_INDEX_URL}
RUN echo PIP_INDEX_URL=${PIP_INDEX_URL}

# here, we install the requirements, some requirements come by default
# you can add more if you need to in requirements.txt
RUN pip3 install -U "pip>=20.2"
COPY requirements.* ./
RUN cat requirements.* > .requirements.txt
RUN  pip3 install --use-feature=2020-resolver -r .requirements.txt

RUN pip3 uninstall -y dataclasses

# let's copy all our solution files to our workspace
# if you have more file use the COPY command to move them to the workspace
COPY solution.py /workspace
COPY models /workspace/models
COPY model.py /workspace
COPY wrappers.py /workspace

# let's see what you've got there...
ENTRYPOINT ["python3", "solution.py"]
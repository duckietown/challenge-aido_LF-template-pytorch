# Definition of Submission container

FROM duckietown/aido2-base-python3:z2

# DO NOT MODIFY: your submission won't run if you do
RUN apt-get update -y && apt-get install -y --no-install-recommends \
         gcc \
         libc-dev\
         git \
         bzip2 \
         python-tk && \
     rm -rf /var/lib/apt/lists/*

# let's create our workspace, we don't want to clutter the container
WORKDIR /workspace

# here, we install the requirements, some requirements come by default
# you can add more if you need to in requirements.txt
COPY requirements.txt .
RUN pip install -r requirements.txt

# let's copy all our solution files to our workspace
# if you have more file use the COPY command to move them to the workspace
COPY solution.py /workspace
COPY models /workspace/models
COPY model.py /workspace
COPY wrappers.py /workspace


CMD python solution.py

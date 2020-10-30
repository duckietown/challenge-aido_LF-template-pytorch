FROM frank1chude1qian/dt-ml-base:latest

# let's copy all our solution files to our workspace
# if you have more file use the COPY command to move them to the workspace
COPY solution.py /submission
COPY models /submission/models
COPY model.py /submission
COPY wrappers.py /submission

# let's see what you've got there...
ENTRYPOINT ["python3", "solution.py"]
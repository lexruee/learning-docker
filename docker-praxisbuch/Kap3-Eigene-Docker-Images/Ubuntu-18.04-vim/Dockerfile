FROM ubuntu:18.04
RUN apt-get -y update \
    && apt-get -y install vim \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
CMD ["/bin/bash"]

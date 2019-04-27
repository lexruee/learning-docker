FROM ubuntu:18.04
RUN apt-get -y update \
    && apt-get -y install python3 python3 ipython3 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
CMD ["ipython3"]
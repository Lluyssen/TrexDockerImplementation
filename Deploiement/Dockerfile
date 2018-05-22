FROM debian:jessie

RUN \
	apt-get update && \
  	apt-get install -y python python-dev python-pip python-virtualenv && \
	rm -rf /var/lib/apt/lists/*

RUN pip install trex trex-api pyyaml pexpect
RUN pip install docker==2.0.1


COPY Docker /usr/local/Docker

WORKDIR /usr/local/Docker
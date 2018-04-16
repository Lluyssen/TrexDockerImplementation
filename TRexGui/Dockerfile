# Dockerfile

FROM debian:jessie

MAINTAINER  Lino Luyssen TrexGui

RUN  echo "===> update and upgrade" && \
     apt-get update && \
     apt-get upgrade -y
     #apt-get install -y  software-properties-common

RUN  echo "===> add webupd8 repository..." && \
     echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" | tee /etc/apt/sources.list.d/webupd8team-java.list && \
     echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" | tee -a /etc/apt/sources.list.d/webupd8team-java.list && \
     apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EEA14886

RUN  echo "===> install additional pack" && \
     apt-get update  && \
     apt-get install -y gtk2-engines libxtst6 libxxf86vm1 freeglut3 libxslt1.1

RUN  echo "===> install Java" && \
     apt-get update && \
     echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-selections && \
     echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-selections && \
     DEBIAN_FRONTEND=noninteractive  apt-get install -y --force-yes oracle-java8-installer oracle-java8-set-default

RUN  echo "===> clean up..." && \
     rm -rf /var/cache/oracle-jdk8-installer && \
     apt-get clean && \
     rm -rf /var/lib/apt/lists/*

CMD ./usr/local/gui/trex-stateless-gui

RUN echo "===> TrexGui part..." && \
    mkdir /usr/local/gui/
ADD https://github.com/cisco-system-traffic-generator/trex-stateless-gui/releases/download/v4.2.3/trex-stateless-gui-4.2.3.tgz /usr/local/gui/trex-stateless-gui-4.2.3.tgz
RUN tar -xvf /usr/local/gui/trex-stateless-gui-4.2.3.tgz -C /usr/local/gui/
COPY sfr_delay_10_1g.yaml /usr/local/gui/
COPY trex_08_5mflows.yaml /usr/local/gui/
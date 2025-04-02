FROM ubuntu:24.04

RUN rm /bin/sh && ln -s /bin/bash /bin/sh

ENV TZ=America/Sao_Paulo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get -y update

WORKDIR /home

RUN apt-get -y install openjdk-8-jdk openjdk-17-jdk android-sdk build-essential pipx 

ENV ANDROID_HOME=/usr/lib/android-sdk/
RUN export ANDROID_HOME
# ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64/
ENV JAVA_HOME=/usr/lib/jvm/java-8-openjdk-arm64/

RUN export JAVA_HOME 

ENV PATH=$JAVA_HOME/bin:$PATH
ENV PATH="${PATH}:${ANDROID_HOME}tools/:${ANDROID_HOME}platform-tools/:${ANDROID_HOME}tools/bin:"

ADD ./cryptoRunner /home/cryptoRunner

RUN chmod -R 755 /home
RUN chmod -R 777 /home/cryptoRunner/results

WORKDIR /home/cryptoRunner/script

RUN pipx install unicode

# CMD python3 runnerAndroidExperiment.py 
# CMD python3 runnerExperiment.py 
# CMD python3 runnerCryptoGuard.py 
# CMD python3 runnerCryptoGuardAndroid.py 

#!/bin/bash

docker run -it -v $(pwd)/cryptoRunner/results:/home/cryptoRunner/results -v $(pwd)/cryptoRunner/projects:/home/cryptoRunner/projects -v $(pwd)/cryptoRunner/script:/home/cryptoRunner/script --name crypto-runner amaralh/crypto-runner:latest

# export JAVA_HOME="/usr/lib/jvm/java-8-openjdk-amd64/"
# export PATH=$JAVA_HOME/bin:$PATH
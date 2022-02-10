# CryptoAnalysisSAST and CryptoGuard Runner

Environment to run Static Analysis tools and Detect Crypto-API misuses in Java and Android projects.

## CognyCryptSAST:
https://github.com/CROSSINGTUD/CryptoAnalysis

## CryptoGuard: 
https://github.com/CryptoGuardOSS/cryptoguard


## How to run

- Clone this repository:

     `git clone https://github.com/luisamaralh/cryptoSASTRunner.git`
     
- Run build.sh to configure the environment:

     `cd cryptoSASTRunner`
     
     `./build.sh`
     
- Run Docker container:
     './run.sh'
  
<!-- - Create folders to receive the Java and/or Android projects to be analyzed and the output folders:  

     `cd cryptoSASTRunner/cryptoRunner`
     
     `mkdir -p projects/apks`
     
     `mkdir -p projects/jars`
     
     `mkdir -p results/cryptoAnalysisOutput`
     
     `mkdir -p results/cryptoGuardOutput`
     
     `cd ..`

- Build docker image:
    `docker build -t cryptorunner:1.0 .`

- Run docker container:

    `docker run -it -v ./cryptoRunner/results:/home/cryptoRunner/results -v ./cryptoRunner/projects:/home/cryptoRunner/projects -v ./cryptoRunner/script:/home/cryptoRunner/script --name cryptorunner cryptorunner:1.0`
 -->
- There are for python scripts to execute the analysis inside the Docker:
    - runnerExperiment.py (execute CogniCryptSAST on Java projects inside of `/home/cryptoRunner/projects/jars` folder)
    - runnerAndroidExperiment.py (execute CogniCryptSAST on Android projects inside of `/home/cryptoRunner/projects/apks` folder)
    - runnerCryptoGuard.py (execute CryptoGuard on Java projects inside of `/home/cryptoRunner/projects/jars` folder)
    - runnerCryptoGuardAndroid.py (execute CryptoGuard on Android projects inside of `/home/cryptoRunner/projects/apks` folder)

### Docker

- System requirements:
    - Docker version 20.10.12

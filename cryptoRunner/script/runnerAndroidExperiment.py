from email.mime import base
import os
import glob
import subprocess
import time
import unidecode 

start_time = time.time()

basePath = "/home/cryptoRunner/"
# basePath = '/Users/Amaral/tools/crypto-analysis-runner/fse2022/'

outputPath = basePath + "results/cryptoAnalysisOutput/"
reportPath = basePath + "results/cryptoReportOutput/"
summaryPath = basePath + "results/cryptoSummaryOutput/"
sarifPath = basePath + "results/cryptoSarifOutput/"
apksPath = basePath + 'projects/apks/'
jarPath=  basePath + 'src/CryptoAnalysis-Android-2.8.0-SNAPSHOT-jar-with-dependencies.jar'
rulesPath = basePath + 'src/JCA/'
platformsPath = '/usr/lib/android-sdk/platforms/'

os.chdir(apksPath)

extension = 'apk'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

for file in all_filenames:
    subprocess.call(['java', '-Xmx8g', '-Xss128m', '-cp', jarPath, 'de.fraunhofer.iem.crypto.CogniCryptAndroidAnalysis',
                 apksPath + file, platformsPath,  rulesPath, outputPath])
    
    print("Analysis finished for prject: " + file)
    
    file = unidecode.unidecode(file) 
    subprocess.call(['mv', outputPath + "CryptoAnalysis-Report.csv", reportPath + file + "-report.csv"])
    subprocess.call(['mv', outputPath + "CryptoAnalysis-Summary.csv", summaryPath + file + "-summary.csv"])
    subprocess.call(['mv', outputPath + "CryptoAnalysis-Report.json", sarifPath + file + "-sarif.json"])


print("Analysis finished for: ")
print(all_filenames)
print("--- %s seconds ---" % (time.time() - start_time))


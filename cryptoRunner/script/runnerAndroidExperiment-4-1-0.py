from email.mime import base
import os
import glob
import subprocess
import time
import unidecode 

start_time = time.time()

basePath = "/home/cryptoRunner/"

outputPath = basePath + "results/cryptoAnalysisOutput/"
reportPath = basePath + "results/cryptoReportOutput/"
summaryPath = basePath + "results/cryptoSummaryOutput/"
sarifPath = basePath + "results/cryptoSarifOutput/"
apksPath = basePath + 'projects/apks/'
jarPath=  basePath + 'src/HeadlessAndroidScanner-4.1.0-jar-with-dependencies.jar'
rulesPath = basePath + 'src/JavaCryptographicArchitecture/'
platformsPath = '/usr/lib/android-sdk/platforms/'

os.chdir(apksPath)

extension = 'apk'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

for file in all_filenames:
    subprocess.call(['java', '-Xmx8g', '-Xss128m', '-jar', jarPath,'--apkFile',apksPath + file,
                     '--platformDirectory', platformsPath, '--rulesDir', rulesPath, '--reportPath', outputPath, '--reportFormat', 'CSV'])
    
    print("Analysis finished for prject: " + file)
    
    file = unidecode.unidecode(file) 
    subprocess.call(['mv', outputPath + "CryptoAnalysis-Report.csv", reportPath + file + "-report.csv"])


print("Analysis finished for: ")
print(all_filenames)
print("--- %s seconds ---" % (time.time() - start_time))


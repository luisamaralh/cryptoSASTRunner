import os
import glob
import subprocess
import time
import unidecode 

start_time = time.time()
basePath = "/home/cryptoRunner/"

outputPath = basePath + 'results/cryptoAnalysisOutput/'
reportPath = basePath + 'results/cryptoReportOutput/'
summaryPath = basePath + 'results/cryptoSummaryOutput/'
sarifPath = basePath + 'results/cryptoSarifOutput/'
jarsPath = basePath + 'projects/jars/'
jarPath= basePath + 'src/CryptoAnalysis-2.8.0-SNAPSHOT-jar-with-dependencies.jar'
rulesPath = basePath + 'src/JCA/'

os.chdir(jarsPath)

extension = 'jar'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

for file in all_filenames:
    subprocess.call(['java', '-Xmx8g', '-Xss128m', '-cp', jarPath, 
               'crypto.HeadlessCryptoScanner', '--rulesDir', rulesPath, 
                     '--appPath', jarsPath + file, '--reportPath', outputPath, 
                     '--reportFormat', 'TXT'])
    print("Analysis finished for prject: " + file)

    file = unidecode.unidecode(file) 
    subprocess.call(['mv', outputPath + "CryptoAnalysis-Report.csv", reportPath + file + "-report.csv"])
    subprocess.call(['mv', outputPath + "CryptoAnalysis-Summary.csv", summaryPath + file + "-summary.csv"])


print("Analysis finished for: ")
print(all_filenames)
print("--- %s seconds ---" % (time.time() - start_time))

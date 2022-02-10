import os
import glob
import subprocess
import time

start_time = time.time()

basePath = "/home/cryptoRunner/"
# basePath = "/Users/Amaral/tools/crypto-analysis-runner/fse2022/cryptoRunner/"

outputPath = basePath + "results/cryptoGuardOutput/"
jarsPath = basePath + 'projects/jars/'
jarPath=  basePath + 'src/cryptoguard.jar'

os.chdir(jarsPath)

extension = 'jar'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

# print(all_filenames)

os.chdir(outputPath)
# AnalysisOutput = open(outputPath + 'AnalysisResults.txt', 'w')
for file in all_filenames:
    subprocess.call(['java', '-Xmx8g', '-Xss128m', '-jar', jarPath,'-in', 'jar', '-s', jarsPath + file , '-m', 'D'])
    print("Analysis finished for project: " + file)

print("Analysis finished for: ")
print(all_filenames)
print("--- %s seconds ---" % (time.time() - start_time))

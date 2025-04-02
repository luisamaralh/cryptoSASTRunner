import os
import glob
import subprocess
import threading
import json
import csv
import concurrent.futures


# Função para converter JSON para CSV
def json_issues_to_csv(input_json_file, output_csv_file):
    # Abra o arquivo JSON de entrada para leitura
    with open(input_json_file, 'r') as json_file:
        data = json.load(json_file)

    # Abra o arquivo CSV de saída para escrita
    with open(output_csv_file, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)

        # Escreva o cabeçalho do CSV
        csv_writer.writerow(['Message', 'Description', 'RuleNumber', 'RuleDesc', 'CWEId', 'Severity', 'ClassName', 'MethodName'])

        # Extraia as questões (issues) do JSON e escreva no CSV
        issues = data.get('Issues', [])
        
        for issue in issues:
            message = issue.get('Message', '')
            description = issue.get('Description', '')
            ruleNumber = issue.get('RuleNumber', '')
            ruleDesc = issue.get('RuleDesc', '')
            cweId = issue.get('CWEId', '')
            severity = issue.get('Severity', '')
            location = issue.get('Location', {})
            className = location.get('ClassName', '')
            methodName = location.get('MethodName', '')
            
            csv_writer.writerow([message, description, ruleNumber, ruleDesc, cweId, severity, className, methodName])




def process_apk(apk):
    print(apksPath + apk)
    cmd = ['java', '-Xmx18g', '-Xss1024m', '-jar', jarPath, '-in', 'apk', '-s', apksPath + apk, '-m', 'D', '-o', apk + '.json']
    timeout_s = 3600
    try:
        p = subprocess.run(cmd, timeout=timeout_s)
        input_json_file = jsonOutputPath + apk + '.json'
        output_csv_file = csvOutputPath + apk + '.csv'
        json_issues_to_csv(input_json_file, output_csv_file)
        print("Cryptoguard analysis finished for project: " + apk)
        successList.append(apk)
    except subprocess.TimeoutExpired:
        timeoutList.append(apk)
        print(f'Timeout for {apk} ({timeout_s}s) expired')

basePath = "/home/cryptoRunner/"
jsonOutputPath = basePath + "results/cryptoGuardOutput/json/"
csvOutputPath = basePath + "results/cryptoGuardOutput/csv/"
apksPath = basePath + 'projects/apks/'
jarPath=  basePath + 'src/cryptoguard-develop.jar'


os.chdir(csvOutputPath)
extension = 'csv'
listApps = finishedApps = []
all_files = [i for i in glob.glob('*.{}'.format(extension))]
for file in all_files:
    file = file.replace('.csv', '')
    finishedApps.append(file)

os.chdir(apksPath)
extension = 'apk'
all_apks = [i for i in glob.glob('*.{}'.format(extension))]

listApps = list(set(all_apks)-set(finishedApps))

os.chdir(jsonOutputPath)

successList = []
timeoutList = []

# Use a ThreadPoolExecutor to run the subprocess calls in 10 threads
max_threads = 4
with concurrent.futures.ThreadPoolExecutor(max_threads) as executor:
    futures = [executor.submit(process_apk, apk) for apk in listApps]

    # Wait for all tasks to complete
    for future in concurrent.futures.as_completed(futures):
        # Handle any exceptions raised by the threads, if needed
        if future.exception() is not None:
            print(f"Thread raised an exception: {future.exception()}")

print("All APKs processed.") 
print(successList)
print(timeoutList)

import os
import subprocess
import json
import csv
import glob

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



basePath = "/home/cryptoRunner/"
jsonOutputPath = basePath + "results/cryptoGuardOutput/json/"
csvOutputPath = basePath + "results/cryptoGuardOutput/csv/"
apksPath = basePath + 'projects/apks/'
jarPath=  basePath + 'src/cryptoguard-develop.jar'


os.chdir(apksPath)
extension = 'apk'
apks = [i for i in glob.glob('*.{}'.format(extension))]

os.chdir(jsonOutputPath)

successList = []
timeoutList = []
for apk in apks:
    cmd = ['java','-Xmx24g', '-Xss512m','-jar', jarPath,'-in', 'apk', '-s',apksPath + apk , '-m', 'D', '-o', apk + '.json']
    timeout_s = 3000
    try:
        p = subprocess.run(cmd, timeout=timeout_s)
        # Nome do arquivo JSON de entrada e arquivo CSV de saída
        input_json_file = jsonOutputPath + apk + '.json'
        output_csv_file = csvOutputPath + apk + '.csv'

        # Chame a função para converter JSON para CSV
        json_issues_to_csv(input_json_file, output_csv_file)
        print("Cryptoguard analysis finished for prject: " + apk)
        successList.append(apk)
    except subprocess.TimeoutExpired:
        timeoutList.append(apk)
        print(f'Timeout for {apk} ({timeout_s}s) expired')

print('Analysis finished for: ')
print(apks)

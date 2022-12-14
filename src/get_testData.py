import os, requests, json, base64
from os import environ

SELNAME = environ.get('SELNAME')
if SELNAME is None:
    SELNAME = "localhost"
SELPORT = environ.get('SELPORT')
if SELPORT is None:
    SELPORT = "4444"
HOSTNAME = environ.get('HOSTNAME')
if HOSTNAME is None:
    HOSTNAME = "localhost"
print(SELNAME, SELPORT, HOSTNAME)

allure_results_directory = '/results_allure'
allure_server = 'https://allure.i.clive.tk/api'
project_id = 'wallettest'


current_directory = os.path.dirname(os.path.realpath(__file__))
results_directory = current_directory + allure_results_directory
print('RESULTS DIRECTORY PATH: ' + results_directory)

files = os.listdir(results_directory)

print('FILES:')
results = []
for file in files:
    result = {}

    file_path = results_directory + "/" + file
    print(file_path)

    if os.path.isfile(file_path):
        try:
            with open(file_path, "rb") as f:
                content = f.read()
                if content.strip():
                    b64_content = base64.b64encode(content)
                    result['file_name'] = file
                    result['content_base64'] = b64_content.decode('UTF-8')
                    results.append(result)
                else:
                    print('Empty File skipped: ' + file_path)
        finally:
            f.close()
    else:
        print('Directory skipped: ' + file_path)

headers = {'Content-type': 'application/json'}
request_body = {
    "results": results
}
json_request_body = json.dumps(request_body)

print("------------------SEND-RESULTS------------------")
headers = {
    'accept': '*/*',
    'Content-Type': 'application/json'
}

session = requests.Session()
response = session.post(allure_server + '/allure-docker-service/send-results?project_id=' + project_id, headers=headers, data=json_request_body, verify=False)
print("STATUS CODE:")
print(response.status_code)
print("RESPONSE:")
json_response_body = json.loads(response.content)
json_prettier_response_body = json.dumps(json_response_body, indent=4, sort_keys=True)
print(json_prettier_response_body)

print("------------------GENERATE-REPORT------------------")
execution_name = 'execution from my script'
execution_from = f'{HOSTNAME}'
execution_type = 'teamcity'
response = session.get(allure_server + '/allure-docker-service/generate-report?project_id=' + project_id + '&execution_name=' + execution_name + '&execution_from=' + execution_from + '&execution_type=' + execution_type, headers=headers, verify=False)

print("STATUS CODE:")
print(response.status_code)
print("RESPONSE:")
json_response_body = json.loads(response.content)
json_prettier_response_body = json.dumps(json_response_body, indent=4, sort_keys=True)
print(json_prettier_response_body)
print('ALLURE REPORT URL:')
print(json_response_body['data']['report_url'])
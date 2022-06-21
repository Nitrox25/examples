import os, requests, json, base64
# TODO запилить одну папку  results со junit и  allure
# This directory is where you have all your results locally, generally named as `allure-results`
allure_results_directory = '/results_allure'
# This url is where the Allure container is deployed. We are using localhost as example
allure_server = 'https://allure.i.clive.tk/api'
# Project ID according to existent projects in your Allure container - Check endpoint for project creation >> `[POST]/projects`
project_id = 'wallettest'
# project_id = 'my-project-id'
# Set security_user & security_password according to Allure container configuration


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

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

print("------------------Create a new project------------------")
url = "https://allure.i.clive.tk/api/allure-docker-service/projects"
payload = json.dumps({
    "id": f"{HOSTNAME}"
})
headers = {
    'accept': '*/*',
    'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload, verify=False)

print(response.text)

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
    HOSTNAME = "dev.megadex.clive.tk"
print(SELNAME, SELPORT, HOSTNAME)

print("------------------Create a new project------------------")

new_HOSTNAME = HOSTNAME.replace('.', '-')


url = "https://allure.i.clive.tk/api/allure-docker-service/projects"
payload = json.dumps({
    "id": f"{new_HOSTNAME}"
})
headers = {
    'accept': '*/*',
    'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload, verify=False)

print(response.text)

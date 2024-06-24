import requests
import utils

url = "https://hash-browns.cs.uwaterloo.ca/api/plain/inbox"
headers = { "Accept": "application/json", "Content-Type" : "application/json" }
body = {
    "api_token": "697b4f056c1fd75cd72c58e27951accb54bef798f3525eb15f8d6d7aa0c165a0",
    }
# print(body)
result = requests.post(url=url, headers=headers, json=body)
# print("the status code is:", result.status_code)
print(utils.from_base64(result.json()[0]["msg"]))
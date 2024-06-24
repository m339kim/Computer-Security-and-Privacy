import requests
import utils

def to_base64(s: str):
    return base64.b64encode(s.encode('ascii')).decode('ascii')

url = "https://hash-browns.cs.uwaterloo.ca/api/plain/send"
headers = { "Accept" : "application/json", "Content-Type" : "application/json" }
json = { 
    "api_token": "697b4f056c1fd75cd72c58e27951accb54bef798f3525eb15f8d6d7aa0c165a0",
    "recipient": "Gooser",
    "msg" : utils.to_base64("Hello, World!")
    }
result = requests.post(url = url,  headers = headers,  json = json)
# print(result.status_code)
# print(result.text)
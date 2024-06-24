import requests
import utils
import nacl.secret
import nacl.utils


secret_shared_key = bytes.fromhex("a4132e9f43de8c106c25ba580996809e340913ce123bb3cbe153a79e8f445150")
encryted_message = nacl.secret.SecretBox(secret_shared_key).encrypt(b"Hello World!")

url = "https://hash-browns.cs.uwaterloo.ca/api/psk/send"
headers = { "Accept" : "application/json", "Content-Type" : "application/json" }
json = { 
    "api_token": "697b4f056c1fd75cd72c58e27951accb54bef798f3525eb15f8d6d7aa0c165a0",
    "recipient": "Gooser",
    "msg" : utils.to_base64_bytes(encryted_message)
    }
result = requests.post(url = url,  headers = headers,  json = json)
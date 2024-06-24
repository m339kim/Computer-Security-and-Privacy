import requests
import nacl
from nacl import pwhash, secret
import utils

# Pre-shared password: domestic horse
# Argon2id salt: 11c6fc8a187c10eff35a95ff97a48aac
# Argon2id operations limit: 2
# Argon2id memory limit: 67108864

encrypted = pwhash.argon2id.kdf(
    size=secret.SecretBox.KEY_SIZE, 
    password=b"domestic horse", 
    salt=bytes.fromhex("11c6fc8a187c10eff35a95ff97a48aac"), 
    opslimit=2, 
    memlimit=67108864
)
secret_box = secret.SecretBox(encrypted)

url = "https://hash-browns.cs.uwaterloo.ca/api/psp/inbox"
headers = {"Accept": "application/json", "Content-Type" : "application/json"}
json = {
    "api_token": "697b4f056c1fd75cd72c58e27951accb54bef798f3525eb15f8d6d7aa0c165a0",
}
response = requests.post(url=url, headers=headers, json=json)

response_in_bytes = utils.from_base64_bytes(response.json()[0]["msg"])

text = secret_box.decrypt(response_in_bytes)
print(text.decode('utf-8'))
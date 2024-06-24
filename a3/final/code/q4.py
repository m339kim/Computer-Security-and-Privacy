import requests
import binascii

import nacl
import nacl.secret
import nacl.utils
import nacl.pwhash
from nacl.signing import SigningKey

import utils

# a. upload public verif key
signing_key = SigningKey.generate() # random signing key
print(binascii.hexlify(signing_key.verify_key.encode())) # encode it

url = "https://hash-browns.cs.uwaterloo.ca/api/signed/set-key"
headers = { "Accept": "application/json", "Content-type": "application/json" }
json = {
  "api_token": "697b4f056c1fd75cd72c58e27951accb54bef798f3525eb15f8d6d7aa0c165a0",
  "pubkey": utils.to_base64_bytes(signing_key.verify_key.encode())
}
response = requests.post(url=url, headers=headers, json=json)
# print(response.json())

# b. send a message
url = "https://hash-browns.cs.uwaterloo.ca/api/signed/send"
headers =  { "Accept": "application/json", "Content-type": "application/json" }
json = {
  "api_token": "697b4f056c1fd75cd72c58e27951accb54bef798f3525eb15f8d6d7aa0c165a0",
  "recipient": "Gooser",
  "msg": utils.to_base64_bytes(signing_key.sign(b"testing q4"))
}
response = requests.post(url=url, headers=headers, json=json)
# print(response.json())
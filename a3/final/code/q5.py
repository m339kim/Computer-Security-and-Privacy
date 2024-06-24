import requests
import nacl.encoding
import nacl.hash
import nacl.utils
from nacl.public import PrivateKey, Box

import utils

# a. verify public key
url1 = 'https://hash-browns.cs.uwaterloo.ca/api/pke/get-key'
headers = { 'Accept': 'application/json', 'Content-type': 'application/json' }
json1 = {
  "api_token": '697b4f056c1fd75cd72c58e27951accb54bef798f3525eb15f8d6d7aa0c165a0',
  "user": "Gooser"
}
response = requests.post(url=url1, headers=headers, json=json1)
pubkey_bytes = nacl.encoding.Base64Encoder.decode(response.json()['pubkey'].encode('utf-8'))
pubkey_hash = nacl.hash.blake2b(pubkey_bytes, encoder=nacl.encoding.HexEncoder)
pubkey_hash_str = pubkey_hash.decode('utf-8')
print(pubkey_hash_str)


# b. send a message
url2 = 'https://hash-browns.cs.uwaterloo.ca/api/pke/set-key'
seckey = PrivateKey.generate()
pubkey = seckey.public_key
pubkey_str = nacl.encoding.Base64Encoder.encode(pubkey.encode()).decode('utf-8')
json2 = {
    "api_token": '697b4f056c1fd75cd72c58e27951accb54bef798f3525eb15f8d6d7aa0c165a0',
    "pubkey": pubkey_str
}
response = requests.post(url=url2, headers=headers, json=json2)

url2 = 'https://hash-browns.cs.uwaterloo.ca/api/pke/send'
secret_box = Box(seckey, nacl.public.PublicKey(pubkey_bytes))
msg = "q5 part 2 test"
b64_box_encr_msg_str = nacl.encoding.Base64Encoder.encode(
                            secret_box.encrypt(
                                msg.encode('utf-8'), 
                                nacl.utils.random(Box.NONCE_SIZE))
                       ).decode('utf-8')
json2 = {
    "api_token": '697b4f056c1fd75cd72c58e27951accb54bef798f3525eb15f8d6d7aa0c165a0',
    "recipient": "Gooser",
    "msg": b64_box_encr_msg_str
}
response = requests.post(url=url2, headers=headers, json=json2)


# c. receive a message
url3 = 'https://hash-browns.cs.uwaterloo.ca/api/pke/inbox'
json3 = {
    "api_token": '697b4f056c1fd75cd72c58e27951accb54bef798f3525eb15f8d6d7aa0c165a0'
}
response = requests.post(url=url3, headers=headers, json=json3)
response_msg_str = nacl.encoding.Base64Encoder.decode(response.json()[0]['msg'].encode('utf-8'))
print(secret_box.decrypt(response_msg_str).decode('utf-8'))

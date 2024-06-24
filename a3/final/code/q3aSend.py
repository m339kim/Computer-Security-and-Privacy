import requests
import utils
from nacl import pwhash, secret
import nacl

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
nonce = nacl.utils.random(secret.SecretBox.NONCE_SIZE)

msg = b"Q3b message"
encrypted = secret_box.encrypt(b"encrypted message")

url = "https://hash-browns.cs.uwaterloo.ca/api/psp/send"
headers = {"Accept": "application/json", "Content-Type" : "application/json"}
json = {
    "api_token": "697b4f056c1fd75cd72c58e27951accb54bef798f3525eb15f8d6d7aa0c165a0",
    "recipient": "Gooser", 
    "msg": utils.to_base64_bytes(secret_box.encrypt(msg, nonce))  
}
response = requests.post(url=url, headers=headers, json=json)

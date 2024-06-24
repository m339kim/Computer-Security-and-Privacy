import base64

def to_base64(s: str):
    return base64.b64encode(s.encode('ascii')).decode('ascii')

def to_base64_bytes(bytes):
    return base64.b64encode(bytes).decode('ascii')

def from_base64(code: str):
    return base64.b64decode(code.encode('ascii')).decode('ascii')

def from_base64_bytes(bytes):
    return base64.b64decode(bytes)

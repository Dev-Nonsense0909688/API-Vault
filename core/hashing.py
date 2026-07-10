from hashlib import sha256
import base64

def hash_key(text: str):
    return base64.urlsafe_b64encode(sha256(text.encode()).digest())

def hash_token(text: str):
    return sha256(text.encode()).hexdigest()